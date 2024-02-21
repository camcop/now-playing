import urllib.request
from PIL import Image

filename = 'album_cover.jpg'

def fetch_image(image_url):
    urllib.request.urlretrieve(image_url, filename)
    # img = Image.open(filename)
    return filename
