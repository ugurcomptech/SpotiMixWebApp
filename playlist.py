from flask import Flask, render_template, request, redirect, url_for, flash
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import random
import argparse
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'
SPOTIPY_SCOPE = 'user-library-read user-top-read playlist-modify-public'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    if request.method == "POST":
        client_id = request.form['client_id']
        client_secret = request.form['client_secret']

        if not client_id or not client_secret:
            flash('Lütfen tüm alanları doldurun.', 'warning')
            return redirect(url_for('index'))

        sp_oauth = SpotifyOAuth(
            client_id, client_secret, SPOTIPY_REDIRECT_URI, scope=SPOTIPY_SCOPE
        )

        sp = spotipy.Spotify(auth_manager=sp_oauth)

        # Kullanıcının en çok dinlediği 10 sanatçıları al
        top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')

        # Tüm sanatçıların popüler şarkılarını toplayacak liste
        all_artist_tracks = []

        # Sanatçıların popüler şarkılarını al
        for artist in top_artists['items']:
            artist_id = artist['id']
            artist_tracks = sp.artist_top_tracks(artist_id, country='TR')
            all_artist_tracks.extend(artist_tracks['tracks'])

        # Rastgele karışık bir şekilde şarkıları seçin
        random.shuffle(all_artist_tracks)
        selected_tracks = all_artist_tracks[:100]

        # Kullanıcının playlistini oluştur
        playlist_name = "En Çok Dinlenen Sanatçıların Karışık Şarkıları"
        playlist_description = "En çok dinlenen 10 sanatçının rastgele karışık şarkıları"

        playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=True, description=playlist_description)
        playlist_id = playlist['id']

        # Şarkıları playliste ekle
        track_uris = [track['uri'] for track in selected_tracks]
        sp.playlist_add_items(playlist_id, track_uris)

         # Playlist oluşturulduktan sonra index.html sayfasına yönlendir
        return redirect(url_for('playlist', playlist_id=playlist_id))
    
@app.route("/playlist/<playlist_id>")
def playlist(playlist_id):
    return render_template("playlist.html", playlist_id=playlist_id)


@app.route('/developer')
def developer():
    return render_template('developer.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,debug=True)
