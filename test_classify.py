from playlist_logic import build_playlists, normalize_song, DEFAULT_PROFILE

# Test songs with chill genres
test_songs = [
    {
        "title": "Lo-fi Rain",
        "artist": "DJ Calm",
        "genre": "lofi",
        "energy": 2,
        "tags": ["study"],
    },
    {
        "title": "Soft Piano",
        "artist": "Sleep Sound",
        "genre": "ambient",
        "energy": 1,
        "tags": ["sleep"],
    },
    {
        "title": "Weightless",
        "artist": "Marconi Union",
        "genre": "ambient",
        "energy": 1,
        "tags": ["relax", "sleep"],
    },
    {
        "title": "Zen Garden",
        "artist": "Meditation Monks",
        "genre": "ambient",
        "energy": 1,
        "tags": ["meditative", "peaceful"],
    },
]

# Classify songs
playlists = build_playlists(test_songs, DEFAULT_PROFILE)

print("HYPE PLAYLIST:")
for song in playlists["Hype"]:
    print(f"  - {song['title']} ({song['genre']}, energy: {song['energy']})")

print("\nCHILL PLAYLIST:")
for song in playlists["Chill"]:
    print(f"  - {song['title']} ({song['genre']}, energy: {song['energy']})")

print("\nMIXED PLAYLIST:")
for song in playlists["Mixed"]:
    print(f"  - {song['title']} ({song['genre']}, energy: {song['energy']})")
