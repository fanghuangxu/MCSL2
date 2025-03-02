#!/Volumes/FHX/MCSL2/env/bin/python

import McslLib.download as download
import McslLib.frp.frp
import McslLib.server.start as start
import McslLib.server.new as new


import tkinter as tk
from cml.utils import get_version_list as version_list
import os
import requests as req





current_directory=os.getcwd()
new.utils.root.withdraw()
print(current_directory)
root=tk.Tk()
root.title("MCSL2")
root.geometry("500x300")

menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

server_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="服务器",menu=server_menu)
server_menu.add_command(label="新建",command=lambda:new.AddServer(root=root,current_directory=current_directory))
server_menu.add_command(label="启动服务器",command=lambda:start.start_Server(root=root,current_dir=current_directory,java=r"java"))
frp_menu=tk.Menu(menu_bar,tearoff=0)
#menu_bar.add_cascade(label="获取外网ip",menu=frp_menu)
frp_menu.add_command(label="frp管理",command=lambda:McslLib.frp.frp.frp_window(current_dir=current_directory))

# 获取公告

json=req.get("https://fanghuangxu.github.io/mcsl-mc/notice.json").json()
print(json)
title_label=tk.Label(root,text="公告",font=("Arial",16)).grid(row=0,column=0)
notice_label=tk.Label(root,text=f"      {json['info']}",font=("Arial",12)).grid(row=1,column=0,padx=10,pady=10)
root.mainloop()
