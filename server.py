from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8080

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Grove Server iniciado en http://localhost:{PORT}")

server.serve_forever()