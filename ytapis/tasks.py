from __future__ import absolute_import, unicode_literals
from celery import shared_task
# from .serializers import VideoSerializer
from .models import Video
import requests
import json
from assignment import settings

from datetime import datetime, timedelta

@shared_task
def add(x, y):
    return x + y

@shared_task
def call_api():
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=5)
    apiKeys = settings.YT_API_KEYS
    URL = "https://youtube.googleapis.com/youtube/v3/search"
    PARAMS = {
        'q': 'news',
        'maxResults': 10,
        'key': apiKeys,
        'order': 'date',
        'type': 'video',
        'part': 'snippet',
        'publishedAfter': last_request_time.replace(microsecond=0).isoformat()+'Z',
    }
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    json_data = json.loads(r.text)
    for item in reversed(json_data['items']):
        title = item['snippet']['title'],
        description = item['snippet']['description'],
        published = item['snippet']['publishedAt'],
        thumbnail = item['snippet']['thumbnails']['default']['url']

        # print(title, description, published, thumbnail)

        video = Video(
            title=title[0],
            description=description[0],
            published=published[0],
            thumbnail=thumbnail,
        )
        video.save()
        
    #print(json_data)

@shared_task
def test():
    print('Hello World')