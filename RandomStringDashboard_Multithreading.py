import os
import sys
import time
import random as r
from random import randint
import threading
import multiprocessing
import tkinter as tk
import string


def display(string_val, displayLocation):
    label = label_dict[displayLocation]
    printval = "String: " + str(string_val)
    label.config(text=printval)
    label.config(bg='white')
    time.sleep(0.2)
    label.config(bg=color_dict[displayLocation])


def task(refreshTime, displayLocation):
    while(True):
        # Generate a random integer between 5 and 9
        N = r.randint(5, 10)
        # Make a random string of N length
        res = ''.join(r.choices(string.ascii_uppercase + string.digits, k=N))
        result = str(res)
        display(result, displayLocation)
        time.sleep(refreshTime)


root = tk.Tk()
root.geometry("500x350")
root.configure(bg='black')
root.title("Random Value Display Dashboard")

# Create label dictionary to store labels for display locations
label_dict = {}

# Create labels for display locations
locations = ["D1", "D2", "D3", "D4", "D5", "D6"]
label = []
colors = ['yellow', 'red', 'blue', 'pink', 'green', 'gray']
color_dict={}
text_dict={}

c = 0
for i in range(6):
    label.append(tk.Label(root, text=f"Location{i}", font=('Times', 16)))
    label[i].grid(padx=(30, 30), pady=(40, 40))
    label[i].config(bg=colors[c])
    c = c+1

k = 0
for i in range(3):
    for j in range(2):
        label[k].grid(row=i, column=j)
        label_dict[locations[k]] = label[k]
        color_dict[locations[k]]=colors[k]
        k = k+1


t1 = threading.Thread(target=task, args=(1, 'D1'))
t2 = threading.Thread(target=task, args=(2, 'D2'))
t3 = threading.Thread(target=task, args=(3, 'D3'))
t4 = threading.Thread(target=task, args=(4, 'D4'))
t5 = threading.Thread(target=task, args=(5, 'D5'))
t6 = threading.Thread(target=task, args=(6, 'D6'))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

root.mainloop()