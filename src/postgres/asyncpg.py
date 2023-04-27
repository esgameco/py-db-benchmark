import asyncpg
import time
import random
import sys

from ..helpers import Benchmark, do_time_async

class BenchmarkAsyncpg(Benchmark):
    def __init__(self, pool=None, host=None) -> None:
        super().__init__(pool, host)

    async def _do_cleanup(self):
        await self.b_asyncpg_create_pool()
        await self.b_asyncpg_delete_table()
        await self.b_asyncpg_delete_pool()

    @do_time_async
    async def b_asyncpg_create_pool(self):
        self.pool = await asyncpg.create_pool(self.host)
    
    @do_time_async
    async def b_asyncpg_delete_pool(self):
        return await self.pool.close()

    @do_time_async
    async def b_asyncpg_create_table(self):
        async with self.pool.acquire() as conn:
            return await conn.execute('''
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    value integer DEFAULT 0
                );
            ''')
    
    @do_time_async
    async def b_asyncpg_delete_table(self):
        async with self.pool.acquire() as conn:
            return await conn.execute('''
                DROP TABLE IF EXISTS test;
            ''')

    @do_time_async
    async def b_asyncpg_insert(self):
        random_value = random.randint(0, 2147483646)
        async with self.pool.acquire() as conn:
            return await conn.execute('''
                INSERT INTO test
                (value)
                VALUES ($1)
            ''', random_value)
    
    @do_time_async
    async def b_asyncpg_update(self):
        async with self.pool.acquire() as conn:
            return await conn.execute('''
                UPDATE test
                SET value = 1
                WHERE id = 1;
            ''')
    
    @do_time_async
    async def b_asyncpg_get(self):
        async with self.pool.acquire() as conn:
            return await conn.execute('''
                UPDATE test
                SET value = 1
                WHERE id = 1;
            ''')
    
    async def benchmark_all(self):
        await self._do_cleanup()

        results = []
        results.append(await self.b_asyncpg_create_pool())
        results.append(await self.b_asyncpg_create_table())
        results.append(await self.b_asyncpg_insert())
        results.append(await self.b_asyncpg_update())
        results.append(await self.b_asyncpg_get())
        results.append(await self.b_asyncpg_delete_table())
        results.append(await self.b_asyncpg_delete_pool())
        return self._sum_time(results), self._get_times(results)
