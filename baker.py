def cake(available, recipe):
    for ingredient in recipe:
        if ingredient in available:
            count_of_ingredient_available = available.get(ingredient)
            count_of_ingredient_in_recipe = recipe.get(ingredient)
            return count_of_ingredient_available//count_of_ingredient_in_recipe

    return 0