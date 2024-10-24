```mermaid
erDiagram
    actor {
        id int(11)
        name varchar(50)
    }
    casting {
        movieid int(11)
        actorid int(11)
        ord int(11)
    }
    movie {
        id int(11)
        title varchar(50)
        yr int(11)
        director int(11)
        budget int(11)
        gross int(11)
    }

    actor ||--o{ casting : "participates in"
    movie ||--o{ casting : "features"
```
