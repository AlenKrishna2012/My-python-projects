import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Pattern")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest speed
spiral_turtle.width(2)

# Function to draw a colorful spiral pattern
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
    
    for i in range(360):
        spiral_turtle.pencolor(colors[i % len(colors)])  # Change color
        spiral_turtle.forward(i * 2)  # Move forward
        spiral_turtle.right(59)  # Turn right

# Draw the spiral
draw_spiral()

# Hide the turtle and finish
spiral_turtle.hideturtle()

# Close the turtle graphics window on click
screen.exitonclick()