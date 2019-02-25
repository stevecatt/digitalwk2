from graphics import *
win = GraphWin('Window 1' ,600,600)
pt = Point(300,300)
oval_point = 

ear2 = Point(400,200)
eye2 = Point(250,250)
eye1 = Point(350,250)
ear1 = Point(200,200)


circle = Circle(pt,150)

earcirc1 = Circle(ear1, 50)

earcirc2 = Circle(ear2,50)

eyecirc2 = Circle(eye2,25)

eyecirc1 = Circle(eye1,25)

eyecirc1.setFill("black")
eyecirc2.setFill("black")


earcirc1.setFill("yellow")

earcirc2.setFill("yellow")
circle.setFill("yellow")
earcirc1.setOutline("black")
earcirc2.setOutline("black")
circle.setOutline("black")
earcirc1.draw(win)

earcirc2.draw(win)
circle.draw(win)
eyecirc1.draw(win)
eyecirc2.draw(win)





win.getMouse()
win.close()