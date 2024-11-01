recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredient_num = int(input("Enter the number of ingredients: "))
    ingredients_list_local = []
    for i in range(0, ingredient_num):
        ingredient = str(input("Enter one ingredient: "))
        
        if ingredient not in ingredients_list_local:
            ingredients_list_local.append(ingredient)
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients_list_local}
    recipes_list.append(recipe)

n = int(input("How many recipes would you like to enter?: "))

for i in range(0, n):
    take_recipe()

for recipe in recipes_list:
    if recipe.get("cooking_time") < 10 and len(recipe.get("ingredients")) < 4:
        difficulty = "Easy"
    elif recipe.get("cooking_time") < 10 and len(recipe.get("ingredients")) >= 4:
        difficulty = "Medium"
    elif recipe.get("cooking_time") >= 10 and len(recipe.get("ingredients")) < 4:
        difficulty = "Intermediate"
    elif recipe.get("cooking_time") >= 10 and len(recipe.get("ingredients")) >= 4:
        difficulty = "Hard"           
    recipe["difficulty_level"] = difficulty

def print_recipe(recipe):
    print("Recipe: " + recipe.get("name"))
    print("Cooking Time (min): " + str(recipe.get("cooking_time")))
    for ingredient in recipe.get("ingredients"):
        print(ingredient)
    print("Difficulty level: " + recipe.get("difficulty_level"))

for recipes in recipes_list:
    print_recipe(recipes)

ingredients_list.sort()

print("Ingredients Available Across All Recipes")
print("----------------------------------------")
for ingredient in ingredients_list:  
    print(ingredient)   


  