import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def retrieve_youtube_playlist():
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
        request = youtube.videos().list(part="snippet", myRating="like")
        playlist = []
        while(request):
                response = request.execute()
                for item in response['items']:
                        playlist.append(item['snippet']['title'])
                request = youtube.videos().list_next(request, response)
        return playlist
    