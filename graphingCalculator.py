from graphics import*
from Button import*
from math import*

def calcy(f, num):
    if "+" in f:
        l = f.split("+")
        result = calcy(l[0], num) + calcy(l[1], num)
        return result
    elif "-" in f:
        l = f.split("-")
        result = calcy(l[0], num) - calcy(l[1], num)
        return result
    elif "*" in f:
        l = f.split("*")
        result = calcy(l[0], num) * calcy(l[1], num)
        return result
    elif "/" in f:
        l = f.split("/")
        result = calcy(l[0], num) / calcy(l[1], num)
        return result
    elif "^" in f:
        l = f.split("^")
        result = calcy(l[0], num) ** calcy(l[1], num)
        return result
    elif "sqrt(x)" in f:
        return sqrt(num)
    elif "x^2" in f:
        return num**2
    elif "sin(x)" in f:
        return sin(num)
    elif "e^x" in f:
        return e**num
    elif "cos(x)" in f:
        return cos(num)
    elif "tan(x)" in f:
        return tan(num)
    elif "ln(x)" in f:
        if num>0:
            return log(num)
        else:
            return 0
    elif f == "x":
        return num
    else:
        return float(f)

def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(30)
    title2 = Text(Point(400,85), "Enter a function you would like to graph")
    title2.setSize(17)
    #edited: y value of text points to move titles
    #edited: title setSize for proportional size adjustment (to make space for larger graph scope) 
    title.draw(win)
    title2.draw(win)

    yAxis = Line(Point(185,105), Point(185,650))
    yAxis.draw(win)
    xAxis = Line(Point(50,500), Point(750,500))
    #edited: xAxis line points to shift x axis down & elongate y axis
    xAxis.draw(win)

    funText = Text(Point(100,700), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(240,700),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(450,700), 75)
    quitB = Button(win, 'red', "QUIT", Point(600,700), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()

            scale = 50

            points = []
            for i in range(350):
                x = i + 185
                y = 500 - scale*calcy(f,i/scale)
                #edited: above x&y intercepts and range values to adjust graph scale
                points.append(Point(x,y))

            for p in points:
                p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break
                
    

if __name__ == "__main__":
    main()
