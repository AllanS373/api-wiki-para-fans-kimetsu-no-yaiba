from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Dados de exemplo
data = {
    "personagens": [
        {"id": 1, "nome": "Tanjiro Kamado", "poder": "Respiração do Sol"},
        {"id": 2, "nome": "Nezuko Kamado", "poder": "Demônio"}
    ]
}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/personagens':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data["personagens"]).encode())

    def do_POST(self):
        if self.path == '/personagens':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_character = json.loads(post_data)
            data["personagens"].append(new_character)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(new_character).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
