from springSimgraphics import*


class youngA():
    def __init__(self, win, p):
        self.pos = p
        self.win = win
        self.im = Image(p, "youngA.png")
        self.im.draw(win)
        
    def getPos(self):
        return self.pos

    def ripeA(self):
        self.im.undraw()
        self.im = Image(self.pos, "ripeA.png")
        self.im.draw(self.win)
