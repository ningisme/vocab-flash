import http.server
import ssl
import os
import threading

os.chdir('/home/11407655/vocab-app')

# HTTPS on port 443
def run_https():
    server = http.server.HTTPServer(('0.0.0.0', 443), http.server.SimpleHTTPRequestHandler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain('cert.pem', 'key.pem')
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    print("HTTPS on :443")
    server.serve_forever()

# HTTP on port 80
def run_http():
    server = http.server.HTTPServer(('0.0.0.0', 80), http.server.SimpleHTTPRequestHandler)
    print("HTTP on :80")
    server.serve_forever()

# HTTP on port 8080
def run_8080():
    server = http.server.HTTPServer(('0.0.0.0', 8080), http.server.SimpleHTTPRequestHandler)
    print("HTTP on :8080")
    server.serve_forever()

# HTTPS on port 8443
def run_8443():
    server = http.server.HTTPServer(('0.0.0.0', 8443), http.server.SimpleHTTPRequestHandler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain('cert.pem', 'key.pem')
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    print("HTTPS on :8443")
    server.serve_forever()

threads = []
for fn in [run_https, run_http, run_8080, run_8443]:
    t = threading.Thread(target=fn, daemon=True)
    t.start()
    threads.append(t)

print("All servers started. Ports: 80, 443, 8080, 8443")
import time
while True:
    time.sleep(3600)
