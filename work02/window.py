#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import threading
import time

class LoopThread(threading.Thread):
    def __init__(self,fnc):
        super(LoopThread,self).__init__()
        self.daemon = True
        self.fnc = fnc
    def run(self):
        while True:
            time.sleep(0.001)
            self.fnc();
    def __del__(self):
        print("loopend");

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
        self.th = LoopThread(self.autoMove)
        self.th.start();
    def moveRect(self,e):
        self.canvas.coords("vip",e.x-15,e.y-15,e.x+15,e.y+15)
    def autoMove(self):
        if self.rectx < 665 and self.recty <= 5:
            self.rectx += 1
        elif self.rectx >=665 and self.recty < 465:
            self.recty += 1
        elif self.rectx > 5 and self.recty >= 465:
            self.rectx -=1
        elif self.rectx >= 5 and self.recty >= 5:
            self.recty-=1;
        self.canvas.coords("vip",self.rectx,self.recty,self.rectx+30,self.recty+30)
    def __del__(self):
        print("end");



f = Frame()
f.mainloop()
