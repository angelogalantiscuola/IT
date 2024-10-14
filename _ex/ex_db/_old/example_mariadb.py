import mariadb

# Connect to MariaDB
conn = mariadb.connect(
    user="x", password="x", host="localhost", port=3306, database="w3schools"
)

# Create a cursor object
cur = conn.cursor()

# List all tables in the database
cur.execute("SHOW TABLES")
tables = cur.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Describe each table
for table in tables:
    print(f"\nDescription of table {table[0]}:")
    cur.execute(f"DESCRIBE {table[0]}")
    description = cur.fetchall()
    for row in description:
        print(row)

# Close the connection
cur.close()
conn.close()
