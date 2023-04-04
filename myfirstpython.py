# https://docs.python.org/3/library/turtle.html


# print is a built in python function that prints the string argument in the terminal
print("hello world")

# import the turtle library (libraries are code we can use that we didn't write*
from turtle import *
# specfies that it is an image
color('pink', 'black')
# color command specifies what colors to use
begin_fill()
# initiates the program
while True:
    # allows the drawing to stick its origin
    forward(2)
    # forward command gives the directon of the drawing and the number of pixels it goes
    left(1)
    # left command gives the directon of the drawing and the number of pixels it goes
    if abs(pos()) < 1:
        break
    # when the line reaches its origin and is less than one pixel away from it then it breaks
end_fill()
# once it breaks the whole object is filled in
done()
# done.