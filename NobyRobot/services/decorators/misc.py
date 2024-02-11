 
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.

from functools import wraps
from time import time


def exec_time(func):
    @wraps(func)
    async def _time_it(*args, **kwargs):
        t1 = time()
        try:
            return await func(*args, **kwargs)
        finally:
            t2 = time()
            total = t2 - t1
            total = round(total, 3)
            print(f"{func.__name__} Took: {total} Seconds")

    return _time_it
