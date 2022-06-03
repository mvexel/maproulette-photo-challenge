import sys
import os 
from utils import init_logger
from aws import S3
from photo import Photo
from config import settings
import maproulette

if __name__ == "__main__":

	logger = init_logger("root")

	# Collect photo locations
	photos = []
	for f in os.listdir(settings.get("photos_dir")):
		photo = Photo(os.path.join(settings.get("photos_dir"), f))
		if photo.is_jpeg:
			photos.append(photo)

	logger.info("{} photos found...".format(len(photos)))

	# Initialize S3 session
	s3_session = S3('maproulette')

	# Upload to S3
	logger.info("uploading files to S3...")
	for photo in photos:
		if s3_session.object_exists(settings.get("s3_bucket_name"), photo.name):
			logger.info("{} already in bucket".format(photo.name))
		else:
			logger.info("uploading {}...".format(photo.name))
			s3_session.upload_file(photo.local_path, settings.get("s3_bucket_name"))

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
