class Benchmark:
    def __init__(self, pool=None, host=None) -> None:
        self.pool = pool
        self.host = host

    async def _do_cleanup(self):
        pass

    async def benchmark_all(self):
        pass

    async def get_benchmark(self, n_times: int=3):
        results = [await self.benchmark_all() for i in range(n_times)]
        return self._average_benchmarks(results)
        
    def _average_benchmarks(self, benchmarks: list):
        avg_time = sum([x[0] for x in benchmarks])/len(benchmarks)
        avg_indv_times = []
        for i in range(len(benchmarks[0][1])):
            avg_indv_times.append((benchmarks[0][1][i][0], sum([benchmarks[j][1][i][1] for j in range(len(benchmarks))])/len(benchmarks)))
        return avg_time, avg_indv_times

    def _sum_time(self, y: list) -> int:
        return sum([x[1] for x in y])
    
    def _get_times(self, y: list) -> list:
        return [(x[2], x[1]) for x in y]
    
    @staticmethod
    def _pretty_print_res(res: list):
        print(f'Average: {res[0]*1000} ms')
        for i in res[1]:
            print(f'{i[0]}: {i[1]*1000} ms')