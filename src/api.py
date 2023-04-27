from .postgres import BenchmarkAsyncpg
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
        return results
    
    def print_benchmarks(self, benchmarks: list):
        for b in benchmarks:
            print(b[0])
            Benchmark._pretty_print_res(b[1])
            print('\n')