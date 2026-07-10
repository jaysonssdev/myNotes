import sqlite3

def save_user(name, age):
    # Establish a connection to the local SQLite database file named 'users.db'
    conn = sqlite3.connect("users.db")
    
    # Create a cursor object, which allows you to execute SQL commands
    cursor = conn.cursor()
    
    # Execute the SQL statement using parameterized queries to safely insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    
    # Save (commit) the changes permanently to the database file
    conn.commit()
    
    # Close the database connection to free up system resources
    conn.close()