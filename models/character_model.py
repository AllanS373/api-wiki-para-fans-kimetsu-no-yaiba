class Character:
    def __init__(self, id, name, skills, age, description, affiliation):
        self.id = id
        self.name = name
        self.skills = skills
        self.age = age
        self.description = description
        self.affiliation = affiliation

    def to_dict(self):
        return self.__dict__