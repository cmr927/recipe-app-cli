# recipe-app-cli

## Description
This is the command line version of a Recipe app using Python. The Django web app counterpart is coming soon.

Users can create and modify recipes with ingredients, cooking time, and a difficulty parameter that is automatically calculated by the app. Users should also be able to search for recipes by their ingredients.

## Features
- Create and manage the user’s recipes on a locally hosted MySQL database.
- Option to search for recipes that contain a set of ingredients specified by the user.
- Automatically rate each recipe by their difficulty level.
- Display more details on each recipe if the user prompts it, such as the ingredients, cooking time, and difficulty of the recipe.

## Data Structures
The data structure for the **individual recipes** is a dictionary because each recipe contains multiple data types such as strings for the names, ints for the cooking times and lists for the ingredients. Unlike tuples and lists, dictionaries utilize key-value pairs to keep all of the data types organized.

The data structure for **all_recipies** is a list because I am saving the keys of the individual recipe dictionaries. Lists are typically faster to load than dictionaries and they are mutable, making it easier to modify data. 