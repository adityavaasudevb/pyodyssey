# import turtle
# maxi = turtle.Turtle() #object creation
# OR

'''
#learining turtle

from turtle import Turtle, Screen
maxi = Turtle()  #creating an object
print(maxi)
maxi.shape("turtle")
maxi.color('chartreuse3')
maxi.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
'''

# import prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table.align)
table.align = "l"
print(table.align)

print(table)
