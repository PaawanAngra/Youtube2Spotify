import youtube
import spotify
import time

songs_on_youtube = youtube.retrieve_youtube_playlist()

sp = spotify.authorize_spotify()
song_ids = []
counter = 1
for song in songs_on_youtube:
    if counter % 100 == 0:
        print("Waiting for 5 secs")
        time.sleep(5)
    print(f'Retrieving ID {counter} for {song}')
    song_ids.append(spotify.track_name_to_id(song, sp))
    counter += 1
playlist_id = spotify.create_playlist(sp = sp)
n = len(song_ids)
rem = n % 100
hundreds = int(n / 100)
start = 0
end = 100
song_batches = []
for i in range(hundreds):
    song_batches.append(song_ids[start : end])
    start = end
    end = end + 100
start = hundreds * 100
end = hundreds * 100 + rem
song_batches.append(song_ids[start : end])
for batch in song_batches:
    spotify.add_to_playlist(batch, playlist_id, sp)