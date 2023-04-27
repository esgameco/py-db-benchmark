import os
import asyncio

from dotenv import load_dotenv
load_dotenv()

from src import PyBenchmarker

if __name__ == '__main__':
    hosts = [
        ('asyncpg', os.getenv('DB_POSTGRES')),
        ('aiosqlite', os.getenv('DB_SQLITE')),
        ('python-cache', ''),
    ]
    b_api = PyBenchmarker(hosts=hosts)
    res = asyncio.run(b_api.do_benchmarks())
    b_api.print_benchmarks(res)