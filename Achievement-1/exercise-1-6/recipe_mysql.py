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

def create_recipe(conn, cursor):
    '''
    Params: conn & cursor.
    Taking in the recipe name, cooking time, and ingredients from the user. 
    Calculating the difficulty of the recipe. Gathering all these attributes into the Recipes Table
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
    '''
    Params: conn, cursor, and recipe.
    The ingredients_string gets converted into a comma-separated strings for MySQL. 
    '''
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
    Calculates the difficulty level of recipe. Retuns the difficulty_level of the recipe.
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

def search_recipe(conn, cursor):
    '''
    Params: conn & cursor
    User searches the Recipes table based on the ingredient column. Adds new ingredients to all_ingredients list.
    '''
    cursor.execute("SELECT ingredients FROM Recipes")
   
    results = cursor.fetchall()
   
    for row in results:
        for ingredient in row[0].split(", "):
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    for i in range(1, 1 + len(all_ingredients)):
        print(str(i) + (" ") + all_ingredients[i - 1])         

    search_ingredient = int(input("Select the ingredient's number: "))
    sql = "SELECT * FROM Recipes WHERE ingredients LIKE '%" +  all_ingredients[search_ingredient - 1] + "%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

def update_recipe(conn, cursor):
    '''
    Params: conn & cursor
    User chooses what column to update (name, ingredients or cooking_time). New difficulty is calculated when ingredients or cooking_time are updated.
    '''
    cursor.execute("SELECT * FROM Recipes")
   
    results = cursor.fetchall()
    
    for row in results:
        #Prints all the columns in the Recipe table
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty:", row[4])
        print()  
    
    choose_recipe = int(input("Select the number of the recipe you want to update: "))
    sql = "SELECT * FROM Recipes WHERE id =" + str(choose_recipe)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    
    update_recipe_column = int(input("Do you want to update the (1) Name, (2) Ingredients or (3) Cooking Time?: "))
    if update_recipe_column == 1:
        new_name = str(input("Enter the new name: "))
        sql = "UPDATE Recipes SET name ='" + new_name + "' WHERE id =" + str(choose_recipe)
        cursor.execute(sql)
    
    elif update_recipe_column == 2:
        new_ingredients = str(input("Enter the new ingredient(s) Use commas to separate each ingredient: "))
        recipe = {"name": results[0][1], "cooking_time": results[0][3], "ingredients": new_ingredients.split(", ")}
        new_difficulty = calc_difficulty(recipe)
        sql = "UPDATE Recipes SET ingredients ='" + new_ingredients + "' WHERE id =" + str(choose_recipe)
        cursor.execute(sql)
        
        recipe["difficulty"] = new_difficulty
        sql1 = "UPDATE Recipes SET difficulty ='" + new_difficulty + "' WHERE id =" + str(choose_recipe)
        cursor.execute(sql1)
    
    elif update_recipe_column == 3:
        new_cooking_time = int(input("Enter the new cooking time (in minutes): "))
        recipe = {"name": results[0][1], "cooking_time": new_cooking_time, "ingredients": results[0][2].split(", ")}
        new_difficulty = calc_difficulty(recipe)
        sql = "UPDATE Recipes SET cooking_time ='" + str(new_cooking_time) + "' WHERE id =" + str(choose_recipe)
        cursor.execute(sql) 
        
        recipe["difficulty"] = new_difficulty
        sql1 = "UPDATE Recipes SET difficulty ='" + new_difficulty + "' WHERE id =" + str(choose_recipe)
        cursor.execute(sql1)      
    conn.commit()   

def delete_recipe(conn, cursor):
    '''
    Params: conn & cursor.
    The user selects the Recipe row they want to delete.
    '''
    cursor.execute("SELECT * FROM Recipes")
   
    results = cursor.fetchall()
    
    for row in results:
        #Prints all the columns in the Recipe table
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty:", row[4])
        print()  
    
    delete_recipe = int(input("Select the number of the recipe you want to delete: "))
    sql = "SELECT * FROM Recipes WHERE id =" + str(delete_recipe)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    
    sql1 = "DELETE FROM Recipes WHERE id = " + str(delete_recipe)
    cursor.execute(sql1)
    print(results)
    
    conn.commit()

# This is our loop running the main menu.
# It continues to loop as long as the user 
# doesn't choose to quit.
def main_menu():
    print("What would you like to do? Pick a choice!")
    print("1. Create a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("Type 'quit' to exit the program.")
    choice = input("Your choice: ")
    
    while(choice != 'quit'):
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor) 
        elif choice == '4':
            delete_recipe(conn, cursor) 
            
        print("What would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")
 
main_menu()


   





