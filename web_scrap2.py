import requests
from bs4 import BeautifulSoup
import json

def extract_bird_songs(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        song_list = []

        if 'recordings' in data:
            for recording in data['recordings']:
                song_list.append(recording['en'])
        return song_list
    else:
        print(f"Failed to fetch data from {api_url}. Status code: {response.status_code}")
        return[]
    
if __name__ == '__main__':
    ###### Bird