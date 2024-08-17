from pathlib import Path
from tkinter import *
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

#Change the path with yours
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/sajandeepsingh/Desktop/student_management_system/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Login functionality
def login():
    if entry_1.get()=='' or entry_2.get()=='':
        messagebox.showerror("ERROR","Fiels can not be empty!")
    elif entry_1.get()=="admin" and entry_2.get()=="student":
        # messagebox.showinfo('Success','Click OK to continue')
        window.destroy()
        import student
    else:
        messagebox.showerror('ERROR',"Incorrect details")

#GUI
window = Tk()
window.title("Student Management System - sajandeep9812")
window.geometry("950x600")
window.configure(bg = "#403F8E")


canvas = Canvas(
    window,
    bg = "#403F8E",
    height = 600,
    width = 950,
    bd = 0,
    highlightthickness = 0, 
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    564.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    171.0,
    278.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    592.0,
    125.0,
    image=image_image_3
)

# userid input field

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    616.0,
    295.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=398.0,
    y=272.0,
    width=436.0,
    height=44.0
)

# password entery field

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    616.0,
    399.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=398.0,
    y=376.0,
    width=436.0,
    height=44.0
)

canvas.create_text(
    400.0,
    251.0,
    anchor="nw",
    text="USER ID:",
    fill="#000000",
    font=("InknutAntiqua Bold", 16 * -1)
)

canvas.create_text(
    400.0,
    355.0,
    anchor="nw",
    text="PASSWORD:",
    fill="#000000",
    font=("InknutAntiqua Bold", 16 * -1)
)

#login button

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,

    command=login,
)
button_1.place(
    x=481.0,
    y=459.0,
    width=270.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
