class Recipe(object):
    all_ingredients = []
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None
    
    def recipe_search(data, search_term):
        '''
        Param data: takes in a list of Recipe objects to search from
        Param search_term: the ingredient to be searched for
        '''
        #Step 3
        
    def get_name(self):
        output = str(self.name)
        return output
    
    def get_cooking_time(self):
        output = int(self.cooking_time)
        return output
    
    def get_ingredients(self):
        output = list(self.ingredients)
        return output
    
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty     
            
    def set_name(self):
        self.name = str(input("Enter the recipe name: ")) 
        
    def set_cooking_time(self):
        self.cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    def add_ingredients(self, *ingredients):
        for i in ingredients:
            self.ingredients.append(i)
        #update_all_ingredients()
    
    def calculate_difficulty(self):
        '''
        Param: self
        Calculates and sets the difficulty level of Recipe
        '''
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"           
    
    def search_ingredient(self, ingredient):
         if ingredient in self.ingredients:
             return True
         else:
             return False 
    
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def print_recipe(self):
        '''
        Param: self
        Prints the Recipe class
        
        '''
        output = "\nRecipe Name: " + self.name + \
        "\nIngredients: " + self.ingredients + \
        "\nCooking Time (in minutes): " + self.cooking_time + \
        "\nDifficulty Level: " + self.difficulty
        print (output)  

         
# l = Recipe(name, ingredients, cooking_time)