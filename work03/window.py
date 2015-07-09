#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
import urllib.request as ur
import tkinter as tk

class GetBoard():

    def __init__(self):
        self.url = "http://viper.2ch.net/news4vip/subback.html";

    def get_data(self):
        self.fp = ur.urlopen(self.url)
        html = self.fp.read().decode("cp932");
        self.fp.close()
        return html;

    def __del__(self):
        pass


class LoopThread(threading.Thread):

    def __init__(self,fnc):
        super(LoopThread,self).__init__()
        self.daemon = True
        self.fnc = fnc

    def run(self):
        while True:
            time.sleep(1)
            self.fnc();

    def __del__(self):
        print("loopend");



class Frame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self,master,width=600,height=800,bg="#999")

        #ラベル追加・設定
        self.label = tk.Label(self,height=55,width=80,bg="#ddd",anchor=tk.N)
        self.label.pack(padx=5,pady=5)

        #LoopThread
        self.timer = LoopThread(self.reload)

        #GetBoard
        self.board = GetBoard()

        self.pack()
        self.timer.start()
        self.reload()

    def reload(self):
        html = self.board.get_data()
        self.label.configure(text=html)

    def __del__(self):
        pass


f = Frame()
f.mainloop()
