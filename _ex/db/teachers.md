```mermaid
erDiagram
    dept {
        id int(11)
        name varchar(50)
    }
    teacher {
        id int(11)
        dept int(11)
        name varchar(50)
        phone varchar(50)
        mobile varchar(50)
    }
    dept ||--o{ teacher : "has"
```
