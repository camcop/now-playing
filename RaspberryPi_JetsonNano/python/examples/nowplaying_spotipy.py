import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                                               client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
                                               redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
                                               scope="user-read-currently-playing"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
    # track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])

currently_playing = sp.currently_playing()
print(currently_playing)
logging.info(currently_playing)

for idx, item in enumerate(currently_playing['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
