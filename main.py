import youtube
import spotify
import time
import json

# Retrieve the youtube liked videos
songs_on_youtube = youtube.retrieve_youtube_playlist()

# Authorize spotify 
with open("spotify_client_secret.json", "r") as file:
    spotify_secrets = json.load(file)
    spotify_client_id = spotify_secrets['client_id']
    spotify_client_secret = spotify_secrets['client_secret']
    file.close()
sp = spotify.authorize_spotify(spotify_client_id, spotify_client_secret)

# Retrieve song ids for each liked video by searching with the video's name.
# This is not an exact match as the video names sometimes differ but it is close enough
# After every 100 retrievals wait for 5 secs as the API gets overloaded
song_ids = []
counter = 1
for song in songs_on_youtube:
    if counter % 100 == 0:
        print("Waiting for 5 secs")
        time.sleep(5)
    print(f'Retrieving ID {counter} for {song}')
    song_ids.append(spotify.track_name_to_id(song, sp))
    counter += 1

# Create a new spotify playlist with the name entered by the user
name = input("Enter the name of the playlist you want to create in spotify - ")
playlist_id = spotify.create_playlist(name, sp = sp)

# Create batches of 100 and using a loop and then create one additional batch for the remainder
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

# Add each batch of song IDs to the playlist
for batch in song_batches:
    spotify.add_to_playlist(batch, playlist_id, sp)