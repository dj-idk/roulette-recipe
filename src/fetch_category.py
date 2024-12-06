import asyncio
import aiohttp


async def get_all_categories():
    """Returns all the categories"""
    url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("categories"):
                        return data["categories"]
                    else:
                        print("Couldn't fetch categories")
                        return None
                else:
                    print(f"Error: Recived status code: {response.status}")

        except aiohttp.ClientError as e:
            print(f"An error occurred: {e}")
            return None


async def get_specific_category(category: str):
    """Get specific category"""
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("meals"):
                        return data["meals"]
                    else:
                        print(f"Couldn't find {category} category.")
                        return None
                else:
                    print(f"Error: recieved status code: {response.status}")
        except aiohttp.ClientError as e:
            print(f"An error occured:{e}")


# print(asyncio.run(get_specific_category("dick")))
