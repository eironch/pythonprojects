from tkinter import *
from PIL import ImageTk,Image

def main():
    root = Tk()
    root.title("Image Viewer")
    root.iconbitmap('picture.ico')
    global image_index
    image_index = 0

    img1 = ImageTk.PhotoImage(Image.open("images/1.png").resize((512, 512), Image.LANCZOS))
    img2 = ImageTk.PhotoImage(Image.open("images/2.gif").resize((512, 512), Image.LANCZOS))
    img3 = ImageTk.PhotoImage(Image.open("images/3.png").resize((512, 512), Image.LANCZOS))
    img4 = ImageTk.PhotoImage(Image.open("images/4.png").resize((512, 512), Image.LANCZOS))
    img5 = ImageTk.PhotoImage(Image.open("images/5.png").resize((512, 512), Image.LANCZOS))
    img6 = ImageTk.PhotoImage(Image.open("images/6.png").resize((512, 512), Image.LANCZOS))
    img7 = ImageTk.PhotoImage(Image.open("images/7.gif").resize((512, 512), Image.LANCZOS))
    img8 = ImageTk.PhotoImage(Image.open("images/8.png").resize((512, 512), Image.LANCZOS))
    img9 = ImageTk.PhotoImage(Image.open("images/9.png").resize((512, 512), Image.LANCZOS))
    img10 = ImageTk.PhotoImage(Image.open("images/10.png").resize((512, 512), Image.LANCZOS))
    img11 = ImageTk.PhotoImage(Image.open("images/11.png").resize((512, 512), Image.LANCZOS))
    img12 = ImageTk.PhotoImage(Image.open("images/12.png").resize((512, 512), Image.LANCZOS))

    image_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]

    global label
    global status

    status = Label(root, text="Image "  + str(image_index + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    label = Label(root, image=image_list[image_index])
    label.grid(row=0, column=0, columnspan=3)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def button_backwards(len):
        global image_index
        global label
        global status

        if image_index != 0:
            image_index -= 1
        else:
            image_index = len - 1

        status.grid_forget()
        label.grid_forget()
        status = Label(root, text="Image " + str(image_index + 1)+ " of " + str(len), bd=1, relief=SUNKEN, anchor=E)
        label = Label(image=image_list[image_index])
        label.grid(row=0, column=0, columnspan=3)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def button_forwards(len):
        global image_index
        global label
        global status

        if image_index != len - 1:
            image_index += 1
        else:
            image_index = 0

        status.grid_forget()
        label.grid_forget()
        status = Label(root, text="Image " + str(image_index + 1) + " of " + str(len), bd=1, relief=SUNKEN, anchor=E)
        label = Label(image=image_list[image_index])
        label.grid(row=0, column=0, columnspan=3)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    button_back = Button(root, text="<<", command=lambda: button_backwards(len(image_list)))
    button_quit = Button(root, text="Quit", command=root.quit)
    button_forward = Button(root, text=">>", command=lambda: button_forwards(len(image_list)))

    button_back.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2, pady=10)

    root.mainloop()


if __name__== "__main__":
    main()