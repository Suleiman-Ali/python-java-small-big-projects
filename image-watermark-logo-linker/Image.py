import tkinter
from tkinter import simpledialog
import PIL.Image
import tkinter.messagebox


class Image:
    def __init__(self):
        self.img = ""
        self.window = tkinter.Tk()
        self.window.title("GUI")
        self.window.config(padx=20, pady=20)
        self.text = tkinter.Label(self.window,text="Welcome", font=("Courier", 20)).grid(column=0, row=0)
        self.image_button = tkinter.Button(self.window, text="Add image", font=("Courier", 12), command=self.add_image).grid(column=1, row=0)
        self.canvas = tkinter.Canvas(self.window, width=300, height=300)
        # self.canvas.pack()
        self.mainloop = self.window.mainloop()

    def add_image(self):
        image_path = simpledialog.askstring(title="Image path", prompt="Enter your image path:")
        logo_path = simpledialog.askstring(title="Logo/Watermark path", prompt="Enter your Logo/Watermark path:")
        base_image = PIL.Image.open(image_path)
        logo = PIL.Image.open(logo_path)
        x_position = int(simpledialog.askstring(title="X position:", prompt="Enter x position: "))
        y_position = int(simpledialog.askstring(title="Y position:", prompt="Enter y position: "))
        base_image.paste(logo, (x_position, y_position))
        base_image.save("output.png")
        tkinter.messagebox.showinfo("Image saved", "Your image saved as 'output.png'")
        self.window.quit()
