import os
from googleapiclient.discovery import build


def get_video(video_id):
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_info = youtube.videos().list(part="snippet,statistics", id=video_id).execute()
    return video_info


def get_playlist(playlist_id):
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    playlist_info = youtube.playlists().list(part='contentDetails, snippet', id=playlist_id).execute()
    return playlist_info


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_info = get_video(video_id)
        try:
            self.title = self.video_info['items'][0]['snippet']['title']
            self.view_count = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']
            self.video_url = "https://www.youtube.com/watch?=" + self.video_id + '&ab_channel=MoscowPython'
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.video_url = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_info = get_playlist(playlist_id)
