from turtle import*
import colorsys
y=1
h=0.0
hideturtle()
bgcolor("black")
pensize(2)
def pok():
	c=colorsys.hsv_to_rgb(h,1,1)
	pencolor(c)
	circle(y)
	left(120)
	
for x in range(3600):
	pok()
	h+=0.005
	y+=1
	
	speed(500)