#!/usr/bin/env/python
from charms.benchmark import Benchmark
import re
import sys


def search(haystack, needle, filter=None):
    m = re.search(re.escape(needle) + r':\s+(.*)', haystack)
    if m:
        if filter:
            # treat filter as a regex to strip out extraneous data
            m2 = re.search(
                r'%s' % filter,
                m.group(1).strip()
            )
            if m2:
                return m2.group(0)

        return m.group(1).strip()
    return ""


def parse_sysbench_output():
    output = '\n'.join(sys.stdin.readlines())

    results = {}


    results['read'] = {'value': search(output, 'read'), 'units': 'queries'}
    results['write'] = {'value': search(output, 'write'), 'units': 'queries'}
    results['other'] = {'value': search(output, 'other'), 'units': 'queries'}
    results['total'] = {'value': search(output, 'total'), 'units': 'queries'}

    results['transactions'] = {'value': search(output, 'transactions', '\d+'), 'units': ''}
    # results['deadlocks'] = {'value': search(output, 'deadlocks'), 'units': ''}

    results['rw-requests'] = {'value': search(output, 'read/write requests', '\d+'), 'units': ''}

    results['other-operations'] = {'value': search(output, 'other operations', '\d+'), 'units': ''}
    results['total-time'] = {'value': search(output, 'total time', '\d+\.\d+'), 'units': 'seconds'}
    results['events'] = {'value': search(output, 'total number of events', '\d+'), 'units': 'events'}
    results['event-time'] = {'value': search(output, 'total time taken by event execution', '\d+\.\d+'), 'units': 'seconds'}

    results['min'] = {'value': search(output, 'min', '\d+\.\d+'), 'units': 'ms'}
    results['avg'] = {'value': search(output, 'avg', '\d+\.\d+'), 'units': 'ms'}
    results['max'] = {'value': search(output, 'max', '\d+\.\d+'), 'units': 'ms'}

    results['95th'] = {'value': search(output, 'approx.  95 percentile', '\d+\.\d+'), 'units': 'ms'}
    results['avg-time'] = {'value': search(output, 'execution time (avg/stddev)', '\d+\.\d+'), 'units': 'ms'}

    # import json
    # print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))

    # Benchmark.set_data({'results.transactions.value': 1096})
    # Benchmark.set_data({'results.transactions.units': 'hits'})

    for key in results:
        # print {"results.%s.value" % key: results[key]['value']}
        Benchmark.set_data({"results.%s.value" % key: results[key]['value']})
        Benchmark.set_data({"results.%s.units" % key: results[key]['units']})

    Benchmark.set_composite_score(results['95th']['value'], 'ms', 'asc')

if __name__ == "__main__":
    parse_sysbench_output()
