#CHECKBOX FROM H.G

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('200x50')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())


ttk.Checkbutton(root,
                text='Do you agree?',
                command=agreement_changed,
                variable=agreement,
                onvalue='π--agreed--πsimple project from πππππ ππππππ»α΄Όα΄Ήα΄±α΅α΄΄ α΅α΄΅α΄Ώα΅Λ’α΄¬α΄Ώα΄¬',
                offvalue='disagree').pack()


root.mainloop()