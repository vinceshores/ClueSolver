import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from python_gui.constants import total_cards
from python_gui.integercheck import int_validate


class AskNumCards(ttk.Frame):
    def __init__(self, parent, names, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        self._vars = []
        self.button_confirm = ttk.Button(self, text='Confirm')
        question_lbl = ttk.Label(self, text='How many cards does each player have?', style='Subtitle.TLabel')
        from_ = 0
        to_ = ((total_cards - 3) // len(names)) + 1
        for i, name in enumerate(names):
            var = tk.IntVar(self)
            self._vars.append(var)
            lbl = ttk.Label(self, text=name)
            entry = ttk.Spinbox(self, textvariable=var, justify=tk.CENTER, from_=from_, to_=to_)
            var.set(to_ - 1)
            int_validate(entry, limits=(from_, to_))

            lbl.grid(column=1, row=i+2, pady=5, padx=(0, 6), sticky=tk.E)
            entry.grid(column=2, row=i+2, pady=5, padx=(6, 0), sticky=tk.W)
        question_lbl.grid(column=1, row=1, columnspan=2)
        self.button_confirm.grid(column=1, row=len(names) + 3, columnspan=2, pady=(5, 0))

    def set_confirm_command(self, func):
        def confirm_func():
            if sum(self.get_num_cards()) <= (total_cards - 3):
                func()
            else:
                showwarning(title='Warning',
                            message='Total number of cards must be less than {}.'.format(total_cards - 2))
        self.button_confirm.config(command=confirm_func)

    def get_num_cards(self):
        return [var.get() for var in self._vars]
