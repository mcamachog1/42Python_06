# validator.py


def validate_ingredients(ingredients: str) -> str:
    from .spellbook import VALID_INGREDIENTS

    ingredients_list = ingredients.split()
    for ingredient in ingredients_list:
        if ingredient.lower() not in VALID_INGREDIENTS:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
