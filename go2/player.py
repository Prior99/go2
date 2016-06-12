from marshmallow import Schema, fields

class Player:
    def __init__(self, username):
        self.username = username
