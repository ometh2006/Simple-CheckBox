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
                onvalue='🙂--agreed--🙂simple project from 𝙃𝙔𝙋𝙀𝙍 𝙂𝙃𝙊𝙎𝙏👻ᴼᴹᴱᵀᴴ ᵛᴵᴿᵁˢᴬᴿᴬ',
                offvalue='disagree').pack()


root.mainloop()