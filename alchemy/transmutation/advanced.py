#!usr/bin/env python3
# advanced.py

from ..potions import healing_potion
from .basic import lead_to_gold


def philosophers_stone() -> str:
    return (
        "Philosopher's stone created "
        f"using {lead_to_gold()} and {healing_potion()}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
