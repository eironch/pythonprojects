import tkinter as tk
from PIL import Image, ImageTk

global is_menu_scroll
global is_checked_out


def main():
    # root
    app = tk.Tk()
    app.title("Tita Karen\'s")
    app.iconbitmap("assets/tita_karens.ico")
    app.resizable(False, False)
    window_width, window_height = 1280, 720
    x_position = (app.winfo_screenwidth() - window_width) // 2
    y_position = (app.winfo_screenheight() - window_height) // 2
    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # imgs
    lechonsilog_img = ImageTk.PhotoImage(Image.open("assets/lechonsilog.png").resize((280, 280), Image.LANCZOS))
    shangsilog_img = ImageTk.PhotoImage(Image.open("assets/shangsilog.png").resize((280, 280), Image.LANCZOS))
    sisilog_img = ImageTk.PhotoImage(Image.open("assets/sisilog.png").resize((280, 280), Image.LANCZOS))
    malingsilog_img = ImageTk.PhotoImage(Image.open("assets/malingsilog.png").resize((280, 280), Image.LANCZOS))
    hamsilog_img = ImageTk.PhotoImage(Image.open("assets/hamsilog.png").resize((280, 280), Image.LANCZOS))
    tapsilog_img = ImageTk.PhotoImage(Image.open("assets/tapsilog.png").resize((280, 280), Image.LANCZOS))
    bangsilog_img = ImageTk.PhotoImage(Image.open("assets/bangsilog.png").resize((280, 280), Image.LANCZOS))
    porksilog_img = ImageTk.PhotoImage(Image.open("assets/porksilog.png").resize((280, 280), Image.LANCZOS))
    hotsilog_img = ImageTk.PhotoImage(Image.open("assets/hotsilog.png").resize((280, 280), Image.LANCZOS))
    chicken_fillet_img = ImageTk.PhotoImage(Image.open("assets/chicken_fillet.png").resize((280, 280), Image.LANCZOS))

    checkout_header_img = ImageTk.PhotoImage(Image.open("assets/checkout_header.png").resize((384, 127), Image.LANCZOS))
    checkout_footer_img = ImageTk.PhotoImage(Image.open("assets/checkout_footer.png").resize((384, 127), Image.LANCZOS))

    increase_img = ImageTk.PhotoImage(Image.open("assets/increase.png").resize((84, 84), Image.LANCZOS))
    decrease_img = ImageTk.PhotoImage(Image.open("assets/decrease.png").resize((84, 84), Image.LANCZOS))
    checkout_img = ImageTk.PhotoImage(Image.open("assets/checkout.png").resize((159, 92), Image.LANCZOS))

    # vars
    orders = []
    is_menu_scroll = False
    order_strings = [
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar()
    ]
    total_string = tk.StringVar()
    total_string.set("PHP 0  ")
    is_checked_out = False
    total_checked_out_string = tk.StringVar()

    # functions
    # changes which scrollbar to scroll
    def change_is_menu_scroll(state):
        global is_menu_scroll

        is_menu_scroll = state

    def on_mouse_wheel(event, menu, order):
        global is_menu_scroll

        # prevents unwanted scrolling
        if is_checked_out:
            return

        if is_menu_scroll:
            if event.num == 5 or event.delta == -120:
                menu.yview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                menu.yview_scroll(-1, "units")
        else:
            if len(orders) >= 5:
                if event.num == 5 or event.delta == -120:
                    order.yview_scroll(1, "units")
                elif event.num == 4 or event.delta == 120:
                    order.yview_scroll(-1, "units")

    # shows orders on the checkout tab by matching corresponding items
    def add_order_frame():
        for order in orders:
            match order["index"]:
                case 0:
                    order_0_frame.pack(fill=tk.BOTH, pady=5)
                case 1:
                    order_1_frame.pack(fill=tk.BOTH, pady=5)
                case 2:
                    order_2_frame.pack(fill=tk.BOTH, pady=5)
                case 3:
                    order_3_frame.pack(fill=tk.BOTH, pady=5)
                case 4:
                    order_4_frame.pack(fill=tk.BOTH, pady=5)
                case 5:
                    order_5_frame.pack(fill=tk.BOTH, pady=5)
                case 6:
                    order_6_frame.pack(fill=tk.BOTH, pady=5)
                case 7:
                    order_7_frame.pack(fill=tk.BOTH, pady=5)
                case 8:
                    order_8_frame.pack(fill=tk.BOTH, pady=5)

    # removes orders on the checkout tab by matching corresponding items
    def remove_order_frame(index):
        match index:
            case 0:
                order_0_frame.pack_forget()
            case 1:
                order_1_frame.pack_forget()
            case 2:
                order_2_frame.pack_forget()
            case 3:
                order_3_frame.pack_forget()
            case 4:
                order_4_frame.pack_forget()
            case 5:
                order_5_frame.pack_forget()
            case 6:
                order_6_frame.pack_forget()
            case 7:
                order_7_frame.pack_forget()
            case 8:
                order_8_frame.pack_forget()

    # update order string to reflect count and cost by matching corresponding items
    def update_strings(order):
        match order["index"]:
            case 0:
                order_strings[0].set(
                    str(order["order_count"]) + "x Lechonsilog \nPHP " +
                    str(order["order_count"] * 65)
                )
            case 1:
                order_strings[1].set(
                    str(order["order_count"]) + "x Shangsilog \nPHP " +
                    str(order["order_count"] * 50)
                )
            case 2:
                order_strings[2].set(
                    str(order["order_count"]) + "x Sisilog \nPHP " +
                    str(order["order_count"] * 65)
                )
            case 3:
                order_strings[3].set(
                    str(order["order_count"]) + "x Malingsilog \nPHP " +
                    str(order["order_count"] * 55)
                )
            case 4:
                order_strings[4].set(
                    str(order["order_count"]) + "x Hamsilog \nPHP " +
                    str(order["order_count"] * 55)
                )
            case 5:
                order_strings[5].set(
                    str(order["order_count"]) + "x Tapsilog \nPHP " +
                    str(order["order_count"] * 70)
                )
            case 6:
                order_strings[6].set(
                    str(order["order_count"]) + "x Bangsilog \nPHP " +
                    str(order["order_count"] * 70)
                )
            case 7:
                order_strings[7].set(
                    str(order["order_count"]) + "x Porksilog \nPHP " +
                    str(order["order_count"] * 60)
                )
            case 8:
                order_strings[8].set(
                    str(order["order_count"]) + "x Hotsilog \nPHP " +
                    str(order["order_count"] * 50)
                )

    # updates total based on ordered items by matching corresponding items
    def update_total_strings():
        total = 0

        for order in orders:
            match order["index"]:
                case 0:
                    total += order["order_count"] * 65
                case 1:
                    total += order["order_count"] * 50
                case 2:
                    total += order["order_count"] * 65
                case 3:
                    total += order["order_count"] * 55
                case 4:
                    total += order["order_count"] * 55
                case 5:
                    total += order["order_count"] * 70
                case 6:
                    total += order["order_count"] * 70
                case 7:
                    total += order["order_count"] * 60
                case 8:
                    total += order["order_count"] * 50

        if total == 0:
            total_string.set("PHP 0  ")
            return

        total_string.set("PHP " + str(total))

    # handles addition of order to the list by matching corresponding item
    def add_order(index):
        checkout_button.configure(state=tk.NORMAL)

        for order in orders:
            if order["index"] == index:
                if order["order_count"] == 20:
                    return

                order["order_count"] += 1

                update_strings(order)
                update_total_strings()

                return

        match index:
            case 0:
                order_strings[0].set(
                    "1x Lechonsilog \nPHP 65"
                )
            case 1:
                order_strings[1].set(
                    "1x Shangsilog \nPHP 50"
                )
            case 2:
                order_strings[2].set(
                    "1x Sisilog \nPHP 65"
                )
            case 3:
                order_strings[3].set(
                    "1x Malingsilog \nPHP 55"
                )
            case 4:
                order_strings[4].set(
                    "1x Hamsilog \nPHP 55"
                )
            case 5:
                order_strings[5].set(
                    "1x Tapsilog \nPHP 70"
                )
            case 6:
                order_strings[6].set(
                    "1x Bangsilog \nPHP 70"
                )
            case 7:
                order_strings[7].set(
                    "1x Porksilog \nPHP 60"
                )
            case 8:
                order_strings[8].set(
                    "1x Hotsilog \nPHP 50"
                )

        orders.append({"index": index, "order_count": 1})
        update_total_strings()
        add_order_frame()

    # increases order count on the checkout tab by finding the item on the list
    def increase_order_count(index):
        for order in orders:
            if order["index"] == index and order["order_count"] < 20:
                order["order_count"] += 1

                update_strings(order)

        update_total_strings()

    # decreases order count on the checkout tab by finding the item on the list
    def decrease_order_count(index):
        for order in orders:
            if order["index"] == index:
                if order["order_count"] == 1:
                    remove_order_frame(order["index"])
                    orders.remove(order)
                    update_total_strings()
                    update_strings(order)

                    if len(orders) == 0:
                        checkout_button.configure(state=tk.DISABLED)

                    return

                order["order_count"] -= 1
                update_total_strings()
                update_strings(order)

    # handles checking out, resetting of variables and clearing of lists
    def check_out():
        if len(orders) == 0:
            return

        global is_checked_out

        is_checked_out = True

        total_checked_out_string.set("Thank you for Ordering!\nPlease Pay at the Counter\nTotal: " + total_string.get())

        total_string.set("PHP 0  ")
        for order in orders:
            remove_order_frame(order["index"])

        orders.clear()

        checkout_button.configure(state=tk.DISABLED)
        checked_out_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # resetting to homepage
    def go_to_homepage(event):
        global is_checked_out

        is_checked_out = False

        checked_out_frame.place_forget()

    # widgets
    # menu
    menu_canvas = tk.Canvas(app, highlightthickness=0, bg="#fdc0b0")
    menu_canvas.place(x=0, y=0, relwidth=0.7, relheight=1)
    menu_canvas.bind("<Enter>", lambda event: change_is_menu_scroll(True))
    menu_canvas.bind("<Leave>", lambda event: change_is_menu_scroll(False))

    menu_grid = tk.Frame(menu_canvas, bg="#fdc0b0")
    menu_grid.bind("<Configure>", lambda e: menu_canvas.config(scrollregion=menu_canvas.bbox("all")))

    menu_canvas.create_window((4, 0), window=menu_grid, anchor="nw")

    menu_v_scrollbar = tk.Scrollbar(menu_canvas, orient=tk.VERTICAL, command=menu_canvas.yview)
    menu_v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    menu_canvas.config(yscrollcommand=menu_v_scrollbar.set)

    # menu buttons
    menu_button_count = 10
    menu_buttons = []
    menu_button_imgs = [
        lechonsilog_img, shangsilog_img, sisilog_img,
        malingsilog_img, hamsilog_img, tapsilog_img,
        bangsilog_img, porksilog_img, hotsilog_img,
        chicken_fillet_img
    ]

    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[0],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(0)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[1],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(1)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[2],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(2)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[3],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(3)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[4],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(4)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[5],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(5)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[6],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(6)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[7],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(7)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[8],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        command=lambda: add_order(8)
    ))
    menu_buttons.append(tk.Button(
        menu_grid, image=menu_button_imgs[9],
        relief="flat", background="#fdc0b0",
        activebackground="#fdc0b0",
        state=tk.DISABLED
    ))

    row = 0
    column = 0
    for i in range(menu_button_count):
        column += 1

        if i % 3 == 0:
            column = 0
            row += 1

        if i == 9:
            column = 1

        menu_buttons[i].grid(row=row, column=column, columnspan=1, padx=1.5, pady=1.5)

    # checkout menu
    checkout_frame = tk.Frame(app, bg="#fde6bc")
    checkout_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    # header
    checkout_header_bg = tk.Label(checkout_frame, image=checkout_header_img, bg="#fde6bc")
    checkout_header_bg.place(x=-2, y=-1)

    order_label = tk.Label(
        checkout_frame, text="Orders", fg="#d97ed0", bg="#fde6bc",
        font=("Roboto", 20, "bold")
    )
    order_label.pack(pady=125)

    # body
    order_canvas = tk.Canvas(checkout_frame, highlightthickness=0, bg="#fde6bc")
    order_canvas.place(y=175, relwidth=1, relheight=0.58)

    order_grid = tk.Frame(order_canvas, bg="#fde6bc")
    order_grid.bind("<Configure>", lambda e: order_canvas.config(scrollregion=order_canvas.bbox("all")))
    order_canvas.create_window((0, 0), window=order_grid, anchor="nw", width=367)

    order_v_scrollbar = tk.Scrollbar(order_canvas, orient=tk.VERTICAL, command=order_canvas.yview)
    order_v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    order_canvas.config(yscrollcommand=order_v_scrollbar.set)

    # order 0
    order_0_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_0_decrease_button = tk.Button(
        order_0_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(0)
    )
    order_0_decrease_button.pack(side=tk.LEFT)

    order_0_text = tk.Label(
        order_0_frame, textvariable=order_strings[0], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_0_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_0_increase_button = tk.Button(
        order_0_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(0)
    )
    order_0_increase_button.pack(side=tk.RIGHT)

    # order 1
    order_1_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_1_decrease_button = tk.Button(
        order_1_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(1)
    )
    order_1_decrease_button.pack(side=tk.LEFT)

    order_1_text = tk.Label(
        order_1_frame, textvariable=order_strings[1], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_1_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_1_increase_button = tk.Button(
        order_1_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(1)
    )
    order_1_increase_button.pack(side=tk.RIGHT)

    # order 2
    order_2_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_2_decrease_button = tk.Button(
        order_2_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(2)
    )
    order_2_decrease_button.pack(side=tk.LEFT)

    order_2_text = tk.Label(
        order_2_frame, textvariable=order_strings[2], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_2_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_2_increase_button = tk.Button(
        order_2_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(2)
    )
    order_2_increase_button.pack(side=tk.RIGHT)

    # order 3
    order_3_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_3_decrease_button = tk.Button(
        order_3_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(3)
    )
    order_3_decrease_button.pack(side=tk.LEFT)

    order_3_text = tk.Label(
        order_3_frame, textvariable=order_strings[3], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_3_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_3_increase_button = tk.Button(
        order_3_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(3)
    )
    order_3_increase_button.pack(side=tk.RIGHT)

    # order 4
    order_4_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_4_decrease_button = tk.Button(
        order_4_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(4)
    )
    order_4_decrease_button.pack(side=tk.LEFT)

    order_4_text = tk.Label(
        order_4_frame, textvariable=order_strings[4], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_4_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_4_increase_button = tk.Button(
        order_4_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(4)
    )
    order_4_increase_button.pack(side=tk.RIGHT)

    # order 5
    order_5_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_5_decrease_button = tk.Button(
        order_5_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(5)
    )
    order_5_decrease_button.pack(side=tk.LEFT)

    order_5_text = tk.Label(
        order_5_frame, textvariable=order_strings[5], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_5_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_5_increase_button = tk.Button(
        order_5_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(5)
    )
    order_5_increase_button.pack(side=tk.RIGHT)

    # order 6
    order_6_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_6_decrease_button = tk.Button(
        order_6_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(6)
    )
    order_6_decrease_button.pack(side=tk.LEFT)

    order_6_text = tk.Label(
        order_6_frame, textvariable=order_strings[6], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_6_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_6_increase_button = tk.Button(
        order_6_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(6)
    )
    order_6_increase_button.pack(side=tk.RIGHT)

    # order 7
    order_7_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_7_decrease_button = tk.Button(
        order_7_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(7)
    )
    order_7_decrease_button.pack(side=tk.LEFT)

    order_7_text = tk.Label(
        order_7_frame, textvariable=order_strings[7], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_7_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_7_increase_button = tk.Button(
        order_7_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(7)
    )
    order_7_increase_button.pack(side=tk.RIGHT)

    # order 8
    order_8_frame = tk.Frame(order_grid, bg="#fde6bc")

    order_8_decrease_button = tk.Button(
        order_8_frame, image=decrease_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: decrease_order_count(8)
    )
    order_8_decrease_button.pack(side=tk.LEFT)

    order_8_text = tk.Label(
        order_8_frame, textvariable=order_strings[8], bg="#fdc0b0",
        fg="white", font=("Roboto", 13, "bold")
    )
    order_8_text.pack(side=tk.LEFT, fill="both", expand=True)

    order_8_increase_button = tk.Button(
        order_8_frame, image=increase_img, relief="flat",
        background="#fdc0b0", activebackground="#fdc0b0",
        command=lambda: increase_order_count(8)
    )
    order_8_increase_button.pack(side=tk.RIGHT)

    # footer
    checkout_footer_frame = tk.Frame(checkout_frame, width=384, height=127, bg="#fde6bc")
    checkout_footer_frame.place(x=-2, y=593)

    checkout_footer_bg = tk.Label(checkout_footer_frame, image=checkout_footer_img, bg="#fde6bc")
    checkout_footer_bg.grid(row=0, column=0, rowspan=10, columnspan=10)

    price_text = tk.Label(
        checkout_footer_frame, fg="#d97ed0", bg="#fde6bc",
        justify="right", textvariable=total_string,
        font=("Roboto", 22, "bold")
    )
    price_text.grid(row=6, column=1, rowspan=1, columnspan=6)

    checkout_button = tk.Button(
        checkout_footer_frame, image=checkout_img, relief="flat",
        background="#fde6bc", activebackground="#fde6bc",  state=tk.DISABLED,
        command=check_out
    )
    checkout_button.grid(row=6, column=9)

    # checked out
    checked_out_frame = tk.Frame(app, bg="#fde6bc")
    checked_out_frame.bind("<Button-1>", go_to_homepage)

    checked_out_text = tk.Label(
        checked_out_frame, bg="#fde6bc", fg="#d97ed0",
        textvariable=total_checked_out_string, font=("Roboto", 24, "bold")
    )
    checked_out_text.bind("<Button-1>", go_to_homepage)
    checked_out_text.pack(pady=290)

    app.bind('<Escape>', lambda event: app.quit())
    app.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, menu_canvas, order_canvas))
    app.mainloop()


if __name__ == "__main__":
    main()
