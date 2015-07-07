#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import time

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.rectx = 5;
        self.recty = 5;
        self.setCanvas();
    def setCanvas(self):
        canvas = tk.Canvas(self,width=700,height=500,bg="#aaa");
        canvas.create_rectangle(0,0,700,500,width=0)
        rect = canvas.create_rectangle(self.rectx,self.recty,30,30,width=1,fill="#3f7",tag="vip")
        canvas.pack()
        canvas.tag_bind(rect,"<Button1-Motion>",self.moveRect)
        self.canvas = canvas
    def moveRect(self,e):
        self.canvas.coords("vip",e.x-15,e.y-15,e.x+15,e.y+15)
        
    def __del__(self):
        pass

f = Frame()
f.mainloop()
