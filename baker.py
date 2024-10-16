def cake(available, recipe):

    return_value = 0
    cake_counts = []

    for ingredient in recipe:
        if ingredient in available:
            count_of_ingredient_available = available.get(ingredient)
            count_of_ingredient_in_recipe = recipe.get(ingredient)
            cake_counts.append(count_of_ingredient_available//count_of_ingredient_in_recipe)
        else:
            cake_counts.append(0)

    if cake_counts:
        return_value = min(cake_counts)

    return return_value