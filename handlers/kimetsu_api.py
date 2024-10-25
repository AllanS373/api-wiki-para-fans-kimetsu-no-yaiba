from http.server import BaseHTTPRequestHandler
import json

# Dados simulados (deveriam ser carregados de arquivos ou um banco de dados)
personagens = [
    {'id': 1, 'nome': 'Tanjiro Kamado', 'habilidades': ['Respiração da Água', 'Respiração do Sol'], 'afiliacao': "Corporação dos Caçadores de Oni's"},
    {'id': 2, 'nome': 'Nezuko Kamado', 'habilidades': ['Sangue Explosivo'], 'afiliacao': "Corporação dos Caçadores de Oni's"}
]

arcos = [
    {'id': 1, 'nome': 'Seleção final'},
    {'id': 2, 'nome': 'Primeira missão'},
    {'id': 3, 'nome': 'Asakusa'},
    {'id': 4, 'nome': 'Mansão Tsuzumi'},
    {'id': 5, 'nome': 'Montanha Natagumo'},
    {'id': 6, 'nome': 'Reabilitação e treinamento'},
    {'id': 7, 'nome': 'Trem infinito'},
    {'id': 8, 'nome': 'Distrito do Entretenimento'},
    {'id': 9, 'nome': 'Vila dos Ferreiros'},
    {'id': 10, 'nome': 'Treinamento dos Hashiras'},
    {'id': 11, 'nome': 'Castelo infinito'},
    {'id': 12, 'nome': 'Contagem regressiva pelo nascer do sol'}
]

class KimetsuAPI(BaseHTTPRequestHandler):
    def buscar_personagem_por_id(self, id):
        for personagem in personagens:
            if personagem['id'] == id:
                return personagem
        return None

    def buscar_arco_por_id(self, id):
        for arco in arcos:
            if arco['id'] == id:
                return arco
        return None

    def do_GET(self):
        if self.path == '/personagens':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(personagens)
            self.wfile.write(response.encode())

        elif self.path.startswith('/personagens/'):
            try:
                personagem_id = int(self.path.split('/')[-1])
            except ValueError:
                self.send_error(400, "ID inválido")
                return

            personagem = self.buscar_personagem_por_id(personagem_id)
            if personagem:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(personagem)
                self.wfile.write(response.encode())
            else:
                self.send_error(404, "Personagem não encontrado")

        elif self.path == '/arcos':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(arcos)
            self.wfile.write(response.encode())

        elif self.path.startswith('/arcos/'):
            try:
                arco_id = int(self.path.split('/')[-1])
            except ValueError:
                self.send_error(400, "ID inválido")
                return

            arco = self.buscar_arco_por_id(arco_id)
            if arco:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(arco)
                self.wfile.write(response.encode())
            else:
                self.send_error(404, "Arco não encontrado")

        else:
            self.send_error(404, "Rota não encontrada")

    def do_POST(self):
        if self.path == '/personagens':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                novo_personagem = json.loads(post_data)
                novo_personagem['id'] = len(personagens) + 1
                personagens.append(novo_personagem)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(novo_personagem)
                self.wfile.write(response.encode())
            except json.JSONDecodeError:
                self.send_error(400, "Erro de formato no corpo da requisição")

        elif self.path.startswith('/personagens/'):
            try:
                personagem_id = int(self.path.split('/')[-1])
            except ValueError:
                self.send_error(400, "ID inválido")
                return

            personagem = next((p for p in personagens if p['id'] == personagem_id), None)
            if personagem is None:
                self.send_error(404, "Personagem não encontrado")
                return

            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                dados_atualizados = json.loads(post_data)
                personagem.update(dados_atualizados)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(personagem)
                self.wfile.write(response.encode())
            except json.JSONDecodeError:
                self.send_error(400, "Erro de formato no corpo da requisição")

        else:
            self.send_error(404, "Rota não encontrada")
