import pickle

def display_recipe(recipe):
    '''
    param: recipe is a dictionary with the keys name, cooking_time, ingredients and difficulty_level.
    Prints the values of the recipe
    '''
    print(recipe.get("name"))
    print(recipe.get("cooking_time"))
    print(recipe.get("ingredients"))
    print(recipe.get("difficulty_level"))

def search_ingredient(data):
    '''
    param: data is a dictionary with the keys all_ingredients
    Prints all numbered ingredients in data. User can pick a number, retrieve the corresponding ingredient, and each recipe that contains the given ingredient will be printed.
    '''
    print("All Ingredients:")
    for position, value in enumerate(data.get("all_ingredients"),1):
        print (value, position)
        
    try:
        a = int(input("Enter a number from this list: "))
        ingredient_searched =  data.get("all_ingredients")[a-1]
    except ValueError:
        print ("Please enter a number")
    except IndexError:
        print ("Please enter a number from the ingredients list")
    else:
        for flub in data.get("recipes_list"):
            blub = flub.get("ingredients")
            if ingredient_searched in blub:
                print(flub)
                
search_ingredient(
    {
        "all_ingredients": ["pasta", "sauce"],
        "recipes_list": [{
            "name": "spaghetti",
            "ingredients": ["pasta", "sauce"]
        },
                         {
            "name": "butter noodles",
            "ingredients": ["pasta", "butter"]
        }]
    }
)