import time

def do_time_async(func):
    async def runner(*args, **kwargs):
        start_time = time.time()
        res = await func(*args, **kwargs)
        return res, time.time()-start_time, func.__name__
    return runner

def do_time_sync(func):
    async def runner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        return res, time.time()-start_time, func.__name__
    return runner