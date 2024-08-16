#!/usr/bin/python3

import re

ipaddress = r'^(\b(?:\d{1,3}\.){3}\d{1,3}\b)'
underscore = r' - '
timestamp = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]'
httprequest = r' "GET /projects/260 HTTP/1\.1"'
code = r' (\d{3})'
size = r' (\d+)$'
linein = '78.99.227.220 - [2017-02-05 23:25:51.534767] "GET /projects/260 HTTP/1.1" 401 724'

pattern = ipaddress + underscore + timestamp + httprequest + code + size
# print(pattern)

# match = re.match(pattern, linein)
_pattern = re.compile(pattern)
matches = _pattern.finditer(linein)



for match in matches:
    print(match.group(0))
