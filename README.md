1.Imports:
Tkinter is used for creating the GUI.
PhotoImage from tkinter is used to handle image files.
2.Initialization:
A Tkinter window is initialized with the title "Calculator".
The window size is set to 410x440 pixels and positioned at coordinates (200, 100).
The window is set to be non-resizable.
The background color of the window is set to a shade of green.
3.Global Variables: 
A global variable equation is initialized to an empty string to store the user input.
4.Functions:
show(value): Appends the provided value to the equation and updates the display.
clear(): Clears the equation and updates the display.
det(): Removes the last character from equation and updates the display.
calculate(): Evaluates the equation and displays the result. Handles errors and displays "error" if any.
Calculator Icon: Sets the window icon using an image file named "calculator.png".
Display Label: A label widget is created to display the current equation or result. It's placed at the top of the window.
Buttons:Various buttons are created for numbers (0-9), operators (+, -, *, /, %), clear (C), delete (DEL), decimal point (.), and equals (=).
Each button has its own command associated with it which calls the respective function (show, clear, det, calculate) when clicked.
The buttons are positioned using the place() method.
Main Loop: This starts the Tkinter event loop, which listens for events (like button clicks) and updates the GUI accordingly.
