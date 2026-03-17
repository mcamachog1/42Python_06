# potions.py


from alchemy.elements import (
    create_fire,
    create_water,
    create_earth,
    create_air
)


def healing_potion() -> str:
    fire: str = create_fire()
    water: str = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    fire: str = create_fire()
    earth: str = create_earth()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    air: str = create_air()
    water: str = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    fire: str = create_fire()
    earth: str = create_earth()
    air: str = create_air()
    water: str = create_water()
    all: str = f"{fire} {water} {earth} {air}"
    return f"Wisdom potion brewed with {all}"
