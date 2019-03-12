from graphics import *

def draw_sq(sX, sY, color, size, win):
    square = Rectangle(Point(sX, sY),
                       Point(sX + size, sY + size))
    square.setFill(color)
    square.draw(chWin)
    
sqSz = 50



chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0,0, sqSz * 10, sqSz * 10)

draw_sq(sqSz, sqSz, "red", sqSz, chWin)

chWin.getMouse()
chWin.close()


   
