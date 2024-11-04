from http.server import BaseHTTPRequestHandler
import json
from repositories.character_repository import CharacterRepository
from models.character_model import Character

class CharacterController(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == '/characters':
            self.repo = CharacterRepository()
            characters = self.repo.load_characters()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([char.to_dict() for char in characters]).encode())
        elif self.path.startswith('/characters/'):
            try:
                id = int(self.path.split('/')[-1])
                character = self.repo.find_by_id(id)
                if character:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(character.to_dict()).encode())
                else:
                    self.send_error(404, 'Personagem não encontrado')
            except ValueError:
                self.send_error(400, 'ID inválido')

    def do_POST(self):
        if self.path == '/characters':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                new_character = Character(None, data['name'], data['skills'], data['age'], data['description'], data['affiliation'])
                added_character = self.repo.add_character(new_character)
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(added_character.to_dict()).encode())
            except json.JSONDecodeError:
                self.send_error(400, 'Erro de formato no corpo da requisição')
