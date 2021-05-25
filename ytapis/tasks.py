from __future__ import absolute_import, unicode_literals
from celery import shared_task
# from .serializers import VideoSerializer
from .models import Video
import requests
import json

@shared_task
def add(x, y):
    return x + y

@shared_task
def call_api():
    URL = "https://youtube.googleapis.com/youtube/v3/search"
    PARAMS = {
        'q': 'football',
        'maxResults': 1,
        'key': 'AIzaSyDdj2MdQo-VVaiVH7cYXWD5E5o9_LOCuHs',
        'order': 'date',
        'type': 'video',
        'part': 'snippet'
    }
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    json_data = json.loads(r.text)
    for item in json_data['items']:
        video = Video(
            title = item['snippet']['title'],
            description = item['snippet']['description'],
            published = item['snippet']['publishedAt'],
            thumbnail = item['snippet']['thumbnails']['default']['url']
        )
        video.save()
        
    print(json_data)

@shared_task
def test():
    print('Hello World')