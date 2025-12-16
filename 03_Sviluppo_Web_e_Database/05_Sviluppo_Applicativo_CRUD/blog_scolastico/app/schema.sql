DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

INSERT INTO user (username, password) VALUES ('admin', 'adminpass');
INSERT INTO user (username, password) VALUES ('student', 'studentpass');

INSERT INTO post (author_id, title, body) VALUES (1, 'Welcome to the Blog', 'This is the first post on the blog!');
INSERT INTO post (author_id, title, body) VALUES (2, 'Hello World', 'This is a post by a student.');
INSERT INTO post (author_id, title, body) VALUES (1, 'Second Post', 'Another post by the admin user.');
INSERT INTO post (author_id, title, body) VALUES (2, 'Learning SQL', 'This post discusses basic SQL commands.');
INSERT INTO post (author_id, title, body) VALUES (1, 'Database Design', 'An introduction to designing databases.');
