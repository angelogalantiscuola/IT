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
from sqlmodel import SQLModel, Field, Relationship, select
from sqlmodel import Session, create_engine
from typing import List
import json


class PlaylistSong(SQLModel, table=True):
    playlist_id: Optional[int] = Field(foreign_key="playlist.id", primary_key=True)
    song_id: Optional[int] = Field(foreign_key="song.id", primary_key=True)


class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    duration: int
    # album_id: int = Field(foreign_key="album.id")
    album_id: Optional[int] = Field(foreign_key="album.id")
    album: "Album" = Relationship(back_populates="songs")
    playlists: List["Playlist"] = Relationship(back_populates="songs", link_model=PlaylistSong)


class Playlist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    user_id: Optional[int] = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="playlists")
    songs: List["Song"] = Relationship(back_populates="playlists", link_model=PlaylistSong)


class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    albums: List["Album"] = Relationship(back_populates="artist")


class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")
    artist: Optional[Artist] = Relationship(back_populates="albums")
    songs: List["Song"] = Relationship(back_populates="album")


class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str
    price: float
    users: List["User"] = Relationship(back_populates="subscription")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    subscription_id: Optional[int] = Field(foreign_key="subscription.id")
    subscription: Subscription = Relationship(back_populates="users")
    playlists: List["Playlist"] = Relationship(back_populates="user")


def create_objects(engine):
    with Session(engine) as session:
        # Create an Artist
        pink_floyd = Artist(name="Pink Floyd")
        session.add(pink_floyd)
        session.commit()

        # Create a Subscription
        premium = Subscription(type="Premium", price=9.99)
        session.add(premium)
        session.commit()

        # Create an Album
        the_wall = Album(title="The Wall", artist_id=pink_floyd.id)
        session.add(the_wall)
        session.commit()

        # Create a Song
        comfortably_numb = Song(title="Comfortably Numb", duration=210, album_id=the_wall.id)
        session.add(comfortably_numb)
        session.commit()

        # Create a User
        john = User(username="John", email="john@example.com", subscription_id=premium.id)
        session.add(john)
        session.commit()

        # Create a Playlist
        johns_playlist = Playlist(name="John's Playlist", user_id=john.id)
        session.add(johns_playlist)
        session.commit()

        # Add the song to the playlist
        playlist_song = PlaylistSong(playlist_id=johns_playlist.id, song_id=comfortably_numb.id)
        session.add(playlist_song)
        session.commit()


def create_objects_from_json(engine, folder):
    with Session(engine) as session:
        with open(f"{folder}albums.json") as f:
            albums_data = json.load(f)
        with open(f"{folder}artists.json") as f:
            artists_data = json.load(f)
        with open(f"{folder}playlists.json") as f:
            playlists_data = json.load(f)
        with open(f"{folder}songs.json") as f:
            songs_data = json.load(f)
        with open(f"{folder}subscriptions.json") as f:
            subscriptions_data = json.load(f)
        with open(f"{folder}users.json") as f:
            users_data = json.load(f)

        for subscription_data in subscriptions_data:
            subscription = Subscription(**subscription_data)
            session.add(subscription)
        session.commit()

        for song_data in songs_data:
            song = Song(**song_data)
            session.add(song)
        session.commit()

        for artist_data in artists_data:
            subscription = Artist(**artist_data)
            session.add(subscription)
        session.commit()

        for user_data in albums_data:
            # to create an album the artist id is needed
            # get the artist id from the artist name in the album_data
            artist_name = user_data["artist"]
            subscription = session.exec(select(Artist).where(Artist.name == artist_name)).first()
            if subscription:
                user_data["artist_id"] = subscription.id
            else:
                print(f"Artist {artist_name} not found")
                continue
            album = Album(title=user_data["title"], artist_id=user_data["artist_id"])
            session.add(album)
        session.commit()

        for user_data in users_data:
            # to create an user the subscription id is needed
            subscription_type = user_data["subscription_type"]
            subscription = session.exec(select(Subscription).where(Subscription.type == subscription_type)).first()
            if subscription:
                user_data["subscription_id"] = subscription.id
            else:
                print(f"Subscription {subscription_type} not found")
                continue
            user = User(
                username=user_data["username"], email=user_data["email"], subscription_id=user_data["subscription_id"]
            )
            session.add(user)
        session.commit()

    for playlist_data in playlists_data:
        # to create a playlist, the user id and song ids are needed
        username = playlist_data["username"]
        user = session.exec(select(User).where(User.username == username)).first()
        if user:
            playlist_data["user_id"] = user.id
        else:
            print(f"User {username} not found")
            continue

        song_titles = playlist_data["song_titles"]
        songs = []
        for title in song_titles:
            song = session.exec(select(Song).where(Song.title == title)).first()
            if song:
                songs.append(song)
            else:
                print(f"Song with title {title} not found")

        if len(songs) == len(song_titles):
            playlist_data["song_ids"] = [song.id for song in songs]
        else:
            print(f"Not all songs found for playlist {playlist_data['name']}")
            continue

        playlist = Playlist(user_id=playlist_data["user_id"], name=playlist_data["name"])
        session.add(playlist)
        session.commit()

        for song_id in playlist_data["song_ids"]:
            playlist_song = PlaylistSong(playlist_id=playlist.id, song_id=song_id)
            session.add(playlist_song)
        session.commit()


def select_objects(engine, table):
    with Session(engine) as session:
        statement = select(table)
        results = session.exec(statement)
        for data in results:
            print(data)
        print()


if __name__ == "__main__":
    folder = "temp/streaming_service/"
    sqlite_file_name = f"{folder}/database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url)
    # engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    # create_objects(engine)
    create_objects_from_json(engine, folder)

    list_of_classes = [
        Song,
        Playlist,
        Artist,
        Album,
        Subscription,
        User,
        PlaylistSong,
    ]

    for el in list_of_classes:
        select_objects(engine, el)
