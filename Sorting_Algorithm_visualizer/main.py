from tkinter import *
from tkinter import ttk, messagebox
import random
from colors import *

# Importing algorithms 
from Algorithms.bubbleSort import bubble_sort
from Algorithms.selectionSort import selection_sort
from Algorithms.mergeSort import merge_sort


# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 1100)
window.config(bg=WHITE)
# window.attributes("-fullscreen", True)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Selection Sort',  'Bubble Sort', 'Merge Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


val = 100


# Randomly generate array
def generate():
    global data
    global val
    data = []
    for i in range(0, val):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def setLimit(value):
    global val
    val = value
    generate()


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    else:
        merge_sort(data, drawData, timeTick)


def endFunc():
    messagebox.showinfo('Sorting Algo Visualizer', 'https://github.com/aishwarya162002/Sorting_Algorithms_Visualizer')
    window.destroy()


### User interface ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="     Sort     ", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="   Generate Array   ", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

b4 = Button(UI_frame, text="       Quit       ", command=lambda: endFunc(), bg=LIGHT_GRAY)
b4.grid(row=2, column=2, padx=5, pady=5)

b5 = Button(UI_frame, text="   100   ", command=lambda: setLimit(100), bg=LIGHT_GRAY)
b5.grid(row=3, column=0, padx=5, pady=5)

b6 = Button(UI_frame, text="   150   ", command=lambda: setLimit(150), bg=LIGHT_GRAY)
b6.grid(row=3, column=1, padx=5, pady=5)

b7 = Button(UI_frame, text="   200   ", command=lambda: setLimit(200), bg=LIGHT_GRAY)
b7.grid(row=3, column=2, padx=5, pady=5)

window.mainloop()