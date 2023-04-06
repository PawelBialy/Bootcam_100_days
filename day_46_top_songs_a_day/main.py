from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
spotify_client_id = "6d6c53940e8e4cca99cd23cd4fcfd4d0"
spotify_client_secret  = "b11e017bd34249cf879d615538aaa2ea"
# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)














####################################################################

# import requests
# import spotipy
# from bs4 import BeautifulSoup
# from spotipy.oauth2 import SpotifyOAuth
#
#
# date = input("What year do you want travel to? Type the date in this formar YYYY-MM-DD: ")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# pl_web = response.text
#
# soup = BeautifulSoup( pl_web, "html.parser")
# top100 = []
# titles = []
# # check site in edge or chrome dev tools to see fields
# titles = soup.find_all(name="h3", class_="a-no-trucate")
# top100 = [title.getText().strip() for title in titles]
# print(top100)
#
#
# spotify_client_id = "6d6c53940e8e4cca99cd23cd4fcfd4d0"
#
# spotify_client_secret  = "b11e017bd34249cf879d615538aaa2ea"
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=spotify_client_id,
#         client_secret=spotify_client_secret,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
#
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# song_names = ["The list of song", "titles from your", "web scrape"]
#
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
#  # Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#
# # Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)