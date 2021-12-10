import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(5)

col=['yellow', 'blue', 'white', 'green']
c=0

for i in range(50):
    t.forward(i*20)
    t.right(200)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1

        