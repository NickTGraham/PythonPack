#!/usr/bin/env python3

# GUI for launching Scripts
# Goal is large buttons easy to use with a touch screen
# Would like to have status display how things go with the commands
# List of Commands
#   Rotate Left
#   Rotate Right
#   Reset Wifi
#   ~Check Bitcoin Amount~
#   Get Weather

import subprocess
import tkinter as tk
from math import sqrt, ceil

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        buttonFile = open("buttons.txt")
        buttons = list(buttonFile)
        maxNum = sqrt(len(buttons) + 1)
        maxNum = int(ceil(maxNum))
        r = 0
        c = 0
        for button in buttons:
            button = button[:-1]
            info = button.split(" = ")
            self.button = tk.Button(self, height = 10, width = 15, text=info[0], command=lambda x=info[0], y=info[1]: self.command_parser(x, y))
            # self.button = tk.Button(self, height = 10, width = 15)
            # self.button["text"] = info[0]
            # self.button["command"] = lambda: self.command_parser(info[1])
            self.button.grid(row = r, column = c)
            if (c >= maxNum - 1):
                c = 0
                r += 1
            else:
                c += 1
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy, height = 10, width = 15)
        self.quit.grid(row = maxNum - 1, column = maxNum - 1)
        self.T = tk.Text(self, height = 1, width = (maxNum)*15)
        self.T.tag_config('center', justify = tk.CENTER)
        self.T.grid(row = maxNum, columnspan = maxNum)
        self.T.insert(tk.END, "Select Command", 'center');
        # self.hi_there = tk.Button(self, height = 10, width = 15)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.grid(row = 0, column = 0)
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy, height = 10, width = 15)
        # self.quit.grid(row = 1, column = 1)

    def command_parser(self, name, command):
        command_args = command.split(" ")
        if (command_args[-1] == '&'):
            subprocess.Popen(command_args)
            self.T.delete(1.0, tk.END)
            self.T.insert(tk.END, name + " successful", 'center');
            return
        retCode = subprocess.call(command_args)

        if (retCode == 0):
            self.T.delete(1.0, tk.END)
            self.T.insert(tk.END, name + " successful", 'center');
        else:
            self.T.delete(1.0, tk.END)
            self.T.insert(tk.END, name + " Failed", 'center');

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.wm_title("Surface Helper")
app = Application(master=root)
app.mainloop()
