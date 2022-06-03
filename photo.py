import os
import logging
import imghdr
import subprocess
import csv
from io import StringIO

logger = logging.getLogger(__name__)

class Photo:
    """A photo instance

    :param local_path: local path to the image file
    :param hoster: an instance of a Hoster subclass
    """

    def __init__(self, local_path, hoster):
        self._local_path = local_path
        self._hoster = hoster
        self._url = None

    def _get_exif_location(self):
        exiftool_command = subprocess.run(
            'exiftool -GpsLongitude -GpsLatitude -T -c "%+.6f" {}'.format(self._local_path),
            capture_output=True,
            shell=True,
            text=True)
        logger.debug('{} returned {}'.format(exiftool_command.args, exiftool_command.returncode))
        lon, lat = exiftool_command.stdout[:-1].split("\t")
        try:
            lon = float(lon)
            lat = float(lat)
            logger.debug('we have valid location EXIF')
            return (lon, lat)
        except ValueError:
            logger.info('{} does not have EXIF location information.'.format(self._local_path))
            return None
        else:
            logger.debug('something else is going on')

    def upload(self):
        self._url = self._hoster.upload(self._local_path)

    @property
    def local_path(self):
        return self._local_path

    @property
    def name(self):
        return os.path.basename(self._local_path)

    @property
    def is_jpeg(self):
        return imghdr.what(self._local_path) == 'jpeg'
    
    @property
    def location(self):
        return self._get_exif_location()
    
    @property
    def url(self):
        return self._url
    