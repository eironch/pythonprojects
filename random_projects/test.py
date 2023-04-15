from tkinter import *

r = Tk()

text = """First: abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd\n
Second: abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd\n
Third: abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd\n
Fourth: abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd\n"""


def onConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox('all'))

c = Canvas(r, width=560, height=80)
t = Text(c, width=99, height=9)
t.insert("end", text)
hsb = Scrollbar(r, orient='horizontal', command=c.xview)
vsb = Scrollbar(r, orient='vertical', command=c.yview)
c.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
hsb.grid(row=1, column=0, sticky='esw')
vsb.grid(row=0, column=1, sticky='nes')
c.grid(row=0, column=0, sticky='nesw')

c.create_window((0, 0), window=t, anchor='center')
t.bind('<Configure>', lambda event, canvas=c: onConfigure(c))

r.mainloop()