import turtle

for length in range(50, 100):
    print(length)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()


# turtle.shape(turtle)
turtle.exitonclick()
# time.sleep(100).