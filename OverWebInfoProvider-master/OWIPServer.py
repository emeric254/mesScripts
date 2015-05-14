#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SimpleHTTPServer import SimpleHTTPRequestHandler
import cgi, pagecontent


class HTTPHandler (SimpleHTTPRequestHandler):
    server_version = "CustomPythonHTTP/0.1a"

    def do_GET(self):
        if self.path in ("/favicon.ico", "/style.css"):
            SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.requete = ''
            if self.path != "/" and self.path.find('?') != -1:
                self.path, self.requete = self.path.split('?', 1)
            self.reponse()

    def do_POST(self):
        self.requete = self.rfile.read(int(self.headers['Content-Length']))
        self.reponse()

    def reponse(self):
        self.page = self.path[1:]
        self.args = dict(cgi.parse_qsl(self.requete))
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.send_header('Charset', 'UTF-8')
        self.end_headers()

        self.wfile.write('<html>\n')
        self.wfile.write(pagecontent.corps(self.client_address[0]))
        self.wfile.write('</html>\n')
