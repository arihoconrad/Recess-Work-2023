# Extract the bird species from Xeno-canto website
import requests
from bs4 import BeautifulSoup
import json

# Scrapping function
def extract_bird_species(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        species_list = []
        bird_table = soup.find('table', class_ = "results")

        if bird_table:
            rows = bird_table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                for column in columns:
                    bird_link = column.find('a')
                    if bird_link:
                        species = bird_link.text.strip()
                        species_list.append(species)
        return species_list
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return []
    
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

    # Bird Species
    url = "http://xeno-canto.org/collection/species/all"
    bird_species = extract_bird_species(url)

    # Creating a dictionary of for better organisation
    data = {"Bird Species" : bird_species}
    # Write into JSON file
    with open("bird_species.json", "w") as json_file:
        json.dump(data, json_file)
    print("Data has been successsfully saved to bird_species.json")

# Bird songs 
api_url = "http://xeno-canto.org/api/2/recordings?query=type:song"
bird_songs = extract_bird_songs(api_url)

# Creating a dictionary of for better organisation
song_data = {"Bird Song" : bird_songs}
# Write into JSON file
with open("bird_songs.json", "w") as json_file2:
    json.dump(song_data, json_file2)
print("Data has been successesfully saved to bird_songs.json")