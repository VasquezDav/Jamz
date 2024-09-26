import spotipy
from spotipy.oauth2 import SpotifyOAuth
import environ

# Initialize environment variable loading
env = environ.Env()
environ.Env.read_env()  # This reads the .env file
print("here")
# Retrieve your credentials from environment variables
SPOTIPY_CLIENT_ID = env('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = env('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URL = env('SPOTIPY_REDIRECT_URL')

print("Client ID:", SPOTIPY_CLIENT_ID)
print("Client Secret:", SPOTIPY_CLIENT_SECRET)

# Set up Spotify API
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URL,
                                               scope=scope))

# Now you can fetch the current user's saved tracks
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
