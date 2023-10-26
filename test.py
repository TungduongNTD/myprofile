import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Điền thông tin ứng dụng Spotify Developer của bạn ở đây
client_id = '13e8f6d549974b208fbda4326be2b0e0'
client_secret = '13e8f6d549974b208fbda4326be2b0e0'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Tìm kiếm bài hát
query = input("Nhập tên bài hát hoặc nghệ sĩ: ")
results = sp.search(q=query, type='track')

for track in results['tracks']['items']:
    print(f"Tên bài hát: {track['name']}")
    print(f"Nghệ sĩ: {track['artists'][0]['name']}")
    print(f"Đường dẫn Spotify: {track['external_urls']['spotify']}")
    print()
