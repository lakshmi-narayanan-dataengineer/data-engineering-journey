import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="latchu",
    database="new",
    auth_plugin="mysql_native_password"
)

try:
    # 1. Create cursor directly without 'with'
    cursor = connection.cursor()

    # 2. Execute table creation
    create_query = """
    CREATE TABLE IF NOT EXISTS Employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100)
    );
    """
    cursor.execute(create_query)

    # 3. Insert data
    insert_query = "INSERT INTO Employees (name, department) VALUES (%s, %s);"
    values = [("John", "IT"), ("Anu", "HR")]
    cursor.executemany(insert_query, values)
    
    # Save changes to the database
    connection.commit()

    # 4. Fetch and display data
    select_query = "SELECT * FROM Employees;"
    cursor.execute(select_query)
    results = cursor.fetchall()

    print("\n--- Employee Records ---")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 5. Clean up both cursor and connection safely
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")