import mysql.connector

# Create connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyadarshee@2003"
)

cursor = connection.cursor()
print("Connected successfully")

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

# Reconnect with database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyadarshee@2003",
    database="school"
)

cursor = connection.cursor()
print("Connected successfully")

# Create table (removed trailing comma)
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    studentid INT AUTO_INCREMENT PRIMARY KEY,
    studentname VARCHAR(50),
    subject VARCHAR(50),
    marks INT
)
''')

connection.commit()

# Correct insert query (remove studentid)
query = "INSERT INTO students (studentname, subject, marks) VALUES (%s, %s, %s)"

# Insert single record
values = [("John", "Maths", 85)]
cursor.executemany(query, values)
connection.commit()

# Insert multiple records
students_data = [
    ("Ravi", "Science", 90),
    ("Sneha", "Math", 78),
    ("Kiran", "Science", 88)
]

cursor.executemany(query, students_data)
connection.commit()

# Read the data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

#update the data
cursor.execute("Update students SET marks = 95 where studentname ='John'")
connection.commit()
#delete data
cursor.execute("DELETE FROM students WHERE studentname ='Sneha'")
connection.commit()


