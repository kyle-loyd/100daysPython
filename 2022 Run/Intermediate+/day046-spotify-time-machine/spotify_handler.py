from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

spotify_client: Spotify
user_id: str
playlist_id: str

def setup():
    global spotify_client, user_id
    spotify_client = Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id="1e4a17432fea489a8d29152b0332bbee",
            client_secret="REDACTED",
            show_dialog=True,
            cache_path="token.txt"))
    user_id = spotify_client.current_user()["id"]


def create_playlist(date):
    global playlist_id
    playlist = spotify_client.user_playlist_create(
        user=user_id,
        name=f"Time Travel: {date}",
        public=False,
        description="Another time-travel playlist!")
    playlist_id = playlist["id"]


def add_tracks_to_playlist(track_list, year):
    tracks = [spotify_client.search(q=f"track:{track} year:{year}", type="track") for track in track_list]
    track_uris = []
    for track in tracks:
        try:
            track_uris.append(track["tracks"]["items"][0]["uri"])
        except IndexError:
            print("Couldn't find track.  Skipping..")
    spotify_client.playlist_add_items(playlist_id=playlist_id, items=track_uris)
