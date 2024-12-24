#imports

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

from sqlalchemy import Column

from sqlalchemy.types import Integer, String

from sqlalchemy.orm import sessionmaker

from config import password

# MUST make this secret!
engine = create_engine("mysql://cf-python:"+ password +"@localhost/task_database")

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        '''
        Param: self
        Shows a quick representation of the recipe
        '''
        return "<Recipe ID: " + str(self.id) + " " + "-" + " " + self.name + ">"
    
    def __str__(self):
        '''
        Param: self
        Prints a well-formatted version of the recipe
        '''
        output = "\nRecipe Name: " + self.name + \
        "\nIngredients: " + str(self.ingredients) + \
        "\nCooking Time (in minutes): " + str(self.cooking_time) + \
        "\nDifficulty Level: " + str(self.difficulty)
        return (output) 
    
    def calc_difficulty (self):
        '''
        Param: self
        Calculates the difficulty level of recipe. Retuns the difficulty of the recipe.
        '''  
        if self.cooking_time < 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = "Hard"           
        return self.difficulty
    
    def return_ingredients_as_list(self):
        '''
        Param: self
        Retrieves the ingredients string inside your Recipe object as a list
        '''
        if self.ingredients == (""):
            return []
        else: 
            return self.ingredients.split(", ")

Base.metadata.create_all(engine)        

def create_recipe():
    '''
    User input for the recipe. Adds to table if conditions are met
    '''           
    recipe_name = str(input("Enter the recipe name: "))
    recipe_cooking_time = str(input("Enter the cooking time (in minutes): "))
    ingredient_num = int(input("Enter the number of ingredient(s): "))
    recipe_ingredients = []
    for i in range(0, ingredient_num):
        ingredient = str(input("Enter one ingredient: "))

        if ingredient not in recipe_ingredients:
            recipe_ingredients.append(ingredient)
    
    recipe_ingredients = (", ").join(recipe_ingredients)        
    # checking the character lengths
    if len(recipe_name) <= 50 and recipe_cooking_time.isnumeric() and len(recipe_ingredients) <= 255:
        recipe_entry = Recipe(
            name = recipe_name,
            cooking_time = int(recipe_cooking_time),
            ingredients = recipe_ingredients
        )
        recipe_entry.calc_difficulty()
        
        session.add(recipe_entry)
        
        session.commit()

def view_all_recipes():
    '''
    Finds all recipes
    ''' 
    all_recipes = session.query(Recipe).all()
    
    if all_recipes == []:
        print("There are no recipes yet")
        return None
        
    for recipe in all_recipes:
        print(recipe)

def search_by_ingredients():
    '''
    Finds (a) recipe(s) based on the ingredient(s)
    '''  
    ingredients_count = session.query(Recipe.ingredients).count()
    if ingredients_count == 0:
        print("There are no ingredients")
        return None
   
    results = session.query(Recipe).all()
    
    all_ingredients = []
    
    for result in results:
        result_list = result.return_ingredients_as_list()
        for result_list_ingredient in result_list:
            if result_list_ingredient not in all_ingredients:
                all_ingredients.append(result_list_ingredient)
    
    for i in range(1, 1 + len(all_ingredients)):
        print(str(i) + (" ") + all_ingredients[i - 1])         

    search_ingredient = str(input("Select the ingredient's number: ")).split(" ")
    
    conditions = []

    for x in search_ingredient:
        condition = ("%" + all_ingredients[int(x) - 1] + "%")
        conditions.append(Recipe.ingredients.like(condition))
    
    search_by_ingredients_results = session.query(Recipe).filter(*conditions).all()
    
    for search_by_ingredients_result in search_by_ingredients_results:
        print(search_by_ingredients_result)
   
def edit_recipe():
    '''
    Edits (a) recipe(s)
    '''
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("There are no recipes")
        return None
    
    results = session.query(Recipe).all()
    
    print(results)
    
    search_id = str(input("Which recipe would you like to edit? Type the ID number: "))
    
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == search_id).one()
    if not recipe_to_edit:
        print("Invalid ID number")
        return None  
    print("1" + " " + "Name: " + " " + recipe_to_edit.name)
    print("2" + " " + "Ingredients: " + " " + recipe_to_edit.ingredients)
    print("3" + " " + "Cooking Time: "  + " " + str(recipe_to_edit.cooking_time))
    
    edit_id = str(input("What part would you like to edit? Type the ID number: "))
    if edit_id == "1":
        user_input_name = str(input("Type the new recipe name: "))
        session.query(Recipe).filter(Recipe.id == search_id).update({Recipe.name: user_input_name})
    
    elif edit_id == "2":
        user_input_ingredients = str(input("Type ALL of the new recipe ingredients: "))
        session.query(Recipe).filter(Recipe.id == search_id).update({Recipe.ingredients: user_input_ingredients})

    elif edit_id == "3":
        user_input_cooking_time = int(input("Type the new cooking time (in minutes): "))
        session.query(Recipe).filter(Recipe.id == search_id).update({Recipe.cooking_time: user_input_cooking_time})
    else:
        print("Invalid number")
        return None   
    
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == search_id).one()
    new_difficulty = recipe_to_edit.calc_difficulty()
    session.query(Recipe).filter(Recipe.id == search_id).update({Recipe.difficulty: new_difficulty})
    session.commit()

def delete_recipe():
    '''
    Deletes (a) recipe(s)
    '''
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("There are no recipes")
        return None
    
    results = session.query(Recipe).all()
    
    print(results)
    
    search_id = str(input("Which recipe would you like to DELETE? Type the ID number: "))
    
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == search_id).one()
    if not recipe_to_delete:
        print("Invalid ID number")
        return None  
    print(recipe_to_delete)

    delete_options = str(input("Are you sure you want to DELETE this recipe? Yes or No?: "))
    if delete_options.upper() == "YES":
       delete_this = session.query(Recipe).filter(Recipe.id == search_id).one()
       session.delete(delete_this)
       session.commit()
    if delete_options.upper() == "NO": 
        print("OK, the recipe will NOT be deleted")
        return None
    else:
        print("Please type 'Yes' or 'No'")   

# This is our loop running the main menu.
# It continues to loop as long as the user 
# doesn't choose to quit.
def main_menu():
    print("Main Menu")
    print("="*43)
    print("What would you like to do? Pick a choice!")
    print("\t1. Create a new recipe")
    print("\t2. View all recipes")
    print("\t3. Search for a recipe by ingredient")
    print("\t4. Update an existing recipe")
    print("\t5. Delete a recipe")
    print("\tType 'quit' to exit the program.")
    choice = input("Your choice: ")
    
    while(choice != 'quit'):
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients() 
        elif choice == '4':
            edit_recipe() 
        elif choice == '5':
            delete_recipe()     
            
        print("Main Menu")
        print("="*43)
        print("What would you like to do? Pick a choice!")
        print("\t1. Create a new recipe")
        print("\t2. View all recipes")
        print("\t3. Search for a recipe by ingredient")
        print("\t4. Update an existing recipe")
        print("\t5. Delete a recipe")
        print("\tType 'quit' to exit the program.")
        choice = input("Your choice: ")
 
main_menu()              