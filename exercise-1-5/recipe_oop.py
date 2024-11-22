class Recipe(object):
    all_ingredients = []
    def __init__(self, name, ingredients, cooking_time):
        '''
        Param self: The Recipe object
        Param name: name of the recipe
        Param: ingredients: a list containing the ingredients for a recipe
        Param: cooking_time: the time taken in minutes to carry out a recipe
        '''
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None
    
    def recipe_search(data, search_term):
        '''
        Param data: a list of Recipe objects to search from
        Param search_term: the ingredient to be searched for
        '''
        for d in data:
            if d.search_ingredient(search_term) == True:
                d.print_recipe()    
            
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
        '''
        Param self:
        Param *ingredients: the recipe's ingredients
        Takes variable-length arguments for the recipe's ingredients and adds them to ingredients and then calls update_all_ingredients()
        
        '''
        for i in ingredients:
            self.ingredients.append(i)
        self.update_all_ingredients()
    
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
        "\nIngredients: " + str(self.ingredients) + \
        "\nCooking Time (in minutes): " + str(self.cooking_time) + \
        "\nDifficulty Level: " + str(self.difficulty)
        print (output)  

tea = Recipe("Tea", [], None)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5
tea.calculate_difficulty()
tea.print_recipe()

coffee = Recipe("Coffee", [], None)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5
coffee.calculate_difficulty()
coffee.print_recipe()

cake = Recipe("Cake", [], None)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50
cake.calculate_difficulty()
cake.print_recipe()

banana_smoothie = Recipe("Banana Smoothie", [], None)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5
banana_smoothie.calculate_difficulty()
banana_smoothie.print_recipe()

recipes_list = [tea, coffee, cake, banana_smoothie]

print("The recipe(s) with the specific ingredient(s)")

Recipe.recipe_search(recipes_list, "Bananas")

print("All ingredients: " + str(Recipe.all_ingredients))