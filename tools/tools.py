
from langchain.agents import tool

@tool
def count_letters(city: str) -> str:
    """Count the letters in a given city name"""
    return str(len(city))