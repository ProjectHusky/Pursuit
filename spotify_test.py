import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import spotify

client_credentials_manager = SpotifyClientCredentials(client_id="1b2cd56013a647308e007cb88a1f1d2c", client_secret="0b90798a8d2847938b977b428f0e210d")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlists = sp.user_playlists('tony.vo22')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

print(spotify.get_artist_id("Led Zeppelin", sp))
# seeds = ['7nKQ5WAcjnG48knyLuo8gO', '1h6QMOtZAR0wRyJBrqsoCt', '6Nle9hKrkL1wQpwNfEkxjh', '2xTft6GEZeTyWNpdX94rkf']
# recs = sp.recommendations(seed_artists=seeds)
