class Map():
    def __init__(self):
        self.block_sours = 'sours/block.egg'
        self.texture_sours = 'sours/stone.png'
        self.add_stick()
        for x in range(15):
            for y in range(10):
                self.add_block((x,y,0))
        self.add_block((0,10,0))

    def add_block(self,pos):
        self.model = loader.loadModel(self.block_sours)
        self.texture = loader.loadTexture(self.texture_sours)
        self.model.setTexture(self.texture)
        self.model.setPos(pos)
        # self.model.reparentTo(render)
        self.model.reparentTo(self.stick)

    def add_stick(self):
        self.stick = render.attachNewNode('stickNI')