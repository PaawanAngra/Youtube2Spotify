import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authorize_spotify(client_id, client_secret):
    # Authorize the spotify using OAuth 2.0. The spotipy module caches the access token in a .cache file
    SCOPE = "playlist-modify-public playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id,
                                                client_secret = client_secret,
                                                redirect_uri="http://localhost:8080",
                                                scope = SCOPE))
    return sp

def create_playlist(name, sp = None):
    # Creates a playlist using the ID of the user currently logged in
    userid = sp.current_user()['id']
    response = sp.user_playlist_create(user = userid, name = name)
    return response['id']

def track_name_to_id(name, sp = None):
    # Searches for a given title and returns the ID of the first track in the results
    response = sp.search(name, type = 'track', limit=1)
    track = response['tracks']['items'][0]['id']
    return track

def add_to_playlist(songs, playlist_id, sp = None):
    # Adds a list of songs to the playlist of a given user
    user_id = sp.current_user()['id']
    sp.user_playlist_add_tracks(user = user_id, playlist_id = playlist_id, tracks = songs)
