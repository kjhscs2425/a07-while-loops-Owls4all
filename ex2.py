# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle as t
potato = 'great'
x=1
t.up()
while potato != 'bad':
    t.goto([0,-1*x])
    t.down()
    t.circle(x)
    t.up()
    x+=5
