#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.setCanvas();
        self.rectx = 5;
        self.recty = 5;
    def setCanvas(self):
        canvas = tk.Canvas(self,width=700,height=500,bg="#aaa");
        canvas.create_rectangle(0,0,700,500,width=0)
        rect = canvas.create_rectangle(self.rectx,point.recty,30,30,width=1,fill="#3f7")
        canvas.pack()
        self.moveRect()
    def moveRect(self):
        print("test");


f = Frame()
f.mainloop()
