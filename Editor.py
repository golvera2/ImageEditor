from PIL import Image
import tkinter as tk
from tkinter import filedialog

class ImageEditor:
    def __init__(self, master):
        self.master = master
        master.title("Image Editor")
        self.image = None
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Exit", command=self.master.quit)

        edit_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Flip Horizontally", command=self.flip_horizontally)
        edit_menu.add_command(label="Flip Vertically", command=self.flip_vertically)
        edit_menu.add_command(label="Rotate", command=self.rotate_image)

    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[
