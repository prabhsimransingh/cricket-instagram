#!/usr/bin/env python3
import http.server, socketserver, os

PORT = 8732
DIR = "/Users/prabhsingh/Documents/Code/cricket-ig-pages"

os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {DIR} on port {PORT}")
    httpd.serve_forever()
