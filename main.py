from direct.showbase.ShowBase import ShowBase
from map import Map
from player import Player

class Game(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.map = Map()
        self.Player = Player((5,5,3),self.map)


base = Game()




base.run()