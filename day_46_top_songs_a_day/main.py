import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


date = input("What year do you want travel to? Type the date in this formar YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
pl_web = response.text

soup = BeautifulSoup( pl_web, "html.parser")
top100 = []
titles = []
# check site in edge or chrome dev tools to see fields
titles = soup.find_all(name="h3", class_="a-no-trucate")
top100 = [title.getText().strip() for title in titles]
print(top100)


spotify_client_id = "6d6c53940e8e4cca99cd23cd4fcfd4d0"

spotify_client_secret  = "b11e017bd34249cf879d615538aaa2ea"
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