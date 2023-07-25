import os
import sys
import time
import random as r
import threading
import multiprocessing
import tkinter as tk
import string


def display(num, displayLocation):
    label = label_dict[displayLocation]
    label.config(text=f"Number:{num}")
    label.config(bg='white')
    time.sleep(0.2)
    label.config(bg=color_dict[displayLocation])


def task(lb,ub,refreshTime, displayLocation):
    while(True):
        num = r.randint(lb,ub)
        display(num, displayLocation)
        time.sleep(refreshTime)


root = tk.Tk()
root.geometry("350x350")
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


t1 = threading.Thread(target=task, args=(10,20,2,'D1'))
t2 = threading.Thread(target=task, args=(-10,10,1,'D2'))
t3 = threading.Thread(target=task, args=(-100,0,4,'D3'))
t4 = threading.Thread(target=task, args=(20,50,6,'D4'))
t5 = threading.Thread(target=task, args=(-40,40,5,'D5'))
t6 = threading.Thread(target=task, args=(100,200,3,'D6'))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

root.mainloop()