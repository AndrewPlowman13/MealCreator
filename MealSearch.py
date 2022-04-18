from MealList import meals


def search(ingredients):
    # Create list to store meals that can be cooked with current selection
    can_cook = []

    for meal in meals:
        # Check if meal ingredients are all included in selection
        check = all(i in ingredients for i in meal[1])
        # Append list to include meal if true
        if check:
            can_cook.append(meal[0])

    return can_cook
