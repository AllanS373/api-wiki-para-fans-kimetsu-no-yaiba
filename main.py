from http.server import HTTPServer
from routes import KimetsuAPI

# Porta onde o servidor vai rodar
PORT = 8080

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, KimetsuAPI)
    print(f'Servindo na porta {PORT}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
