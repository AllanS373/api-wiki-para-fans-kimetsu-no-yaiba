from http.server import BaseHTTPRequestHandler
import json
from repositories.arc_repository import ArcRepository
from models.arc_model import Arc

class ArcController(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/arcs':
            self.repo = ArcRepository()
            arcs = self.repo.load_arcs()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([arc.to_dict() for arc in arcs]).encode())
        elif self.path.startswith('/arcs/'):
            try:
                id = int(self.path.split('/')[-1])
                arc = self.repo.find_by_id(id)
                if arc:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(arc.to_dict()).encode())
                else:
                    self.send_error(404, 'Arco não encontrado')
            except ValueError:
                self.send_error(400, 'ID inválido')
    def do_POST(self):
        if self.path == '/arcs':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                new_arc = Arc(None, data['nome'], data['description'])
                added_arc = self.repo.add_arc(new_arc)
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(added_arc.to_dict()).encode())
            except json.JSONDecodeError:
                self.send_error(400, 'Erro de formato no corpo da requisição')
