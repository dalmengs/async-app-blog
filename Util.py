import asyncio
import functools

def Print(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"{func.__name__} start")
        result = await func(*args, **kwargs)
        print(f"{func.__name__} end")
        return result
    return wrapper