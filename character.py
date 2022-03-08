from graphics import*
from Button import*
#from fiddleWithCube import*

def main():

    win = GraphWin("Character Creator", 800, 600)

    l = Line(Point(0,0),Point(400,300))
    l.draw(win)
    
    c2 = Circle(Point(200,400),130)
    c2.draw(win)
    c2.setFill('pink')
    #c2 with a greater diameter than c, is larger, then chronologically, goes before (under) 'c'
    c = Circle(Point(200,400),120)
    c.draw(win)
    #c.setFill(yellow) made the red rectangle, triangle, and the southwest-facing line
    #c.setfill("yellow") ^^same results
    c.setFill('yellow')#WORKED
    c3 = Circle(Point(150,360),25)
    c3.draw(win)
    c3.setFill('orange')
    c3a = Circle(Point(150,360),15)
    c3a.draw(win)
    c3a.setFill('black')
    c3b = Circle(Point(157,350),8)
    c3b.draw(win)
    c3b.setFill('white')
    c4 = Circle(Point(250,360),25)
    c4.draw(win)
    c4.setFill('orange')
    c4a = Circle(Point(250,360),15)
    c4a.draw(win)
    c4a.setFill('black')
    c3b = Circle(Point(257,350),8)
    c3b.draw(win)
    c3b.setFill('white')

    o = Oval(Point(550,400),Point(650,450))
    o.draw(win)
    o.setFill('blue')
    #made o.set fill to try and see it, doesn't seem to appear w/ or w/o color

    r = Rectangle(Point(550,400),Point(650,450))
    r.draw(win)
    r.setFill("red")

    l2 = Line(Point(600,400),Point(545,300))
    l2.draw(win)

    c5 = Circle

    p = Polygon(Point(200,0),Point(250, 50), Point(153,114))
    p.draw(win)
    p.setFill('purple')
    p2 = Polygon(Point(259,59),Point(315, 101), Point(153,115))
    #messed with p2 Point values to warp triangle how i wanted
    #Polygon points go clockwise//distance formula/triangle equations do not work to measure proportional triangles because the triangle is seen at an angle and not headon/birdseye view 
    p2.draw(win)
    p2.setFill('purple')
    p3 = Polygon(Point(300,130),Point(290,104), Point(153,116))
    #Polygon Point values are in XY coordiates
    p3.draw(win)
    p3.setFill('#63087a')
    #hex color values work yay!
    p4 = Polygon(Point(250, 50),Point(153, 114),Point(250, 30))
    p4.draw(win)
    p4.setFill('purple')
    p5 = Polygon(Point(260, 59),Point(153, 114),Point(260, 40))
    p5.draw(win)
    p5.setFill('purple')
    p5.draw(win)
    p5.setFill('purple')

    li = []
    for i in range(5):
        li.append(Point(300 + i*50, 200 - i*50))
                  
    p2 = Polygon(li)
    p2.draw(win)
    
#fun code found online, i got it to run in this program using 'from file import', tying to make them run in the same window
    #import the turtle modules 
    import turtle 
      
    # Forming the window screen
    #tut = turtle.Screen()
      
    # background color green
    #tut.bgcolor("green")
      
    # window title Turtle
    #tut.title("Turtle")
    my_pen = turtle.Turtle()
      
    # object color
    my_pen.color("orange")
    tut = turtle.Screen()           
      
    # forming front square face
    for i in range(4):
        my_pen.forward(100)
        my_pen.left(90)
      
    # bottom left side
    my_pen.goto(50,50)
      
    # forming back square face
    for i in range(4):
        my_pen.forward(ArithmeticError00)
        my_pen.left(90)
  
    # bottom right side
    my_pen.goto(150,50)
    my_pen.goto(100,0)
      
    # top right side
    my_pen.goto(100,100)
    my_pen.goto(150,150)
      
    # top left side
    my_pen.goto(50,150)
    my_pen.goto(0,100)



if __name__ == "__main__":
    main()
