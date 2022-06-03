import sys
import os 
import logging
from photo import Photo
from hosting import Imgur
from config import settings
import maproulette

if __name__ == "__main__":

	# Set up logging
	logging.basicConfig(
		stream=sys.stdout, 
		level=settings.get("log_level", 'INFO'),
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	logger = logging.getLogger('main')

	# Collect photo locations
	photos = []
	
	imgur_hoster = Imgur(credentials=settings['imgur_credentials'])

	for f in os.listdir(settings.get("photos_dir")):
		photo = Photo(
			local_path=os.path.join(settings.get("photos_dir"), f),
			hoster=imgur_hoster)
		if photo.is_jpeg and photo.location:
			photo.upload()
			logger.debug('{} uploaded to {}'.format(f, photo.url))
			photos.append(photo)
			logger.debug('{} added to photos list'.format(f))

	logger.info("{} photos with location found.".format(len(photos)))

	# Build Challenge creation payload
	challenge_payload = {
		"description": settings.get("challenge_description"),
		"difficulty": settings.get("challenge_difficulty"),
		"instruction": settings.get("challenge_instruction"),
		"name": settings.get("challenge_name"),
		"parent": settings.get("parent_project_id")
	}

	# Initialize MR API

	hostname = settings.get("maproulette_server_hostname") if "maproulette_server_hostname" in settings else "maproulette.org"
	protocol = settings.get("maproulette_server_protocol") if "maproulette_server_protocol" in settings else "https"
	config = maproulette.Configuration(
		api_key=settings.get("maproulette_api_key"),
		hostname=hostname)

	challenge_api = maproulette.Challenge(config)

	# Build tasks
