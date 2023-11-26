import http.server
import socketserver

port = 8000

custom_html = ""
with open("index.html", "r") as html_file:
    custom_html = html_file.read()

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servindo na porta {port}")
    httpd.serve_forever()
