from .postgres import BenchmarkAsyncpg
from .sqlite import BenchmarkAiosqlite
from .python_cache import BenchmarkPythonCache
from .redis import BenchmarkRedisPy
from .helpers import Benchmark

class PyBenchmarker:
    def __init__(self, hosts=[]) -> None:
        self.hosts = hosts
    
    async def do_benchmarks(self):
        results = []
        for host in self.hosts:
            if host[0] == 'asyncpg':
                b_asyncpg = BenchmarkAsyncpg(host=host[1])
                results.append((f'asyncpg {host[1]}', await b_asyncpg.get_benchmark()))
            if host[0] == 'aiosqlite':
                b_aiosqlite = BenchmarkAiosqlite(host=host[1])
                results.append((f'aiosqlite {host[1]}', await b_aiosqlite.get_benchmark()))
            if host[0] == 'python-cache':
                b_pycache = BenchmarkPythonCache()
                results.append((f'pycache', await b_pycache.get_benchmark()))
            if host[0] == 'redis-py':
                b_redis_py = BenchmarkRedisPy()
                results.append((f'redis-py {host[1]}', await b_redis_py.get_benchmark()))
        return results
    
    def print_benchmarks(self, benchmarks: list):
        for b in benchmarks:
            print(b[0])
            Benchmark._pretty_print_res(b[1])
            print('\n')