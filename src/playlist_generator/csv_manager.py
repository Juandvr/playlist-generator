from pathlib import Path
from mutagen import File
from mutagen.mp3 import EasyMP3
import csv

def create_csv(songs):
    for song in songs:
        song_data = File(song)

        with open('songs.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(['title', 'artist'])

            try:
                title = ''.join(song_data['title']) # type: ignore
                artist = ''.join(song_data['artist']) # type: ignore
                writer.writerow([title, artist])
            except KeyError:
                song_data = EasyMP3(song)
                title = ''.join(song_data['title'])
                artist = ''.join(song_data['artist'])
                writer.writerow([title, artist])

def read_csv():
    songs_csv = Path('./songs.csv')
    songs_list = []

    with songs_csv.open(mode='r', encoding='utf-8', newline='') as file:
        songs_list = list(csv.DictReader(file))

    return songs_list