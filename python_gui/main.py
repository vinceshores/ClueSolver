from tkinter import ttk
import tkinter as tk

from python_gui.gui.cluegui import Clue
from python_gui.gui.styles import configure_styles
from python_gui.gui.cluemenu import ClueMenu
from python_gui.controller import Controller


def main():
    root = tk.Tk()
    menu = ClueMenu()
    root.wm_title('Clue Solver')
    root.config(menu=menu)
    configure_styles()
    controller = Controller()
    clue = Clue(root, controller=controller)
    menu.signal_new.connect(clue.on_new)
    menu.signal_add.connect(clue.on_add_player)
    menu.signal_remove.connect(clue.on_remove_player)
    menu.signal_edit_overrides.connect(clue.on_edit_overrides)
    menu.signal_edit_order.connect(clue.on_edit_order)

    clue.gui.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
