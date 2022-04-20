from MealList import meals

def convert_ingredient(ingredient):
    if ingredient == 0:
        return "Broccoli"
    elif ingredient == 1:
        return "Onion"
    elif ingredient == 2:
        return "Potato"
    elif ingredient == 3:
        return "Rice"
    elif ingredient == 4:
        return "Rice Noodles"
    elif ingredient == 5:
        return "Chickpeas"
    elif ingredient == 6:
        return "English Peas"
    elif ingredient == 7:
        return "Vegitable Medley"
    elif ingredient == 8:
        return "Tofu"
    elif ingredient == 9:
        return "Tomato Sauce"


def search(ingredients):
    # Create list to store meals that can be cooked with current selection
    converted_ingredients = []
    can_cook = []

    for i in ingredients:
        converted_ingredients.append(convert_ingredient(i))

    for meal in meals:
        # Check if meal ingredients are all included in selection
        check = all(i in converted_ingredients for i in meal[1])
        # Append list to include meal if true
        if check:
            can_cook.append(meal[0])

    return can_cook
