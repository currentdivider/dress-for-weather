
from langchain.agents import tool

@tool
def count_letters(city: str) -> int:
    """Count the letters in a given city name"""
    count = 0
    for char in city:
        if char.isalpha():
            count += 1
    return count