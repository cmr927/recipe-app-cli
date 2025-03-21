#import(s)
import pickle

#empty lists
recipes_list = []
all_ingredients = []

def take_recipe():
    '''
    Taking in the recipe name, cooking time, and ingredients from the user. Calculating the difficulty of the recipe. Gathering all these attributes into a dictionary and putting them into recipes_list
    '''
    name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredient_num = int(input("Enter the number of ingredient(s): "))
    ingredients_list_local = []
    for i in range(0, ingredient_num):
        ingredient = str(input("Enter one ingredient: "))
        
        if ingredient not in ingredients_list_local:
            ingredients_list_local.append(ingredient)
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients_list_local}
    difficulty = calc_difficulty(recipe)
    recipe["difficulty_level"] = difficulty
    recipes_list.append(recipe)
    
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

def print_recipe(recipe):
    '''
    Param: recipe is a dictionary with the keys name, cooking_time, ingredients and difficulty_level.
    Prints the recipe dictonary
    
    '''
    print("Recipe: " + recipe.get("name"))
    print("Cooking Time (min): " + str(recipe.get("cooking_time")))
    for ingredient in recipe.get("ingredients"):
        print(ingredient)
    print("Difficulty level: " + recipe.get("difficulty_level"))    

#User inputs the file name
try:
    file_name = str(input("Enter the file name: "))
    user_file = open(file_name, 'rb')
    data = pickle.load(user_file)
except FileNotFoundError:
    data = { "recipes_list": [],
            "all_ingredients": [] 
    }
except:
    data = { "recipes_list": [],
            "all_ingredients": [] 
    }
else:         
    user_file.close()
finally: 
    recipes_list = data.get("recipes_list")
    all_ingredients = data.get("all_ingredients")
    print("recipe_list", recipes_list, "all_ingredients", all_ingredients)
    
#User input
n = int(input("How many recipes would you like to enter?: "))

#Adding the recipes and ingredients to their respective lists
for i in range(0, n):
    take_recipe()
data["recipes_list"] = recipes_list
data["all_ingredients"] = all_ingredients
print(data)

#Updateding the user file with the information
user_file = open(file_name, 'wb')
pickle.dump(data, user_file)
user_file.close()
