import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute ("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT,
    name VARCHAR(20),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
    )''')

# Definition for operation A
def operation_A():
    ...
    return value

# Definition for operation B
def operation_B():
    ...
    return value

# Definition for operation C
def operation_C():
    ...
    return value

# This is our loop running the main menu.
# It continues to loop as long as the user 
# doesn't choose to quit.
while(choice != 'quit'):
    print("What would you like to do? Pick a choice!")
    print("1. Perform Operation A")
    print("2. Perform Operation B")
    print("3. Perform Operation C")
    print("Type 'quit' to exit the program.")
    choice = input("Your choice: ")
    
    if choice == '1':
        operation_A()
    elif choice == '2':
        operation_B
    elif choice == '3':
        operation_C()        