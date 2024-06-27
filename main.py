import youtube
import spotify

songs_on_youtube = youtube.retrieve_youtube_playlist()

sp = spotify.authorize_spotify()
song_ids = []
for song in songs_on_youtube:
    print(f'Retrieving ID for {song}')
    song_ids.append(spotify.track_name_to_id(song, sp))
playlist_id = spotify.create_playlist(sp = sp)
spotify.add_to_playlist(song_ids, playlist_id, sp)