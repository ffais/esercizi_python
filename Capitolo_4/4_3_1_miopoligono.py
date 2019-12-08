import turtle

def quadrato(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

bob=turtle.Turtle()
print(bob)
quadrato(bob)
turtle.mainloop()
