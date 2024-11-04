import json
from models.character_model import Character

class CharacterRepository:
    def __init__(self, filepath='data/characters.json'):#Construtor
        self.filepath = filepath
    
    def load_characters(self):#Carregar Personagens
        with open(self.filepath, 'r') as file: #'r' reading(leitura)
            data = json.load(file)
            return [Character(**char) for char in data]
    
    def save_characters(self, characters):#Salvar Personagens
        with open(self.filepath, 'w') as file: # 'w' writing(escrita)
            json.dump([char.to_dict() for char in characters], file, indent=4)

    def find_by_id(self, id):#Buscar por ID
        characters = self.load_characters()
        for char in characters:
            if char.id == id:
                return char
        return None
    
    def add_character(self, character):#Adicionar Personagem
        characters = self.load_characters()
        character.id = len(characters) + 1
        characters.append(character)
        self.save_characters(characters)
        return character