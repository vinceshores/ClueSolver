import tkinter as tk
from tkinter import ttk

from tkinter.messagebox import showwarning


class AskNames(ttk.Frame):
    def __init__(self, parent, num_names, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.vars = []
        self.button = ttk.Button(self, text='Confirm')
        question_lbl = ttk.Label(self, text='What are the player names?', style='Subtitle.TLabel')
        for i in range(num_names):
            var = tk.StringVar(self)
            self.vars.append(var)
            default = 'Player {}'.format(i+1)
            lbl = ttk.Label(self, text=default)
            entry = ttk.Entry(self, textvariable=var, justify=tk.CENTER)
            var.set(default)

            lbl.grid(column=1, row=i+2, pady=5, padx=(0, 6), sticky=tk.E)
            entry.grid(column=2, row=i+2, pady=5, padx=(6, 0), sticky=tk.W)
        question_lbl.grid(column=1, row=1, columnspan=2)
        self.button.grid(column=1, row=num_names+3, columnspan=2, pady=(5, 0))

    def get_names(self):
        return [var.get().strip() for var in self.vars]


def ask_names(parent, num_players):
    def quit_and_destroy():
        names = ask.get_names()
        if len(set(names)) == len(names):
            parent.quit()
            ask.destroy()
        else:
            showwarning(title='Warning', message='Cannot have two of the same names')

    ask = AskNames(parent, num_players)
    ask.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
    ask.button.config(command=quit_and_destroy)
    parent.mainloop()
    return ask.get_names()
