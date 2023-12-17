"""
This is a simple streaming service example.
It contains the following classes:
- Song
- Album
- PremiumAlbum
- Playlist
- Subscription
- User
- Artist

It also contains a function that creates the objects and returns them.
"""


from typing import Optional
import json


class Song:
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.title} ({self.duration} seconds)"


class Album:
    def __init__(self, title: str):
        self.title = title
        self.songs: list[Song] = []

    def add_song(self, title: str, duration: int) -> Song:
        song = Song(title, duration)
        self.songs.append(song)
        return song

    def __str__(self):
        return f"Album: {self.title}, Songs: {[str(song) for song in self.songs]}"


class PremiumAlbum(Album):
    def __init__(self, title: str, exclusive_content: str):
        super().__init__(title)
        self.exclusive_content = exclusive_content

    def add_exclusive_content(self, content: str):
        self.exclusive_content = content

    def __str__(self):
        return f"Premium Album: {self.title}, Exclusive Content: {self.exclusive_content}, Songs: {[str(song) for song in self.songs]}"


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs: list[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {[str(song) for song in self.songs]}"


class Subscription:
    def __init__(self, type: str, price: float):
        self.type = type
        self.price = price

    def __str__(self):
        return f"Subscription: {self.type}, Price: {self.price}"


class User:
    def __init__(self, username: str, email: str, subscription: Subscription):
        self.username = username
        self.email = email
        self.playlists: list[Playlist] = []
        self.subscription = subscription

    def create_playlist(self, name: str) -> Playlist:
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Subscription: {str(self.subscription)}, Playlists: {[str(playlist) for playlist in self.playlists]}"


class Artist:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def create_album(self, title: str) -> Album:
        album = Album(title)
        self.albums.append(album)
        return album

    def create_premium_album(self, title: str, exclusive_content: str) -> PremiumAlbum:
        premium_album = PremiumAlbum(title, exclusive_content)
        self.albums.append(premium_album)
        return premium_album

    def __str__(self):
        return f"Artist: {self.name}, Albums: {[str(album) for album in self.albums]}"


class StreamingService:
    def __init__(self):
        self.users: list[User] = []
        self.artists: list[Artist] = []

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        self.users.remove(user)

    def find_user(self, username: str) -> Optional[User]:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def add_artist(self, artist: Artist):
        self.artists.append(artist)

    def remove_artist(self, artist: Artist):
        self.artists.remove(artist)

    def find_artist(self, name: str) -> Optional[Artist]:
        for artist in self.artists:
            if artist.name == name:
                return artist
        return None


def create_objects_from_json(file_path: str) -> StreamingService:
    with open(file_path, "r") as f:
        data = json.load(f)

    streaming_service = StreamingService()

    for user_data in data["users"]:
        subscription = Subscription(user_data["subscription"]["type"], user_data["subscription"]["price"])
        user = User(user_data["name"], user_data["email"], subscription)
        streaming_service.add_user(user)

        for playlist_data in user_data["playlists"]:
            playlist = user.create_playlist(playlist_data["name"])
            for song_data in playlist_data["songs"]:
                song = Song(song_data["title"], song_data["duration"])
                playlist.add_song(song)

    for artist_data in data["artists"]:
        artist = Artist(artist_data["name"])
        streaming_service.add_artist(artist)

        for album_data in artist_data["albums"]:
            if album_data["type"] == "premium":
                album = artist.create_premium_album(album_data["title"], album_data["exclusive_content"])
            else:
                album = artist.create_album(album_data["title"])

            for song_data in album_data["songs"]:
                song = Song(song_data["title"], song_data["duration"])
                album.songs.append(song)

    return streaming_service


def print_objects(StreamingService) -> None:
    list_of_users = StreamingService.users
    list_of_artists = StreamingService.artists

    print("Users:")
    for user in list_of_users:
        print(user.email, user.username, user.subscription.type, user.subscription.price)

        for playlist in user.playlists:
            print(f"{playlist.name}:", end=" ")
            for song in playlist.songs:
                print(song.title, song.duration, end=", ")
            print()
        print()

    print("Artists:")
    for artist in list_of_artists:
        print(f"{artist.name}")
        for album in artist.albums:
            print(f"{album.title}:", end=" ")
            for song in album.songs:
                print(song.title, song.duration, end=", ")
            print()
        print()


if __name__ == "__main__":
    streaming_service = create_objects_from_json("data.json")
    print_objects(streaming_service)

    print(streaming_service.find_user("John") or "User not found")
    print(streaming_service.find_user("James") or "User not found")

    print(streaming_service.find_artist("Pink Floyd") or "User not found")
    print(streaming_service.find_artist("Beatles") or "User not found")
