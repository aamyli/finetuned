import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Get cid and secret by logging in here https://developer.spotify.com/dashboard/

cid = '0edff00b50fc4425b0fe694c47b0a097'
secret='481ff02a69744a81855cacf95fc576a9'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def find_song(title, artist):
    query = "artist:"+artist + " track:" + title

    track_results = sp.search(q=query, type='track')

    t = track_results['tracks']['items'][0]

    artist_name = t['artists'][0]['name']
    track_name = t['name']
    popularity = t['popularity']
    track_id = t['id']

    print(artist_name)
    print(track_name)
    print(popularity)
    print(track_id)

    #track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'popularity' : popularity})
    #print(track_dataframe.shape)
    #track_dataframe.head()
    #print(track_dataframe)

    song_data = sp.audio_features(tracks=[track_id])
    print('------------------------------------------------')
    print(song_data)

    song_extract = [] 

    for item in song_data:
       song_extract = [item['danceability'], item['tempo'], item['energy'], item['valence'], item['mode']]

    print(song_extract)
    return song_extract

if __name__ == "__main__":
    find_song("Times Like These", "EDEN")