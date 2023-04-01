import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

def main():
    root = Tk()
    root.title('File Opener')

    os.getcwd()
    os.chdir('../')
    initial_dir = os.getcwd()

    def open_image():
        global chosen_image

        root.filename = filedialog.askopenfilename(
            initialdir=initial_dir + "/image_viewer/images",
            title="Select an Image",
        )
        chosen_image = ImageTk.PhotoImage(Image.open(root.filename).resize((512, 512), Image.LANCZOS))
        label = Label(image=chosen_image).pack()

    button = Button(text="Open Image", command=open_image).pack()

    mainloop()


if __name__ == "__main__":
    main()