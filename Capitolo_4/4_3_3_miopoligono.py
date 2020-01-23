import turtle

def poligono(t,lung,nlati):
    gradi = 360 / nlati
    for i in range(nlati):
        t.fd(lung)
        t.lt(gradi)
dim=200
lati=7
bob=turtle.Turtle()
print(bob)
poligono(bob,dim,lati)
turtle.mainloop()
