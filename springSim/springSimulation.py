from springSimgraphics import*
from figA import*
from figB import* 
from figTree import*
from waspA import*
from waspB import*
import time
#from youngA import* deleted no longer working; good.

def main():

    win = GraphWin("Spring Simulator", 800, 600)
    tree = figTree(win, Point(400,300))
    yA = youngA(win, Point(100,300))#working
    yA2 = youngA(win, Point(300,100))#working
    yA3 = youngA(win, Point(600,250))#working
    yA4 = youngA(win, Point(400,300))#working
    listyA = [yA.getPos(), yA2.getPos(), yA3.getPos(), yA4.getPos()]
    listFigA = [yA, yA2, yA3, yA4]
    
    yB = youngB(win, Point(400, 440))
    yB2 = youngB(win, Point(100, 150))
    yB3 = youngB(win, Point(500, 100))
    yB4 = youngB(win, Point(700, 500))
    listyB = [yB.getPos(), yB2.getPos(), yB3.getPos(), yB4.getPos()]
    listFigB = [yB, yB2, yB3, yB4]
    
    wA = waspA(win)
    wA2 = waspA(win)
    wA3 = waspA(win)
    wA4 = waspA(win)
    wB = waspB(win)
    wB2 = waspB(win)
    wB3 = waspB(win)
    wB4 = waspB(win)
    
    #flying and checks for groupA
    for i in range(75):
        time.sleep(.01)
        wA.fly()
        wA2.fly()
        wA3.fly()
        wA4.fly()
        wB.fly()
        wB2.fly()
        wB3.fly()
        wB4.fly()
        #interaction A check below
        checkA = wA.checkFigA(listyA)
        if checkA < 4:
            print("wA found a fig!")
        checkA2 = wA2.checkFigA(listyA)
        if checkA2 < 4:
            print("wA2 found a fig!")
        checkA3 = wA3.checkFigA(listyA)
        if checkA3 < 4:
            print("wA3 found a fig!")
        checkA4 = wA4.checkFigA(listyA)
        if checkA4 < 4:
            print("wA4 found a fig!")

            
        #if wB.checkFigB(yB.getPos()):
            #print("wB found yB!")

        #to ripen yA....
        if checkA < 4:
            listFigA[checkA].ripeA()
            print("wA got fig this task works")
        if checkA2 < 4:
            listFigA[checkA2].ripeA()
            print("wA2 got fig this task works")
        if checkA3 < 4:
            listFigA[checkA3].ripeA()
            print("wA3 got fig this task works")
        if checkA4 < 4:
            listFigA[checkA4].ripeA()
            print("wA4 got fig this task works")

        #to check yB
        checkB = wB.checkFigB(listyB)
        if checkB < 4:
            print("wB found a fig!")
        checkB2 = wB2.checkFigB(listyB)
        if checkB2 < 4:
            print("wB2 found a fig!")
        checkB3 = wB3.checkFigB(listyB)
        if checkB3 < 4:
            print("wB3 found a fig!")
        checkB4 = wB4.checkFigB(listyB)
        if checkB4 < 4:
            print("wB4 found a fig!")

        #to ripen yB....
        if checkB < 4:
            listFigB[checkB].ripeB()
            print("wA got fig this task works")
        if checkB2 < 4:
            listFigB[checkB2].ripeB()
            print("wA2 got fig this task works")
        if checkB3 < 4:
            listFigB[checkB3].ripeB()
            print("wA3 got fig this task works")
        if checkB4 < 4:
            listFigB[checkB4].ripeB()
            print("wA4 got fig this task works")

    

if __name__ == "__main__":
    main()
