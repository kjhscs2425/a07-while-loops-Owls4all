# Use turtle graphics to make an infinite spiral
import turtle as t
t.speed(0)
potato = 'awesome'
angle=2.5
l=0.25
while potato != 'bad':
    t.fd(l)
    t.left(angle)
    l *= 1.002