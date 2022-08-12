import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def edit_image():
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    width, height = img.size
    draw = ImageDraw.Draw(img)

    # get watermark text and work with it
    inp = text.get(1.0, "end-1c")
    text_font = ImageFont.truetype('arial.ttf', 62)
    text_width, text_height = draw.textsize(inp, text_font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), inp, font=text_font)
    img.show()

    # Save watermarked image
    image_name = filename.split("/")[-1]
    img.save(f'images/{image_name}')


window = tk.Tk()
window.title("Watermark Creator")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

# add label with instruction
label = tk.Label(text="Insert your watermark text")
label.pack()

# add text box to insert watermark text
text = Text(window, height=1, width=25)
text.pack()

# select file to edit
button = tk.Button(window, text='Open', command=edit_image)
button.pack()


window.mainloop()
