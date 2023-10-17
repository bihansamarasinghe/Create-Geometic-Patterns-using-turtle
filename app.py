import turtle  # Import the turtle graphics library

turtle.bgcolor('black')  # Set the background color to black

t = turtle.Turtle()  # Create a turtle object named 't'

colors = ['red', 'dark red']  # Define a list of colors

# Loop that iterates 400 times
for number in range(400):
    t.forward(number + 1)  # Move the turtle forward by 'number+1' units
    t.right(89)  # Turn the turtle right by 89 degrees
    t.pencolor(colors[number % 2])  # Set the pen color based on whether 'number' is even or odd

turtle.done()  # Finish and close the turtle graphics window
