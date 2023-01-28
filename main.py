import math as m
import sys
from keyboard import *
from tkinter import *
from tkinter.font import Font
import pyperclip


window = Tk()
window.geometry("375x550")
window.title('Calculator')
window.config(bg="grey")
font = Font(family="Roboto", size=10)

text = Text(window, height=4, font=("Roboto", 15), state="disabled")
text.grid(column=0, row=0, columnspan=5, sticky="nswe")

pi = m.pi
euler = m.e
calculation = ""
EPSILON = sys.float_info.epsilon

for column_index in range(0, 5):
    window.columnconfigure(column_index, weight=1)
for row_index in range(0, 7):
    window.rowconfigure(row_index, weight=1)


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
    except SyntaxError as e:
        if str(e).startswith("unexpected EOF"):
            calculation += ")"
            evaluate()

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


def FocusIn(event):
    for i in range(0, 10):
        add_hotkey(str(i), button_click, str(i))

    add_hotkey("backspace", backspace)
    add_hotkey("c", clear)
    add_hotkey("enter", evaluate)
    add_hotkey("ctrl + v", paste)


def FocusOut(event):
    remove_all_hotkeys()


def paste():
    global calculation
    calculation += pyperclip.paste()
    text.config(state="normal")
    text.insert(END, pyperclip.paste())
    text.config(state="disabled")


def factorial():
    global calculation
    text.config(state="normal")
    data = text.get(1.0, END)
    data = list(data[::-1])
    data.remove("\n")

    x = []
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


def logarithm():
    global calculation
    calculation += "m.log10("
    text.config(state="normal")
    text.insert(END, "log(")
    text.config(state="disabled")

def natural_logarithm():
    global calculation
    calculation += "m.log("
    text.config(state="normal")
    text.insert(END, "ln(")
    text.config(state="disabled")


def sqaure_root():
    global calculation
    calculation += "m.sqrt("
    text.config(state="normal")
    text.insert(END, "sqrt(")
    text.config(state="disabled")

def ten_to_the_power():
    global calculation
    calculation += "10**"
    text.config(state="normal")
    text.insert(END, "10^")
    text.config(state="disabled")

def sinus():
    global calculation
    calculation += "m.sin("
    text.config(state="normal")
    text.insert(END, "sin(")
    text.config(state="disabled")

def absolute_value():
    global calculation
    calculation += "abs("
    text.config(state="normal")
    text.insert(END, "abs(")
    text.config(state="disabled")


def button_click(n):
    global calculation
    calculation = calculation + str(n)
    text.get(1.0, END)
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
    column = 1

    for i in range(1, 10):
        if column >= 4:
            column -= 3
            row += 1
        Button(window, text=i, font=font, width=3, command=lambda x=i: button_click(x), bg="#00D7FF") \
            .grid(row=row,
                  column=column,
                  pady=1, sticky="nsew")
        column += 1

    Button(window, text="0", font=font, width=3, command=lambda: button_click(0), bg="#00D7FF").grid(row=6, column=2,
                                                                                                     pady=1,
                                                                                                     sticky="nsew")
    Button(window, text=".", font=font, width=3, command=lambda: button_click(".")).grid(row=6, column=3,
                                                                                         columnspan=1, pady=1,
                                                                                         sticky="nsew")
    Button(window, text="Clear", font=font, width=3, command=clear).grid(row=6, column=1, pady=1,
                                                                         sticky="nsew")

    column = 4
    symbols = ["/", "*", "-", "+"]
    row = 2
    for i in symbols:
        Button(window, text=i, font=font, width=3, command=lambda x=i: button_click(x), bg="#72FFFF") \
            .grid(row=row,
                  column=column,
                  pady=1, sticky="nsew")
        row += 1

    Button(window, text="=", font=font, width=3, command=evaluate, bg="#5800FF").grid(row=6, column=4,
                                                                                      columnspan=1, pady=1,
                                                                                      sticky="nsew")
    Button(window, text=".", font=font, width=3, command=lambda: button_click("."), bg="#72FFFF").grid(row=6,
                                                                                                       column=3,
                                                                                                       columnspan=1,
                                                                                                       pady=1,
                                                                                                       sticky="nsew")
    Button(window, text="Clear", font=font, width=3, command=clear, bg="#72FFFF").grid(row=6, column=1,
                                                                                       pady=1, sticky="nsew")
    Button(window, text="(", font=font, width=3, command=lambda: button_click("("), bg="#72FFFF").grid(row=2,
                                                                                                       column=1,
                                                                                                       pady=1,
                                                                                                       sticky="nsew")
    Button(window, text=")", font=font, width=3, command=lambda: button_click(")"), bg="#72FFFF").grid(row=2,
                                                                                                       column=2,
                                                                                                       pady=1,
                                                                                                       sticky="nsew")
    Button(window, text="n!", font=font, width=3, command=factorial, bg="#72FFFF").grid(row=2,
                                                                                        column=3,
                                                                                        columnspan=1,
                                                                                        pady=1, sticky="nsew")
    Button(window, text="n\u00b2", font=font, width=3, command=square, bg="#72FFFF").grid(row=1,
                                                                                          column=3,
                                                                                          columnspan=1,
                                                                                          pady=1,
                                                                                          sticky="nsew")
    Button(window, text="\u03C0", font=font, width=3, command=lambda x=pi: button_click(x), bg="#72FFFF").grid(row=1,
                                                                                                               column=2,
                                                                                                               pady=1,
                                                                                                               sticky="nsew")
    Button(window, text="e", font=font, width=3, command=lambda x=euler: button_click(x), bg="#72FFFF")\
        .grid(row=1, column=1, pady=1, sticky="nsew")

    Button(window, text="del <--", font=font, width=3, command=backspace, bg="#72FFFF").grid(row=1,
                                                                                             column=4,
                                                                                             columnspan=1,
                                                                                             pady=1,
                                                                                             sticky="nsew")
    Button(window, text="|x|", font=font, width=3, command=absolute_value, bg="#72FFFF").grid(row=1, column=0,
                                                                                              columnspan=1, pady=1,
                                                                                              sticky="nsew")

    Button(window, text="\u221A", font=font, width=3, command=sqaure_root, bg="#72FFFF").grid(row=2, column=0,
                                                                                              columnspan=1,
                                                                                              pady=1, sticky="nsew")

    Button(window, text="log", font=font, width=3, command=logarithm, bg="#72FFFF").grid(row=3, column=0,
                                                                                              columnspan=1,
                                                                                              pady=1, sticky="nsew")

    Button(window, text="ln", font=font, width=3, command=natural_logarithm, bg="#72FFFF").grid(row=4, column=0,
                                                                                         columnspan=1,
                                                                                         pady=1, sticky="nsew")

    Button(window, text="10^n", font=font, width=3, command=ten_to_the_power, bg="#72FFFF").grid(row=5, column=0,
                                                                                                columnspan=1,
                                                                                                pady=1, sticky="nsew")

    Button(window, text="sin", font=font, width=3, command=sinus, bg="#72FFFF").grid(row=6, column=0,
                                                                                                 columnspan=1,
                                                                                                 pady=1, sticky="nsew")
    text.config(state="disabled")


render_buttons()
text.bind('<FocusIn>', FocusIn)
text.bind('<FocusOut>', FocusOut)
text.focus()
window.mainloop()
