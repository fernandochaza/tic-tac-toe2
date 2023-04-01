import sys
import tkinter as tk
import ttkbootstrap as ttk

# Create the main window
window = tk.Tk()

# Get the project directory and display the window icon
project_path = sys.argv[0]
icon_path = project_path.replace('main.py', 'tic-tac-toe.ico')

try:
    window.iconbitmap('tic-tac-toe.ico')
except tk.TclError as incorrect_path:
    print(f"Error: could not find icon file '{icon_path}'")
    pass

# Get the screen size to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size
window_height = 800
window_width = 800

# Get the top-left corner of the window to center it
left = int(screen_width / 2 - window_width / 2)
top = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{left}+{top}")

window.mainloop()