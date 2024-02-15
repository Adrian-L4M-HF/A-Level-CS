import turtle


screen = turtle.Screen()
screen.bgcolor("white")

turtle = turtle.Turtle()
turtle.color("black")
turtle.speed(5)
turtle.penup()
turtle.forward(20)
turtle.left(45)
turtle.pendown()

def one_branch_of_snowflake():  
    for i in range(3):
        for i in range(3):
            turtle.forward(10/3)
            turtle.backward(10/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10)

turtle.penup()
turtle.forward(20)
turtle.left(45)
turtle.pendown()
for i in range(6):
   one_branch_of_snowflake()  
   turtle.left(45)
       


screen.exitonclick()

