import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

root = tk.Tk()
root.title("Page Switching Example")
root.geometry("1100x600")

# -------------------------
# Page 1 (like <div id="page1">)
# -------------------------
page1 = tk.Frame(root, width=500, height=500, bg="lightblue")
page1.place(x=0, y=0)

btn1 = tk.Button(
    page1,
    text="Function One",
    command=lambda: show_page2()
)
btn1.pack(pady=50)

# -------------------------
# Page 2 (like <div id="page2">)
# -------------------------
page2 = tk.Frame(root, width=500, height=500, bg="lightgreen")
page2.place(x=600, y=0)

btn2 = tk.Button(
    page2,
    text="Function Two",
    command=lambda: show_page1()
)
btn2.pack(pady=50)

# -------------------------
# Functions (like JS functions)
# -------------------------
def show_page2():
    messagebox.showinfo("Alert", "function one")
    page1.place_forget()
    page2.place(x=0, y=0)
    full_health_data = pd.read_csv("customer_segmentation_mixed.csv", header=0, sep=",")
    numeric_data = full_health_data.select_dtypes(include='number')
    std = numeric_data.std()
    print(std)

def show_page1():
    messagebox.showinfo("Alert", "function two")
    page2.place_forget()
    page1.place(x=0, y=0)
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()

# Start with page1 only
# page2.place_forget()

root.mainloop()
