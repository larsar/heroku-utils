#!/usr/bin/env python

import os, re
from urlparse import urlparse

uri = os.environ['PGURL']
result = urlparse(uri)
auth, host_port = result.netloc.split('@')
username, password = auth.split(':')
host, port = host_port.split(':')
db = re.sub('/', '', result.path)

print('Host:     %s' % host)
print('Port:     %s' % port)
print('Database: %s' % db)
print('User:     %s' % username)
print('Password: %s' % password)
