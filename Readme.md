26 Jun 2024

Hi! So, I had a habit of listening to songs on youtube since my early days and I would like videos that I liked. My whole playlist was in the youtube liked videos and I would only like songs and no other videos. I also had a few playlists in spotify and one day I decided to consolidate my music library at one place. Ofcourse spotify was a better option out of these two. Now I didn't want to manually like each song from the youtube playlist in a spotify playlist. So I created this little app that trasnfers your liked videos into a spotify playlist.

We've accessed the youtube API, spotify API and used the spotipy library.

Notes to setup this app - 

1. Clone the repo on your machine.
2. Get credentials for youtube data API using OAuth 2.0, refer to this guide https://wpythub.com/documentation/getting-started/set-youtube-oauth-client-id-client-secret/
3. Download the credentials file and rename it to google_client_secret.json
4. Get credentials for spotify API, refer to this guide https://developer.spotify.com/documentation/web-api/concepts/apps
5. Store the spotify credentials in a file titled spotify_client_secret.json in the root folder in the following way -
   {
    "client_id" : "your_client_id",
    "client_secret" : "your_client_secret"
  }
6. Run main.py
