
# spellbook.py

from .validator import validate_ingredients

VALID_INGREDIENTS = ["air", "fire", "earth", "water"]

def record_spell(spell_name: str, ingredients: str) -> str:

    result: str = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
