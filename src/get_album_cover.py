import urllib.request

filename = './images/album_cover.jpg'

def fetch_image(image_url):
    urllib.request.urlretrieve(image_url, filename)
    return filename
