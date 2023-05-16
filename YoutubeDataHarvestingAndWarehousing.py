#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from googleapiclient.discovery import build
from pymongo import MongoClient

import pandas as pd


# In[ ]:


api_key = 'AIzaSyA79XBlkzuMdQsoA74g4TmjdQwnTRmWdxA'
channel_ids = ['UCnz-ZXXER4jOvuED5trXfEA', # techTFQ
               'UCLLw7jmFsvfIVaUFsLs8mlQ', # Luke Barousse 
               'UCiT9RITQ9PW6BhXK0y2jaeg', # Ken Jee
               'UC7cs8q-gJRlGwj4A8OmCmXg', # Alex the analyst
               'UC2UXDak6o7rBm23k3Vv5dww' # Tina Huang
              ]

youtube = build('youtube', 'v3', developerKey=api_key)


# ## statistics##

# In[ ]:


def get_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return all_data


# In[ ]:


channel_statistics = get_channel_stats(youtube, channel_ids)


# In[ ]:


channel_data = pd.DataFrame(channel_statistics)


# In[ ]:


channel_data


# In[ ]:


playlist_id = channel_data.loc[channel_data['Channel_name']=='Ken Jee', 'playlist_id'].iloc[0]


# In[ ]:


def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids


# In[ ]:


video_ids = get_video_ids(youtube, playlist_id)


# In[ ]:


video_ids


# In[ ]:





# In[ ]:


def get_video_details(youtube, video_ids):
    all_video_stats = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                    part='snippet,statistics',
                    id=','.join(video_ids[i:i+50]))
        response = request.execute()
        
        for video in response['items']:
            video_stats = dict(Title = video['snippet']['title'],
                               Published_date = video['snippet']['publishedAt'],
                               Views = video['statistics']['viewCount'],
                               Likes = video['statistics']['likeCount'],
                               Dislikes = video['statistics']['dislikeCount'],
                               Comments = video['statistics']['commentCount']
                               )
            all_video_stats.append(video_stats)
    
    return all_video_stats


# In[ ]:


video_details = get_video_details(youtube, video_ids)


# In[ ]:


video_data = pd.DataFrame(video_details)


# In[ ]:





# In[ ]:


client = MongoClient('mongodb://localhost:27017/')


# In[ ]:


db = client['YT_data']
collection = db['ytanalysis']


# In[ ]:


# Multiple document insertion
data_list = video_ids
result = collection.insert_many(data_list)
print(f"Inserted document IDs: {result.inserted_ids}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




