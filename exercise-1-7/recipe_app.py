#imports

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

from sqlalchemy import Column

from sqlalchemy.types import Integer, String

from sqlalchemy.orm import sessionmaker

# MUST make this secret!
engine = create_engine("mysql://cf-python:password@localhost/task_database")

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
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
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
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
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
    # recipe_name checking character length is => 50
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
    all_recipes = session.query(Recipe).all()
    
    if all_recipes == []:
        print("There are no recipes yet")
        return None
        
    for recipe in all_recipes:
        print(recipe)

view_all_recipes()     



