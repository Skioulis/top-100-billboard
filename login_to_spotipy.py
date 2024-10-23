import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def logintospotipy (clientid, clientsecret):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=clientid,
        client_secret=clientsecret,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        # show_dialog=True,
        # cache_path="token.txt",
        # username="Fotis Fotiadis",
    )
    )

    return sp