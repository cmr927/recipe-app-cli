import mysql.connector
# import(s)

all_ingredients = []
#empty list

conn = mysql.connector.connect(
    # Connects this Python file to MySQL
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute ("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
    )''')


# Definition for create_recipe()
def create_recipe(conn, cursor):
    '''
    Taking in the recipe name, cooking time, and ingredients from the user. 
    Calculating the difficulty of the recipe. Gathering all these attributes into a dictionary and putting them into recipes_list
    '''
    name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredient_num = int(input("Enter the number of ingredient(s): "))
    ingredients_list_local = []
    for i in range(0, ingredient_num):
        ingredient = str(input("Enter one ingredient: "))
    
        if ingredient not in ingredients_list_local:
            ingredients_list_local.append(ingredient)

    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients_list_local}
    difficulty = calc_difficulty(recipe)
    recipe["difficulty_level"] = difficulty
    insert_recipe(conn, cursor, recipe)

def insert_recipe(conn, cursor, recipe):
    ingredients_string = (", ").join(recipe.get("ingredients"))
    sql = '''INSERT INTO Recipes
    (name, ingredients, cooking_time, difficulty)
    VALUES (%s, %s, %s, %s)
    '''
    val = (recipe.get("name"), ingredients_string, recipe.get("cooking_time"), recipe.get("difficulty_level"))
    cursor.execute(sql, val)
    conn.commit()   
        
def calc_difficulty (recipe):
    '''
    Param: recipe is a dictionary with the keys name, cooking_time, and ingredients.
    Calculates the difficulty level of recipe. Retuns the difficulty_level of the recipe
    '''
    if recipe.get("cooking_time") < 10 and len(recipe.get("ingredients")) < 4:
        difficulty = "Easy"
    elif recipe.get("cooking_time") < 10 and len(recipe.get("ingredients")) >= 4:
        difficulty = "Medium"
    elif recipe.get("cooking_time") >= 10 and len(recipe.get("ingredients")) < 4:
        difficulty = "Intermediate"
    elif recipe.get("cooking_time") >= 10 and len(recipe.get("ingredients")) >= 4:
        difficulty = "Hard"           
    return difficulty

# # Definition for search_recipe()
def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
   
    results = cursor.fetchall()
   
    for row in results:
        for ingredient in row[0].split(", "):
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    for i in range(1, 1 + len(all_ingredients)):
        print(str(i) + (" ") + all_ingredients[i - 1])         

    search_ingredient = int(input("Enter the number of the ingredient: "))
    sql = "SELECT * FROM Recipes WHERE ingredients LIKE '%" +  all_ingredients[search_ingredient - 1] + "%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

# # Definition for update_recipe()
# def update_recipe(conn, cursor):
#     ...
#     return value

# # Definition for delete_recipe()
# def delete_recipe(conn, cursor):
#     ...
#     return value

# This is our loop running the main menu.
# It continues to loop as long as the user 
# doesn't choose to quit.
def main_menu():
    while(choice != 'quit'):
        print("What would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

    # if choice == '1':
    #     create_recipe()
    # elif choice == '2':
    #     search_recipe()
    # elif choice == '3':
    #     update_recipe() 
    # elif choice == '4':
    #     delete_recipe()          
    
# create_recipe(conn, cursor)

# cursor.execute("SELECT name, ingredients, cooking_time, difficulty FROM Recipes")

search_recipe(conn, cursor)

# results = cursor.fetchall()

# for row in results:
    # print("Name: ", row[0])
    # print("Ingredients: ", row[1])
    # print("Cooking Time: ", row[2])
    # print("Difficulty:", row[3])
    # print()    





