# Streaming Service

1. We have a `User` who can subscribe to a service. The `User` has a `username`, `email`, and can also create multiple `Playlists`.

2. There's an `Artist` who can create multiple `Albums`. The `Artist` has a `name`.

3. Each `Album` can contain multiple `Songs` and belongs to an `Artist`. The `Album` has a `title`. There's also a special type of `Album`, called `PremiumAlbum`, that contains `exclusiveContent`.

4. Each `Song` belongs to an `Album` and can be included in multiple `Playlists`. The `Song` has a `title` and `duration`.

5. A `Playlist` belongs to a `User` and can contain multiple `Songs`. The `Playlist` has a `name`.

6. A `Subscription` is associated with a `User`. The `Subscription` has a `type` and `price`.

Remember to use the correct PlantUML syntax for defining classes, attributes, relationships, and inheritance.
