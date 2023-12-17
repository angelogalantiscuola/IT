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


def create_objects() -> tuple[list[User], list[Artist]]:
    # Create a subscription
    subscription_base = Subscription("base", 9.99)
    Subscription_premium = Subscription("premium", 19.99)

    # Create a user with the subscription
    john = User("John", "john@example.com", subscription_base)
    jane = User("Jane", "jane@example.com", Subscription_premium)

    pink_floyd = Artist("Pink Floyd")
    pink_floyd.create_premium_album("The Dark Side of the Moon", "Secret message")
    pink_floyd.albums[0].songs = [
        Song("Speak to Me", 90),
        Song("Breathe", 163),
        Song("On the Run", 216),
    ]

    rolling_stones = Artist("The Rolling Stones")
    rolling_stones.create_album("Sticky Fingers")
    rolling_stones.albums[0].songs = [
        Song("Brown Sugar", 132),
        Song("Sway", 154),
        Song("Wild Horses", 215),
    ]

    john_playlist = john.create_playlist("Rock")
    john_playlist.add_song(pink_floyd.albums[0].songs[0])
    john_playlist.add_song(rolling_stones.albums[0].songs[1])

    list_of_users = [john, jane]
    list_of_artists = [pink_floyd, rolling_stones]

    return list_of_users, list_of_artists


def print_objects(list_of_users: list[User], list_of_artists: list[Artist]) -> None:
    for user in list_of_users:
        print(user.email, user.username, user.subscription.type, user.subscription.price)

        for playlist in user.playlists:
            print(f"{playlist.name}:", end=" ")
            for song in playlist.songs:
                print(song.title, song.duration, end=", ")
            print()
        print()

    for artist in list_of_artists:
        print(f"{artist.name}")
        for album in artist.albums:
            print(f"{album.title}:", end=" ")
            for song in album.songs:
                print(song.title, song.duration, end=", ")
            print()
        print()


if __name__ == "__main__":
    list_of_users, list_of_artists = create_objects()
    print_objects(list_of_users, list_of_artists)
