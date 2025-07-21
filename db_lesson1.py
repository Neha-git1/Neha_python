import mysql.connector

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='amazon'
    )
    print("✅ Connected to MySQL")

    cursor = conn.cursor()

    # SQL query to select data
    query = "SELECT * FROM users"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Check if rows exist
    if rows:
        print("User Data:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("⚠️ No data found in the 'users' table.")

    print("hey")  # confirm script reached here

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("❌ MySQL Error:", err)

except Exception as e:
    print("❌ General Error:", e)
