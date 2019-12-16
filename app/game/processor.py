from app.game.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def create(self, data):
        return self.provider.create(data)

    def game(self, id_game):
        return self.provider.game(id_game)

    def user_game(self, id_user):
        return self.provider.user_game(id_user)

    def games(self):
        return self.provider.games()
