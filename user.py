class User:
    def __init__(self, id, name, job):
        self.id = id
        self.name = name
        self.job = job

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'job': self.job}
