# .env

`.env` is a plain text file that is used to store environment variables. Environment variables are a kind of variable that is available system-wide and can be used to configure your application's behavior. For example, you might use environment variables to store API keys, database connection strings, or the path to important directories. The `.env` file is often used in local development to mimic the environment variables that will be used in production. However, because they can contain sensitive information, `.env` files should not be tracked by Git and should be included in your *.gitignore* file.

``` txt
# .env file

DB_HOST=localhost
DB_USER=my_database_user
DB_PASS=my_database_password
DB_NAME=my_database_name

API_KEY=my_api_key
```

- `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` are environment variables used to configure a database connection. They represent the database host, user, password, and database name, respectively.
- `API_KEY` is an environment variable that might be used to authenticate with an external API.
