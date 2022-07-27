#!/usr/bin/env python

import json

hosts = {
    "node0": ["127.0.0.1"],
    "node1": ["172.16.9.128"],
    "node2": ["172.16.9.129"],
    "open": ["172.16.9.128"],
    "all": ["172.16.9.128", "172.16.9.129"]
}

print(json.dumps(hosts, indent=4))