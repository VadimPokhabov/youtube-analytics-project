import json
import os
from googleapiclient.discovery import build


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Channel:

    """Класс для ютуб-канала"""

    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):

        """Выводит в консоль информацию о канале."""

        printj(self.channel)
