import redis.asyncio as redis
import time
import random
import sys

from ..helpers import Benchmark, do_time_async

class BenchmarkRedisPy(Benchmark):
    def __init__(self, pool=None, host=None) -> None:
        super().__init__(pool, host)

    async def _do_cleanup(self):
        await self.b_create_pool()
        await self.b_clear_db()
        await self.b_delete_pool()

    @do_time_async
    async def b_create_pool(self):
        self.pool = redis.from_url(self.host)
        await self.pool.ping()
    
    @do_time_async
    async def b_delete_pool(self):
        await self.pool.close()
    
    @do_time_async
    async def b_clear_db(self):
        await self.pool.flushdb()

    @do_time_async
    async def b_insert(self):
        random_value = random.randint(0, 2147483646)
        return await self.pool.set(1, random_value)
    
    @do_time_async
    async def b_update(self):
        return await self.pool.set(1, 1)
    
    @do_time_async
    async def b_get(self):
        return await self.pool.get(1)
    
    async def benchmark_all(self):
        await self._do_cleanup()

        results = []
        results.append(await self.b_create_pool())
        results.append(await self.b_insert())
        results.append(await self.b_update())
        results.append(await self.b_get())
        results.append(await self.b_delete_pool())
        return self._sum_time(results), self._get_times(results)
