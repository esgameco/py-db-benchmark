import aiosqlite
import time
import random
import sys

from ..helpers import Benchmark, do_time_async

class BenchmarkPythonCache(Benchmark):
    def __init__(self, pool=None, host=None) -> None:
        super().__init__(pool, host)
        self._cache = []

    async def _do_cleanup(self):
        self._cache = []

    @do_time_async
    async def b_insert(self):
        random_value = random.randint(0, 2147483646)
        self._cache.append(random_value)
    
    @do_time_async
    async def b_update(self):
        self._cache[0] = 1
    
    @do_time_async
    async def b_get(self):
        return self._cache[0]
    
    async def benchmark_all(self):
        await self._do_cleanup()

        results = []
        results.append(await self.b_insert())
        results.append(await self.b_update())
        results.append(await self.b_get())
        return self._sum_time(results), self._get_times(results)
