from werkzeug.security import generate_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def to_dict(self):
        return {"username": self.username, "password": self.password}