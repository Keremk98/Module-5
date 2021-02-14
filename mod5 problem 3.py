Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
>>> alex = turtle.Turtle()
>>> 
>>> sides = input ("Number of sides in polygon?")
Number of sides in polygon?
>>> length = input ("Length of the sides in polygon?")
Length of the sides in polygon?
>>> colorname = input ("COlor of polygon?")
COlor of polygon?
>>> fcolor = input ("Fill color of polygon?")
Fill color of polygon?
>>> alex.color = (colorname)
>>> alex.fillcolor = (fcolor)
>>> 
>>> for i in range(int(sides)):
	alex.forward (int(length))
	alex.left (int(360)/int(sides))

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for i in range(int(sides)):
ValueError: invalid literal for int() with base 10: ''
>>> 