print("                   Copyright (C) 2022 Joseph McKeown               ")
print("")
print("This program is free software: you can redistribute it and/or modify")
print("it under the terms of the GNU General Public License as published by")
print("the Free Software Foundation, either version 3 of the License, or")
print("(at your option) any later version.")
print("")
print("This program is distributed in the hope that it will be useful,")
print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
print("GNU General Public License for more details.")
print("")
print("You should have received a copy of the GNU General Public License")
print("along with this program.  If not, see <http://www.gnu.org/licenses/>.")
print("")
print("---------------------------------------------------------------------")
print("")
###############################################################################

import tkinter as tk
from PIL import Image, ImageTk
import time, random

### Functions which work on button press, displaying the desired image
### and changing the button's function to the next step
def get_Unlit(some_input):
    global top_canvas, bottom_button, unlit_img, has_burnt
    top_canvas.create_image(0,0,anchor="nw",image=unlit_img)
    top_canvas.update()
    if has_burnt:
        bottom_button["text"] = "Remove the candle."
        bottom_button.bind("<Button 1>", get_BlackScreen)
    else:
        bottom_button["text"] = "Light your candle."
        bottom_button.bind("<Button 1>", get_Burning)

def get_Burning(some_input):
    global top_canvas, bottom_button, burning_img, has_burnt
    top_canvas.create_image(0,0,anchor="nw",image=burning_img)
    top_canvas.update()
    bottom_button["text"] = "Please wait."
    bottom_button.update()
    time.sleep(random.randint(1,10))
    has_burnt = True
    get_Unlit(0)

def get_BlackScreen(some_input):
    global top_canvas, bottom_button, blackscreen_img, has_burnt
    top_canvas.create_image(0,0,anchor="nw",image=blackscreen_img)
    top_canvas.update()
    has_burnt = False
    bottom_button["text"] = "Take a candle."
    bottom_button.bind("<Button 1>", get_Unlit)

### Initialising the root_window
root_window = tk.Tk()
root_window.title("Candle Magic")

### A boolean for keeping images in order
has_burnt = False

### Images to use later
blackscreen_img = ImageTk.PhotoImage((Image.open(f"Black_Screen.jpg")).resize((200,200)))
unlit_img = ImageTk.PhotoImage((Image.open(f"Unlit_Candle.jpg")).resize((200,200)))
burning_img = ImageTk.PhotoImage((Image.open(f"Burning_Candle.jpg")).resize((200,200)))
button_img = tk.PhotoImage(width = 200, height = 50)

### Organising the UI in frames
top_frame = tk.Frame(root_window)
top_frame.pack(side="top")

bottom_frame = tk.Frame(root_window)
bottom_frame.pack(side="bottom")

### Adding a button to move through the candle stages
bottom_button = tk.Button(master = bottom_frame,
                          image = button_img,
                          text = "Take a candle.",
                          compound = "c")
bottom_button.bind("<Button 1>", get_Unlit)
bottom_button.pack()

### Adding a canvas to show the candle images
top_canvas = tk.Canvas(top_frame, width = 200, height = 200)
top_canvas.pack()

### Getting the first image
get_BlackScreen(0)

### Starting the UI mainloop
root_window.mainloop()
