# Social Media Platform

1. We have a `User` who can create `Posts`, `Comments`, and `Messages`. The `User` has a `username`, `email`, `password`, and `profilePicture`. The `User` can also `follow()` other users, `like()` posts and comments, `share()` posts, and `sendMessage()` to other users.

2. A `Post` is created by a `User` and can contain multiple `Comments` and `Likes`. The `Post` has a `content`, `timestamp`, and `location`. The `Post` can also `addComment()`, `removeComment()`, `like()`, and `share()`.

3. Each `Comment` is associated with a `Post` and created by a `User`. The `Comment` has `content` and `timestamp`. The `Comment` can also `like()` and `reply()`.

4. A `Like` is associated with a `Post` or `Comment` and created by a `User`. The `Like` has a `timestamp`.

5. A `Message` is sent between two `Users`. The `Message` has `content` and `timestamp`.

6. A `Group` can contain multiple `Users` and `Posts`. The `Group` has a `name` and `description`. The `Group` can `addUser()`, `removeUser()`, `addPost()`, and `removePost()`.

7. A `Page` is similar to a `Group`, but it's managed by a `User` and can contain `Advertisements`. The `Page` has a `name`, `description`, and `category`. The `Page` can `addAdvertisement()`, `removeAdvertisement()`, `addPost()`, and `removePost()`.

8. An `Advertisement` is associated with a `Page` and created by a `User`. The `Advertisement` has `content`, `timestamp`, and `budget`. The `Advertisement` can `start()`, `stop()`, and `adjustBudget()`.

9. A `Notification` is associated with a `User`. The `Notification` has `content` and `timestamp`. The `Notification` can `markAsRead()`.

10. A `Report` is associated with a `Post`, `Comment`, `Message`, or `Advertisement` and created by a `User`. The `Report` has `reason` and `timestamp`. The `Report` can `submit()`.

Remember to use the correct PlantUML syntax for defining classes, attributes, relationships, and methods.