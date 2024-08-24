import turtle as turtle_module
import random
from tkinter import Tk, Scale, Button, HORIZONTAL, colorchooser

# Set up the turtle module and screen
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Define the color palette
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), 
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Set the background color
screen = turtle_module.Screen()

# Function to draw a dot painting with given parameters
def draw_hirst_painting(dot_size):
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for row in range(rows):
        for col in range(cols):
            tim.dot(dot_size, random.choice(color_list))
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50 * cols)
        tim.setheading(0)

# Function to prompt user for dot size and background color
def prompt_for_dot_size_and_bg_color():
    global dot_size
    global bg_color

    def on_confirm():
        global dot_size
        global bg_color
        dot_size = int(dot_size_slider.get())
        screen.bgcolor(bg_color)  # Set the background color of the turtle screen
        root.destroy()  # Close the Tkinter window
        draw_hirst_painting(dot_size)  # Start painting after Tkinter window is closed

    def pick_color():
        global bg_color
        color_code = colorchooser.askcolor(title="Choose Background Color")[1]
        if color_code:
            bg_color = color_code

    root = Tk()
    root.title("Hirst Painting Setup")

    # Create controls for dot size and background color
    dot_size_slider = Scale(root, from_=10, to_=50, orient=HORIZONTAL, label="Dot Size")
    dot_size_slider.pack()

    color_picker_button = Button(root, text="Pick Background Color", command=pick_color)
    color_picker_button.pack()

    confirm_button = Button(root, text="Start Painting", command=on_confirm)
    confirm_button.pack()

    root.mainloop()

# Fixed grid size and prompt for dot size and background color
rows = 10
cols = 10
bg_color = "#FFFFFF"  # Default background color
prompt_for_dot_size_and_bg_color()  # Prompt the user for the dot size and background color

# Keeps the window open after painting is complete
screen.mainloop()
