import aiosqlite
import time
import random
import sys

from ..helpers import Benchmark, do_time_async

class BenchmarkAiosqlite(Benchmark):
    def __init__(self, pool=None, host=None) -> None:
        super().__init__(pool, host)

    async def _do_cleanup(self):
        await self.b_delete_table()

    @do_time_async
    async def b_create_table(self):
        async with aiosqlite.connect(self.host) as db:
            return await db.execute('''
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    value integer DEFAULT 0
                );
            ''')
    
    @do_time_async
    async def b_delete_table(self):
        async with aiosqlite.connect(self.host) as db:
            return await db.execute('''
                DROP TABLE IF EXISTS test;
            ''')

    @do_time_async
    async def b_insert(self):
        random_value = random.randint(0, 2147483646)
        async with aiosqlite.connect(self.host) as db:
            return await db.execute('''
                INSERT INTO test
                (value)
                VALUES ($1)
            ''', (random_value, ))
    
    @do_time_async
    async def b_update(self):
        async with aiosqlite.connect(self.host) as db:
            return await db.execute('''
                UPDATE test
                SET value = 1
                WHERE id = 1;
            ''')
    
    @do_time_async
    async def b_get(self):
        async with aiosqlite.connect(self.host) as db:
            return await db.execute('''
                UPDATE test
                SET value = 1
                WHERE id = 1;
            ''')
    
    async def benchmark_all(self):
        await self._do_cleanup()

        results = []
        results.append(await self.b_create_table())
        results.append(await self.b_insert())
        results.append(await self.b_update())
        results.append(await self.b_get())
        results.append(await self.b_delete_table())
        return self._sum_time(results), self._get_times(results)
