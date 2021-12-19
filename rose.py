import turtle

t = turtle.Turtle()
s = turtle.Screen ()

s.bgcolor('black')
t.pencolor('orange')
t.speed(0)

for i in range (150):
    t.circle(190-1, 90)
    t.lt(98)
    t.circle(190-1, 90)
    t.lt(18)