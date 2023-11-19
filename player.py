from direct.actor.Actor import Actor


class Player:
    def __init__ (self,pos,map):
        # self.player = Actor('sours/ralph')
        # self.player.setTexture(loader.loadTexture('ralf.png'))
        self.player = loader.loadModel('smiley')
        self.player.setPos(pos)
        self.player.setColor((0.7,0.5,0.1,0.1))
        self.player.setScale(0.3)
        self.player.reparentTo(render)
        self.map = map