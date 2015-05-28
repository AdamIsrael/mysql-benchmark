# Overview

Requires Juju 1.23 or later

MySQL-benchmark is a standalone charm for benchmarking MySQL-compatible RDBMS such as MySQL, Percona and MariaDB.

# Usage

    juju deploy mysql
    juju deploy mysql-benchmark
    juju add-relation mysql:db mysql-benchmark

# Running a benchmark

You can see the list of benchmarks available at any time by executing `juju action defined mysql-benchmark`. To run a benchmark:

    $ juju action do mysql-benchmark/0 oltp
    Action queued with id: 097d714d-455e-47d6-8cc9-3eef5f9d5cad

Benchmarks may take a few seconds or several minutes. You can check the status of an action:

    $ juju action status 097d714d-455e-47d6-8cc9-3eef5f9d5cad

Or you can wait for the action to finish and fetch the results:

    $ juju action fetch --wait 0 097d714d-455e-47d6-8cc9-3eef5f9d5cad

Each action has a set of parameters you can use to customize the benchmark run.

    $ juju action do mysql-benchmark/0 oltp mysql-table-engine="myisam" thread-stack-size="64K"

You can view the complete list of parameters by viewing the `actions.yaml` file.

# Contact Information

- [Home page](https://github.com/juju-solutions/mysql-benchmark)
- [Bug tracker](https://github.com/juju-solutions/mysql-benchmark/issues)
