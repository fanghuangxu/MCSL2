import os
import tkinter as tk
import McslLib.terminal.command_terminal
import subprocess
from tkinter import ttk


def start_frp(current_dir):
    subprocess.Popen([current_dir+"/MCSL/frp/ngrok"," config","add-authtoken","2sgxhto2GjjuFn04WfupYiXe1Cg_6fzK4U7A9dgBBdhZkhybP"])
    McslLib.terminal.command_terminal.show_window([current_dir+"/MCSL/frp/ngrok","tcp","22565"])


def frp_window(current_dir):
    roota=tk.Tk()
    print("frp_window")
    roota.title("内网穿透")
    roota.resizable(False,False)
    ttk.Button(roota,text="启动内网穿透",command=lambda:start_frp(current_dir)).pack(pady=10)