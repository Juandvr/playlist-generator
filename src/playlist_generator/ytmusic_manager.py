from ytmusicapi import YTMusic, OAuthCredentials
from playlist_generator.csv_manager import read_csv
from keys import CLIENT_ID, CLIENT_SECRET

client_id = CLIENT_ID
client_secret = CLIENT_SECRET

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id, client_secret))

def create_playlist():
    playlistId = ytmusic.create_playlist('test', 'test description')
    songs = read_csv()

    for song in songs:
        search_results = ytmusic.search(f'{song['title']} {song['artist']}')
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']]) # type: ignore

create_playlist()