from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os, nginx, yaml, shutil


# ----------------------#----------------------
# read engine configuration and set variables #
# ----------------------#----------------------
with open(r'./conf/conf.yml') as configfile:
    configuration = yaml.load(configfile, Loader=yaml.FullLoader)
    applicationsConfigPath = configuration['applications']['config_path']
    appRtmpPort = str(configuration['applications']['rtmp_port'])
    appHlsPort = str(configuration['applications']['hls_port'])
    appHlsPath = configuration['applications']['hls_path']
    appHlsFragment = str(configuration['applications']['hls_fragment'])
    appHlsPlaylistLength = str(configuration['applications']['hls_playlist_length'])
    appDenyPublishAll = bool(configuration['applications']['deny_publish_all'])
    appAllowPublishFrom = str(configuration['applications']['allow_publish_from'])
    appDenyPlayAll = bool(configuration['applications']['deny_play_all'])
    appAllowPlayFrom = str(configuration['applications']['allow_play_from'])
    backupDeletedApp = bool(configuration['applications']['backup_deleted'])


# Create your models here.
class Application(models.Model):
    name                = models.CharField(max_length=32, unique=True)
    description         = models.TextField(blank=True, null=True)
    types               = (("Live", "Live"),("VOD", "VOD"))
    type                = models.CharField(max_length=9,choices=types,default="Live")
    app_config_path     = models.CharField(max_length=512, default=applicationsConfigPath)
    rtmp_port           = models.CharField(max_length=8, default=appRtmpPort)
    hls_port            = models.CharField(max_length=8, default=appHlsPort)
    hls_path            = models.CharField(max_length=512, default=appHlsPath)
    hls_fragment        = models.CharField(max_length=8, default=appHlsFragment)
    hls_playlist_length = models.CharField(max_length=8, default=appHlsPlaylistLength)


@receiver(post_save, sender=Application)
def AddAppConfig(sender, instance, created, **kwargs):
    objectId = instance.id
    appName = instance.name
    hls_path = instance.hls_path
    hls_fragment = instance.hls_fragment
    hls_playlist_length = instance.hls_playlist_length
    if not os.path.isdir(applicationsConfigPath + '/' + appName):
        os.makedirs(applicationsConfigPath + '/' + appName)
    appConf = nginx.Conf()
    httpConf = nginx.Conf()
    # add RTMP config to nginx
    appConf.add(
        nginx.Comment('Application ' + appName + ' RTMP configuration')
    )
    appContainer = nginx.Container('application ' + appName)
    appContainer.add(
        nginx.Key('live', 'on'),
        nginx.Comment('Turn on HLS'),
        nginx.Key('hls', 'on'),
        nginx.Key('hls_path', hls_path + appName),
        nginx.Key('hls_fragment', hls_fragment),
        nginx.Key('hls_playlist_length', hls_playlist_length),
        nginx.Comment('disable consuming the stream from nginx as rtmp'),
        nginx.Key('allow publish', 'all'),
        nginx.Key('allow play', 'all'),
    )
    appConf.add(appContainer)
    nginx.dumpf(appConf, applicationsConfigPath + '/' + appName + '/Application.conf')
    # now the HLS
    httpConf.add(
        nginx.Comment('Application ' + appName + ' HLS configuration')
    )
    httpContainer = nginx.Location(' /' + appName,
        nginx.Comment('Disable cache'),
        nginx.Key('add_header', '\'Cache-Control\' \'no-cache\''),
        nginx.Comment('CORS setup'),
        nginx.Key('add_header', '\'Access-Control-Allow-Origin\' \'*\' always'),
        nginx.Key('add_header', '\'Access-Control-Expose-Headers\' \'Content-Length\''),
        nginx.Comment(''),
        nginx.Comment('allow CORS preflight requests'),
        nginx.If('($request_method = \'OPTIONS\')',
        nginx.Key('add_header', '\'Access-Control-Allow-Origin\' \'*\''),
        nginx.Key('add_header', '\'Access-Control-Max-Age\' 1728000'),
        nginx.Key('add_header', '\'Content-Type\' \'text/plain charset=UTF-8\''),
        nginx.Key('add_header', '\'Content-Length\' 0'),
        nginx.Key('return', '204'),
                 ),
        nginx.Types(
            nginx.Key('application/dash+xml', 'mpd'),
            nginx.Key('application/vnd.apple.mpegurl', 'm3u8'),
            nginx.Key('video/mp2t', 'ts')
        ),
        nginx.Key('root', hls_path)
                                   )
    httpConf.add(httpContainer)
    nginx.dumpf(httpConf, applicationsConfigPath + '/' + appName + '/http.conf')
    if created:
        print(appName, 'Obj ID', objectId, 'Created')
    elif not created:
        print(kwargs.get('instance'), appName, objectId, 'Updated')


@receiver(post_delete, sender=Application)
def DelAppConfig(sender, instance, **kwargs):
    appName = instance.name
    appConfigPath = applicationsConfigPath + '/' + appName
    appConfigBkpPath = applicationsConfigPath + '.bkp'
    if backupDeletedApp == True:
        if not os.path.isdir(appConfigBkpPath):
            os.makedirs(appConfigBkpPath)
        shutil.move(appConfigPath, appConfigBkpPath)
    else:
        if os.path.isdir(appConfigPath):
            shutil.rmtree(appConfigPath)
    print(kwargs.get('instance'), ' Deleted')




