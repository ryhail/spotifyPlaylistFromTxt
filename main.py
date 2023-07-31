import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="CLIENT_ID",
                                               client_secret="CLIENT_SECRET",
                                               redirect_uri="REDIR_URI",
                                               scope="playlist-modify-private"))

if __name__ == "__main__":
    with open('music.txt', 'r', encoding='UTF-8') as f:
        music = [line.rstrip('\n') for line in f]
    f.close()
    user = sp.current_user()
    print("Hello", user['display_name'])
    playlist = sp.user_playlist_create(user['id'], "YourNewPlaylist", False, False, "")
    print(playlist['name'], "created successfully!")
    uri_list = []
    for song in music:
        print(song)
        SearchResult = sp.search(song, 1, 0, "track")['tracks']['items'][0]
        uri_list.append(SearchResult['uri'])
        sp.playlist_add_items(playlist['id'], uri_list, 0)
        uri_list.clear()
    print("Ended successfully")


