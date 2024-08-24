# Hirst Painting

## Description

The Hirst Painting project is a Python application that uses the Turtle graphics library to create a dot painting inspired by the artist Damien Hirst. The program allows users to customize the painting by selecting dot size and background color through a graphical user interface (GUI) built with Tkinter.

## Features

- ***Customizable Dot Size:*** Users can select the dot size using a slider.
- ***Background Color Selection:*** Users can choose a background color using a color picker.
- ***Interactive Painting:*** Users can click on the painting to change the dot colors.

## Installation

1. Ensure you have Python installed on your machine. This project is compatible with Python 3.x.
2. Clone the repository:
   ```bash
   git clone https://github.com/ZayanMalick/Hirst_Painting.git
3. Navigate to the project directory:
   ```bash
   cd Hirst_Painting
4. Install any required dependencies (Tkinter and Turtle should be included with standard Python installations).

## Usage:
1. Run the main.py script: 

        python main.py

2. A Tkinter window will open, prompting you to select the dot size and background color.

3. Use the slider to adjust the dot size and the color picker to select the background color.

4. Click "Start Painting" to generate the dot painting.

## Code Explanation:
### Imports:
- ***turtle_module*** for drawing.
- ***random*** for selecting colors randomly.
- ***Tk*** and related modules from tkinter for the GUI.
  
### Color Palette:
  A predefined list of RGB tuples used for the painting.
  
### Functions:
***draw_hirst_painting(dot_size)***: Draws the painting using the specified dot size.

***prompt_for_dot_size_and_bg_color()***: Opens a Tkinter window to allow users to set parameters for the painting.

## Contributing:
Feel free to submit issues or pull requests if you find bugs or have improvements to suggest.

## License:
This project is licensed under the MIT License. See the LICENSE file for details.
