from hosting import Imgur

credentials = {
	"Client-ID": "6ae1d910ca321bb"
}

photo_local_path = "photos/IMG_4054.jpg"

imgur = Imgur(credentials=credentials)

print (imgur.upload(photo_local_path))