from graphics import *

def draw_sq(sX, sY, color, size, win):
    square = Rectangle(Point(sX, sY),
                       Point(sX + size, sY + size))
    square.setFill(color)
    square.draw(chWin)

print("""Hello user. This program creates a 8x8 checker board. Type the size you'd
want the checker board to be and the color.""")
print()
sqSz = int(input("size > "))
color = str(input("color > "))



chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0,0, sqSz * 10, sqSz * 10)

for m in range(8):
    for i in range(8):
        if (i + m) % 2 == 0:
            sqCol = color
        else:
            sqCol = "black"
        draw_sq(sqSz * (i + 1), sqSz * (m + 1) , sqCol, sqSz, chWin)

chWin.getMouse()
chWin.close()


   
