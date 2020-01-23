import turtle
import math

def cerchio (t, r):
    circonferenza = 2 * math.pi * r
    n = 50
    lunghezza = circonferenza / n
    poligono(t, lunghezza, n)

def poligono(t,lung,nlati):
    gradi = 360 / nlati
    for i in range(nlati):
        t.fd(lung)
        t.lt(gradi)
dim=200
lati=7
bob=turtle.Turtle()
print(bob)
cerchio(bob, 200)
turtle.mainloop()
