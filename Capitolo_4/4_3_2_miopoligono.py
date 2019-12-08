import turtle

def quadrato(t,lung):
    for i in range(4):
        t.fd(lung)
        t.lt(90)
dim=200
bob=turtle.Turtle()
print(bob)
quadrato(bob,dim)
turtle.mainloop()
