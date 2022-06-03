import os
import imghdr
import subprocess
import csv
from io import StringIO


class Photo:
    """A photo, its location, S3 URL

    :param local_path: local path to the image file
    """

    def __init__(self, local_path):
        self._local_path = local_path
        self._location = None

    def _get_exif_location(self):
        if self._location == None:
            exiftool_command = subprocess.run(
                'exiftool -GpsLongitude -GpsLatitude -T -c "%+.6f" {}'.format(self._local_path),
                capture_output=True,
                shell=True,
                text=True)
            self._location = exiftool_command.stdout[:-1].split("\t")
        return self._location

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
    
# exiftool -GpsLongitude -GpsLatitude -c "%+.6f" -csv ../photos/IMG_4062.jpg