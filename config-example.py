settings = {
	# Location of image directory
	# ---------------------------
	# The path to the directory on your local machine where your geotagged
	# images are located. May be relative.
	"photos_dir": 					"/path/to/geotagged/photos",

	# Imgur credentials
	# Each image hoster class requires credentials which are documented at that class.
	# They take the form of a dictionary that you should define here.
	'imgur_credentials': 			{'Client-ID': '6ae1d910ca321bb'},

	# MapRoulette API key
	# -------------------
	# Your personal API key, which enables you to add new challenges using the
	# MapRoulette API. Go to https://maproulette.org/user/profile and scroll all
	# the way to the bottom to find it.
	"maproulette_api_key": 			"YOUR_MR_API_KEY_HERE",

	# MapRoulette server and protocol
	# -------------------------------
	# If you want to use an alternate MapRoulette server, you can define it here.
	# Leave these commented out if you just want to use the main maproulette.org server.
	# "maproulette_server_protocol": "https",
	# "maproulette_server_hostname": "staging.maproulette.org",

	# MapRoulette Project id
	# ----------------------
	# the id of the MapRoulette project you want to create this challenge under.
	# To find this, go to "Create and Manage" on the MapRoulette website 
	# and navigate to your project. The project id is the last part of the URL,
	# for example https://maproulette.org/admin/project/12345
	"parent_project_id": 		12345,

	# Challenge Metadata
	# ------------------
	# Required metadata for your challenge.
	# The name must be unique to MapRoulette, short and descriptive
	"challenge_name": 			"YOUR CHALLENGE NAME HERE",

	# The description, a longer but concise description of what the challenge is about
	"challenge_description": 	"YOUR CHALLENGE DESCRIPTION HERE",

	# The instruction for the mapper. The image thumbnail will be appended at the end.
	"challenge_instruction": 	"YOUR TASK INSTRUCTIONS HERE.",

	# The challenge's difficulty. 2 is normal
	"challenge_difficulty": 	2

	# Log level for logging output. This is useful if you're developing. Default is 'INFO'
	# 'log_level':					'DEBUG',
}