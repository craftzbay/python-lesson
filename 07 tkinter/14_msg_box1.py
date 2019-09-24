import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("Information", "Informative message")


answer = messagebox.askokcancel("Question", "Do you want to open this file?")
answer = messagebox.askretrycancel(
    "Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question", "Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")
