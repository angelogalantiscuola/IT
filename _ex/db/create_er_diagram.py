import mysql.connector


def generate_er_diagram(database) -> str:
    # Connect to MariaDB
    conn = mysql.connector.connect(
        host="localhost",
        user="x",
        password="x",
        database=database,
    )

    cursor = conn.cursor()

    # Query to get tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Query to get columns and their types
    columns_query = f"""
    SELECT TABLE_NAME, COLUMN_NAME, COLUMN_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '{database}'
    """

    cursor.execute(columns_query)
    columns = cursor.fetchall()

    # Query to get foreign keys
    foreign_keys_query = f"""
    SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = '{database}' AND REFERENCED_TABLE_NAME IS NOT NULL
    """

    cursor.execute(foreign_keys_query)
    foreign_keys = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    # Generate Mermaid syntax
    mermaid_syntax = "erDiagram\n"

    # Add tables and columns
    for table in tables:
        table_name = table[0]
        mermaid_syntax += f"    {table_name} {{\n"
        for column in columns:
            if column[0] == table_name:
                mermaid_syntax += f"        {column[1]} {column[2]}\n"
        mermaid_syntax += "    }\n"

    # Add relationships
    for fk in foreign_keys:
        mermaid_syntax += f'    {fk[0]} ||--o| {fk[2]} : "{fk[1]} references {fk[3]}"\n'

    # Print the Mermaid syntax

    return mermaid_syntax


# Example usage
db_name = "world"
er_diagram = generate_er_diagram(db_name)
print(er_diagram)

# create a file with the diagram in the same directory
# the file should be an .md with a mermaid code block
with open(f"{db_name}.md", "w") as file:
    file.write("```mermaid\n")
    file.write(er_diagram)
    file.write("```")
