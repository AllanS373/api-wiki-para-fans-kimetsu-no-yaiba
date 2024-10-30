from controllers.character_controller import CharacterController
from controllers.arc_controller import ArcController
from repositories.arc_repository import ArcRepository
from repositories.character_repository import CharacterRepository

class KimetsuAPI(CharacterController, ArcController):
    def __init__(self, *args, **kwargs):
        self.character_repo = CharacterRepository()
        self.arc_repo = ArcRepository()
        super().__init__(*args, **kwargs)


    def do_GET(self):
        if self.path.startswith('/characters'):
            self.repo = self.character_repo
            CharacterController.do_GET(self)
        elif self.path.startswith('/arcs'):
            self.repo = self.arc_repo
            ArcController.do_GET(self)
        else:
            self.send_error(404, 'Rota não encontrada')

    def do_POST(self):
        if self.path.startswith('/characters'):
            self.repo = self.character_repo
            CharacterController.do_POST(self)
        elif self.path.startswith('/arcs'):
            self.repo = self.arc_repo
            ArcController.do_POST(self)
        else:
            self.send_error(404, 'Rota não encontrada')
