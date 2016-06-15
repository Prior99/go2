class PlayerManager:
    def __init__(self):
        self.players = []

    def register(self, username):
        print('New player registered with username ', username)
        self.players.append(username)
