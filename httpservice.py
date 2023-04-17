import os
import sys
import argparse
import json
import logging
import datetime
import http.server
import socketserver
import re

class MyHTTPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/helloworld':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello Stranger')
        elif self.path.startswith('/helloworld?name='):
            name = self.path.split('=')[1].replace('%20', ' ')
            name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name)
            name = ' '.join([n.capitalize() for n in name.split(' ')])
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(('Hello ' + name).encode())
        elif self.path == '/versionz':
            git_hash = os.environ.get('GIT_HASH', '')
            git_name = os.environ.get('GIT_NAME', '')
            version = {'git_hash': git_hash, 'git_name': git_name}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(version).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Page not found')

def run(port):
    with socketserver.TCPServer(("", port), MyHTTPHandler) as httpd:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info('Starting server on port %d...', port)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        logging.info('Stopping server...')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple HTTP server')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Listening port')
    args = parser.parse_args()
    port = int(os.environ.get('PORT', args.port))
    run(port)