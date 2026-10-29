from playlist_generator.csv_manager import create_csv
from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.post('/upload') # type: ignore
def upload():
    songs = request.files.getlist('files')
    create_csv(songs)
    return 'uploaded'
    
if __name__ == '__main__':
    app.run()