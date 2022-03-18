from springSimgraphics import*

 #image owned by Dreamstime

class youngB():
    def __init__(self, win, p):
        self.pos = p
        self.win = win
        self.im = Image(p, "youngB.png")
        self.im.draw(win)
        
    def getPos(self):
        return self.pos

    def ripeB(self):
        self.im.undraw()
        self.im = Image(self.pos, "ripeB.png")
        self.im.draw(self.win)

