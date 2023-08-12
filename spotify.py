import random
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from flask import Flask, render_template, request, redirect, url_for
# Diğer importları burada ekleyin

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/created_playlist")
def playlist():
    return render_template("playlist.html")

@app.route("/playlist", methods=["GET"])
def playlist():
    sp_oauth = SpotifyOAuth(
        client_id, client_secret, SPOTIPY_REDIRECT_URI, scope=SPOTIPY_SCOPE
    )
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    
    user = sp.current_user()
    playlists = sp.current_user_playlists()
    
    # Eğer kullanıcının playlistleri arasında hedeflediğiniz playlist varsa, onun detaylarını alabilirsiniz
    target_playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == "En Çok Dinlenen Sanatçıların Karışık Şarkıları":
            target_playlist_id = playlist['id']
            break
    
    # Eğer hedeflenen playlist bulunduysa, playlist detaylarını ve içindeki şarkıları al
    target_playlist = None
    playlist_tracks = []
    if target_playlist_id:
        target_playlist = sp.playlist(target_playlist_id)
        playlist_tracks = target_playlist['tracks']['items']
    
    return render_template("playlist.html", playlist=target_playlist, tracks=playlist_tracks)



if __name__ == "__main__":
    app.run(debug=True)
