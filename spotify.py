import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authorize_spotify():
    SCOPE = "playlist-modify-public playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ab32d1d292a14c18922d55507b8bf739",
                                                client_secret="9e1098c1cc6d4a799ee067ae7dca221f",
                                                redirect_uri="http://localhost:8080",
                                                scope = SCOPE))
    return sp

def create_playlist(name = 'Youtube Liked', sp = None):
    userid = sp.current_user()['id']
    response = sp.user_playlist_create(user = userid, name = name)
    return response['id']

def track_name_to_id(name, sp = None):
    response = sp.search(name, type = 'track', limit=1)
    track = response['tracks']['items'][0]['id']
    return track

def add_to_playlist(songs, playlist_id, sp = None):
    user_id = sp.current_user()['id']
    sp.user_playlist_add_tracks(user = user_id, playlist_id = playlist_id, tracks = songs)
