import os
import logging
import requests

logger = logging.getLogger(__name__)

class Hoster:
	"""Image Hoster interface

	:param credentials: A dict with needed credentials to perform an upload action. If no credentials are required, an empty dict should be passed.
	"""	

	def __init__(self, credentials):
		pass

	def upload(self, local_path):
		"""Upload the image to the defined hoster"""
		pass


class Imgur(Hoster):
	"""Imgur image upload class

	:param credentials: A dict with needed credentials to perform an upload action. For imgur, this is a Client-ID, see https://apidocs.imgur.com/#c85c9dfc-7487-4de2-9ecd-66f727cf3139 and https://apidocs.imgur.com/?version=latest#authorization-and-oauth. Example: {"Client-ID": "12345"}
	"""	

	def __init__(self, credentials):
		self._credentials = credentials
		logger = logging.getLogger(__name__)

	def upload(self, local_path):
		"""Upload an image to imgur

		:param local_path: Local path to the image file. Must be <10MB as per imgur API restrictions
		:return: The URL at which the image can be retrieved
		"""

		IMGUR_UPLOAD_API_ENDPOINT = 'https://api.imgur.com/3/image'

		with open(local_path, 'rb') as fh:
	
		# Compose request
			headers = {"Authorization": "Client-ID {}".format(
				self._credentials["Client-ID"])}
			files = {'image': fh}
			response = requests.request(
				'POST',
				IMGUR_UPLOAD_API_ENDPOINT,
				headers=headers, 
				files=files,
			)
			logger.debug(response.text)

		return response.json()['data']['link']