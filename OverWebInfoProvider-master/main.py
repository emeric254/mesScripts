#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer
from OWIPServer import HTTPHandler

httpd = HTTPServer(('',8080),HTTPHandler)  # port 8080
httpd.serve_forever()
