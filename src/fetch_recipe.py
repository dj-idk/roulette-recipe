"""A module for fetching recipes"""

import aiohttp


async def fetch_response(url, query, filter="meals"):
    """Handles the response for multiple recipe searches"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get(filter):
                        return data[filter]
                    else:
                        print(f"Couldn't find a recipe for: {query}")
                        return None
                else:
                    print(f"Error: Received status code {response.status}")
                    return None
        except aiohttp.ClientError as e:
            print(f"An error occurred: {e}")
            return None


async def fetch_randon_recipe():
    """Fetches a random recipe and returns a json response"""
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("meals"):
                        return data["meals"][0]
                    else:
                        print("Couldn't fetch recipe'")
                        return None
        except aiohttp.ClientError as e:
            print(f"An error occurred: {e}")
            return None


async def search_recipes(food_name: str):
    """Searches for a specific recipe using food name"""
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_name}"
    return await fetch_response(url, query=food_name)


async def search_recipes_by_first_letter(letter: str):
    """Reutrns all meals by first letter"""
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
    return await fetch_response(url, query=letter)
