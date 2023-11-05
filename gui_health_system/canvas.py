from tkinter import Tk, Canvas


# creating the root
def create_root():
    root = Tk()
    root.title("HealthCare System")

    # making the canvas not resizable
    root.resizable(False, False)
    root.geometry("700x600")

    return root


# creating the canvas
def create_frame():
    frame = Canvas(root, width=700, height=700)
    # attach the frame to the root
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
