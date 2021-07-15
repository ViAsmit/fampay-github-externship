import requests
from videos.models import Video
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyArjgKkD-MGCCZY-WAUTdb4DuWU-9c_zbA'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q="pubg",
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    print(search_response)
    # for search_result in search_response.get('items', []):
    #     print(search_result)
    #     if search_result['id']['kind'] == 'youtube#video':
    #         videos.append('%s (%s)' % (search_result['snippet']['title'],
    #                                    search_result['id']['videoId']))

    # print('Videos:\n', '\n'.join(videos), '\n')


def update_forecast():
    try:
        youtube_search()
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    print("yipeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    # json = _get_forecast_json()
    # if json is not None:
    #     try:
    #         new_forecast = Video()

    #         # open weather map gives temps in Kelvin. We want celsius.
    #         temp_in_celsius = json['main']['temp'] - 273.15
    #         new_forecast.temperatue = temp_in_celsius
    #         new_forecast.description = json['weather'][0]['description']
    #         new_forecast.city = json['name']
    #         new_forecast.save()
    #         print("saving...\n" + new_forecast)
    #     except:
    #         pass
