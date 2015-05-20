# Overview

MySQL-benchmark is a standalone charm for benchmarking MySQL-compatible RDBMS such as MySQL and MariaDB.

# Usage

    juju deploy mysql
    juju deploy mysql-benchmark
    juju add-relation mysql:db mysql-benchmark

# Configuration

The configuration options will be listed on the charm store, however If you're making assumptions or opinionated decisions in the charm (like setting a default administrator password), you should detail that here so the user knows how to change it immediately, etc.

# Contact Information

Though this will be listed in the charm store itself don't assume a user will know that, so include that information here:


- Upstream website
- Upstream bug tracker
- Upstream mailing list or contact information
- Feel free to add things if it's useful for users
