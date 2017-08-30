#!/usr/bin/env python

import re, sys
from urlparse import urlparse
from subprocess import Popen, PIPE

if len(sys.argv) != 2:
    print 'Usage: %s <heroku app name>' % sys.argv[0]
    exit(-1)

app = sys.argv[1]
print('Fetching database url for: %s\n' % app)
process = Popen(["/usr/local/bin/heroku", "config:get", "DATABASE_URL", "-a", app], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

if exit_code != 0:
    print(output)
    exit(-1)

uri = output
result = urlparse(uri)
auth, host_port = result.netloc.split('@')
username, password = auth.split(':')
host, port = host_port.split(':')
db = re.sub('/', '', result.path)

print('Host:     %s' % host)
print('Port:     %s' % port)
print('Database: %s' % db.rstrip())
print('User:     %s' % username)
print('Password: %s' % password)
