import json
from models.arc_model import Arc

class ArcRepository:
    def __init__(self, filepath='data/arcs.json'):#Construtor
        self.filepath = filepath
    
    def load_arcs(self):#Carregar Arcos
        with open(self.filepath, 'r') as file: #'r' reading(leitura)
            data = json.load(file)
            return [Arc(**arc) for arc in data]
    
    def save_arcs(self, arcs):#Salvar Arcos
        with open(self.filepath, 'w') as file: # 'w' writing(escrita)
            json.dump([arc.to_dict() for arc in arcs], file, indent=4)

    def find_by_id(self, id):#Buscar por ID
        arcs = self.load_arcs()
        for arc in arcs:
            if arc.id == id:
                return arc
        return None
    
    def add_arc(self, arc):#Adicionar Arco
        arcs = self.load_arcs()
        arc.id = len(arcs) + 1
        arcs.append(arc)
        self.save_arcs(arcs)
        return arc