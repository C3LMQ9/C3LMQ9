'''Rajzol egy 150 pontos
egyenlő szárú háromszöget a képernyő közepére
A színe legyen piros
A rajzolás induljon a h betűre
Kilépés legyen a q betűre'''
import turtle
import math

def  rajzol():
    turtle.penup()
    oldal = 150
    magassag = math.sqrt(3) / 2 * oldal
    turtle.goto(-oldal / 2, -magassag / 3)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.pensize(5)
    for _ in range(3):
        turtle.forward(oldal)
        turtle.left(120)


    pass

turtle.hideturtle()
ablak = turtle.Screen()
turtle.dot(10, 'black')
turtle.listen()
turtle.onkey(turtle.bye, 'Escape')
turtle.onkey(rajzol, 'h')
turtle.bgcolor("white")
turtle.mainloop()