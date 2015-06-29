#!/usr/bin/env/python
from charmbenchmark import Benchmark
import re
import sys


def search(haystack, needle):
    m = re.search(re.escape(needle) + r':\s+(.*)', haystack)
    if m:
        return m.group(1).strip()
    return ""


def parse_sysbench_output():
    output = '\n'.join(sys.stdin.readlines())

    results = {}

    results['read'] = search(output, 'read')
    results['write'] = search(output, 'write')
    results['other'] = search(output, 'other')
    results['total'] = search(output, 'total')
    results['transactions'] = search(output, 'transactions')
    results['deadlocks'] = search(output, 'deadlocks')
    results['rw.requests'] = search(output, 'read/write requests')
    results['other.operations'] = search(output, 'other operations')
    results['total.time'] = search(output, 'total time')
    results['events'] = search(output, 'total number of events')
    results['event.time'] = search(output, 'total time taken by event execution')
    results['min'] = search(output, 'min')
    results['avg'] = search(output, 'avg')
    results['max'] = search(output, 'max')
    results['95th'] = search(output, 'approx.  95 percentile')
    results['avg.events'] = search(output, 'events (avg/stddev)')
    results['avg.time'] = search(output, 'execution time (avg/stddev)')

    for key in results:
        Benchmark.set_data({"results.%s" % key: results[key]})

    Benchmark.set_composite_score(results['95th'], '', 'asc')

if __name__ == "__main__":
    parse_sysbench_output()
