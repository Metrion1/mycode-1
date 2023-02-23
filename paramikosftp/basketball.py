import turtle

# Create a turtle object
basketball = turtle.Turtle()

# Set the color of the turtle to orange
basketball.color("orange")

# Set the shape of the turtle to circle
basketball.shape("circle")

# Set the size of the turtle to resemble a basketball
basketball.shapesize(stretch_wid=1.5, stretch_len=1)

# Draw the basketball
basketball.penup()
basketball.goto(0, 0)
basketball.pendown()

# Hide the turtle
basketball.hideturtle()

# Exit the turtle graphics window when clicked
turtle.exitonclick()

