from pathlib import Path
from mutagen import File
from mutagen.mp3 import EasyMP3
import csv

music_folder = Path('/home/juandvr/Music')
songs = list(music_folder.rglob('*.flac')) + list(music_folder.rglob('*.mp3'))

def create_csv():
    for song in songs:
        song_data = File(song)

        with open('songs.csv', 'w', newline='', encoding='utf-8') as file:
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