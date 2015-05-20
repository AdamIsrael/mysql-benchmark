#!/usr/bin/env/python
from charmbenchmark import Benchmark
import re
import sys


def parse_sysbench_output():
    output = '\n'.join(sys.stdin.readlines())

    results = {}

    m = re.search(r'total time:\s+(\d+\.\d+s)', output)
    results['time'] = m.group(0)

    m = re.search(r'total number of events:\s+(\d+)', output)
    results['events'] = m.group(0)

    m = re.search(r'total time taken by event execution:\s+(\d+\.\d+)', output)
    results['execution'] = m.group(0)

    m = re.search(r'min:\s+(\d+\.\d+ms)', output)
    results['min'] = m.group(0)

    m = re.search(r'avg:\s+(\d+\.\d+ms)', output)
    results['avg'] = m.group(0)

    m = re.search(r'max:\s+(\d+\.\d+ms)', output)
    results['max'] = m.group(0)

    m = re.search(r'approx.\s+95 percentile:\s+(\d+\.\d+ms)', output)
    results['95th'] = m.group(0)

    m = re.search(r'events \(avg\/stddev\):s+(.*?)$', output)
    if m:
        results['events_stddev'] = m.group(0)

    m = re.search(r'execution time \(avg/stddev\):\s+(\d+\.\d\/\d+\.\d+)', output)
    if m:
        results['time_stddev'] = m.group(0)

    for key in results:
        Benchmark.set_data({"results.%s" % key: results[key]})

    Benchmark.set_composite_score(results['95th'], '95th %', 'asc')

if __name__ == "__main__":
    parse_sysbench_output()
