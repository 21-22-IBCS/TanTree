from fitGengraphics import*
from fitGenbutton import*
import time

def main():

    win = GraphWin("Fit Generator", 900, 620)
    win.setBackground("pink")
    #What are you planning to do today?
    Q1text = Text(Point(150,68), "What are you planning to do today?")
    Q1text.draw(win)
    e1 = Entry(Point (150,88), 20)
    e1.draw(win)
    #How do you want to dress today?
    Q2text = Text(Point(380,68), "How do you want to dress today?")
    Q2text.draw(win)
    e2 = Entry(Point (380,88), 20)
    e2.draw(win)
    #Feeling flirty?
    Q3text = Text(Point(600,68), "Feeling flirty?")
    Q3text.draw(win)
    e3 = Entry(Point (600,88), 20)
    e3.draw(win)
    #Weather
    Q4text = Text(Point(800,68), "Weather")
    Q4text.draw(win)
    e4 = Entry(Point (800,88), 20)
    e4.draw(win)
    
    graph1 = Button(win, 'white', "reveal outfit!", Point(150,500), 55)
    graph2 = Button(win, 'white', "reveal outfit!", Point(380,500), 55)
    graph3 = Button(win, 'white', "reveal outfit!", Point(600,500), 55)
    graph4 = Button(win, 'white', "reveal outfit!", Point(800,500), 55)
    
    
    quitButton = Button(win, 'red', "i'm done", Point(800,580), 50)

    while True: #Q1
        m1 = win.getMouse()
        if graph1.isClicked(m1):
            f1 = e1.getText()

            if "School" in f1:
                A1 = Text(Point(150,400), "Wear your uniform")
                A1.draw(win)

            if "Shopping" in f1:
                A2 = Text(Point(150,400), "Sparkly dress")
                A2.draw(win)

            if "Hiking" in f1:
                A3 = Text(Point(150,400), "cargo pants")
                A3.draw(win)
                
            elif "" in f1:
                otherResponseA = Text(Point(150,400), "Didn't get that... try again, babe")
                otherResponseA.draw(win)   
            
        if quitButton.isClicked(m1):
            win.close()
            break


    while True: #Q2
        m2 = win.getMouse()
        if graph2.isClicked(m2):
            f2 = e2.getText()

            if "Fashionista!" in f2:
                B1 = Text(Point(150,200), "Sparkly dress")
                B1.draw(win)

            if "Sleepy" in f2:
                B2 = Text(Point(300,200), "loose sweats")
                B2.draw(win)
   
            if "Simple, but cute" in f2:
                B3 = Text(Point(450,200), "tight sweats")
                B3.draw(win)
                
            elif "" in f2:
                otherResponseB = Text(Point(500,200), "B")
                otherResponseB.draw(win)
                
            
            
        if quitButton.isClicked(m1):
            win.close()
            break

    while True: #Q3
        m3 = win.getMouse()
        if graph3.isClicked(m3):
            f3 = e3.getText()

            if "Fashionista!" in f3:
                C1 = Text(Point(150,200), "Sparkly dress")
                C1.draw(win)

            if "Sleepy" in f3:
                C2 = Text(Point(300,200), "Sparkly dress")
                C2.draw(win)

            
            if "Simple, but cute" in f3:
                C3 = Text(Point(450,200), "blue dress")
                C3.draw(win)
                
            elif "" in f3:
                otherResponseC = Text(Point(500,200), "C")
                otherResponseC.draw(win)
                
            
            
        if quitButton.isClicked(m1):
            win.close()
            break

    while True: #Q4
        m4 = win.getMouse()
        if graph4.isClicked(m4):
            f4 = e4.getText()

            if "Ew, no" in f4:
                D1 = Text(Point(150,200), "Sparkly dress")
                D1.draw(win)

            if "Yessss" in f4:
                D2 = Text(Point(300,200), "Sparkly dress")
                D2.draw(win)

            
            if "Okay, sure" in f4:
                D3 = Text(Point(450,200), "blue dress")
                D3.draw(win)
                
            elif "" in f4:
                otherResponseD = Text(Point(500,200), "D")
                otherResponseD.draw(win)
                
            
            
        if quitButton.isClicked(m1):
            win.close()
            break





    
        
if __name__ == "__main__":
    main()
