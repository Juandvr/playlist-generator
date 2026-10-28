from ytmusicapi import YTMusic
from playlist_generator.csv_manager import read_csv

ytmusic = YTMusic('browser.json')

def create_playlist():
    playlistId = ytmusic.create_playlist('Awesome mix #2', 'test description')
    songs = read_csv()

    for song in songs:
        search_results = ytmusic.search(f'{song['title']} {song['artist']}')
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']]) # type: ignore

create_playlist()