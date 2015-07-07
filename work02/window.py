#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

f = Frame()
f.mainloop()


