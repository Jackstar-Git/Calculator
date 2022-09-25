import math
import math as m
import sys
from tkinter import *

window = Tk()
window.title('Calculator')
window.minsize(384, 254)

frame = Frame(window, bg="grey", padx=10, pady=5)
frame.pack()

text = Text(frame, relief=FLAT, height=3, width=45, state="disabled")
text.grid(column=0, row=0, columnspan=4)

pi = m.pi
euler = m.e
calculation = ""
EPSILON = sys.float_info.epsilon


class FixNumber:

    @staticmethod
    def down(n, x=10):
        return math.floor((n + EPSILON) * (10 ** x)) / (10 ** x)

    @staticmethod
    def up(n, x=10):
        return math.ceil((n + EPSILON) * (10 ** x)) / (10 ** x)

    @staticmethod
    def near(n, x=10):
        return round((n + EPSILON) * (10 ** x)) / (10 ** x)


def evaluate():
    global calculation
    text.config(state="normal")
    try:
        x = FixNumber.near(float(eval(calculation)), 15)
    except OverflowError:
        text.delete(1.0, END)
        text.insert(END, "Overflow Error")
        calculation = str(calculation)
    except ZeroDivisionError as e:
        text.delete(1.0, END)
        text.insert(END, str(e))
        calculation = str(calculation)
    except SyntaxError:
        text.delete(1.0, END)
        text.insert(END, "This is not a valid evaluation!")
        calculation = str(calculation)
    else:
        if x.is_integer():
            x = int(x)
        calculation = str(x)

        text.delete(1.0, END)
        text.insert(END, calculation)

    text.config(state="disabled")


def factorial():
    global calculation
    text.config(state="normal")
    data = text.get(1.0, END)
    data = list(data[::-1])
    data.remove("\n")

    x = []  #
    y = 0
    for i in data:

        if not str(i).isdigit() and str(i) != "!":
            break
        else:
            x.append(i)
            y += 1
    x = x[::-1]
    factorial_number = ""
    for i in x:
        factorial_number += i
    try:
        calculation = calculation[:-y]
        calculation += str(m.factorial(int(factorial_number)))
    except OverflowError as e:
        text.delete(1.0, END)
        text.insert(END, str(e))
    except:
        calculation = calculation

    text.insert(END, "!")
    text.config(state="disabled")


def square():
    global calculation
    calculation += "**2"
    text.config(state="normal")
    text.insert(END, "\u00b2")
    text.config(state="disabled")


def click(n):
    global calculation
    calculation = calculation + str(n)
    text.config(state="normal")
    text.insert(END, n)
    text.config(state="disabled")


def clear():
    global calculation
    calculation = ""
    text.config(state="normal")
    text.delete(1.0, END)
    text.config(state="disabled")


def backspace():
    global calculation
    calculation = str(calculation)[:-1]
    text.config(state="normal")
    text.delete("end-2c", END)
    text.config(state="disabled")


def render_buttons():
    text.config(state="normal")
    row = 3
    column = 0

    for i in range(1, 10):
        if column >= 3:
            column -= 3
            row += 1
        Button(frame, text=i, font=("Roboto", 10), width=10, command=lambda x=i: click(x), bg="#00D7FF") \
            .grid(row=row,
                  column=column,
                  pady=2)
        column += 1

    Button(frame, text="0", font=("Roboto", 10), width=10, command=lambda: click(0), bg="#00D7FF").grid(row=6, column=1,
                                                                                                        pady=2)
    Button(frame, text=".", font=("Roboto", 10), width=10, command=lambda: click(".")).grid(row=6, column=2, pady=2)
    Button(frame, text="Clear", font=("Roboto", 10), width=10, command=clear).grid(row=6, column=0, pady=2)

    column = 3
    symbols = ["/", "*", "-", "+"]
    row = 2
    for i in symbols:
        Button(frame, text=i, font=("Roboto", 10), width=10, command=lambda x=i: click(x), bg="#72FFFF") \
            .grid(row=row,
                  column=column,
                  pady=2)
        row += 1

    Button(frame, text="=", font=("Roboto", 10), width=10, command=evaluate, bg="#5800FF").grid(row=6, column=3, pady=2)
    Button(frame, text=".", font=("Roboto", 10), width=10, command=lambda: click("."), bg="#72FFFF").grid(row=6,
                                                                                                          column=2,
                                                                                                          pady=2)
    Button(frame, text="Clear", font=("Roboto", 10), width=10, command=clear, bg="#72FFFF").grid(row=6, column=0,
                                                                                                 pady=2)
    Button(frame, text="(", font=("Roboto", 10), width=10, command=lambda: click("("), bg="#72FFFF").grid(row=2,
                                                                                                          column=0,
                                                                                                          pady=2)
    Button(frame, text=")", font=("Roboto", 10), width=10, command=lambda: click(")"), bg="#72FFFF").grid(row=2,
                                                                                                          column=1,
                                                                                                          pady=2)
    Button(frame, text="n!", font=("Roboto", 10), width=10, command=factorial, bg="#72FFFF").grid(row=2,
                                                                                                  column=2,
                                                                                                  pady=2)
    Button(frame, text="n\u00b2", font=("Roboto", 10), width=10, command=square, bg="#72FFFF").grid(row=1,
                                                                                                    column=2,
                                                                                                    pady=2)
    Button(frame, text="\u03C0", font=("Roboto", 10), width=10, command=lambda x=pi: click(x), bg="#72FFFF").grid(row=1,
                                                                                                                  column=1,
                                                                                                                  pady=2)
    Button(frame, text="e", font=("Roboto", 10), width=10, command=lambda x=euler: click(x), bg="#72FFFF").grid(row=1,
                                                                                                                column=0,
                                                                                                                pady=2)
    Button(frame, text="delete <--", font=("Roboto", 10), width=10, command=backspace, bg="#72FFFF").grid(row=1,
                                                                                                          column=3,
                                                                                                          pady=2)

    text.config(state="disabled")


render_buttons()
window.mainloop()
