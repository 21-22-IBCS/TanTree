from springSimgraphics import*
import random

class waspB():
    def __init__(self, win): #waspB should appear
        p = Point(random.randint(0,500),random.randint(0,500))
        self.pos = p
        self.win = win
        self.im = Image(p, "waspB.png")
        self.im.draw(win)
        
    def fly(self): #flying should works
        xDir = random.choice([-2,0,2])
        yDir = random.choice([-2,0,2])
        self.pos.move(20*xDir, 20*yDir)
        self.im.move(20*xDir, 20*yDir)
        
    def checkFigB(self, points):
        for i in range (len(points)):
            fpoint = points[i]
            x = self.pos.getX()
            y = self.pos.getY()
            xMin = fpoint.getX() - 50
            yMin = fpoint.getY() - 50
            xMax = fpoint.getX() + 50
            yMax = fpoint.getY() + 50
            if x > xMin:
                if y > yMin:
                    if x < xMax:
                        if y < yMax:
                            #fig is found
                            self.disappear()
                            return i
        return 4

    def disappear(self):
        self.im.undraw()
        self.pos = Point(-1000,-1000)

