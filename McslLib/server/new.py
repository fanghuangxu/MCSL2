import tkinter
import os
import McslLib.server.download_file as download_file
import McslLib.server.utils as utils
from cml.utils import get_version_list as version_list
import tkinter as tk
import json
from tkinter import font
import McslLib.forge.install as install
from tkinter import ttk
from tkinter.messagebox import showinfo
import McslLib.java.java as java



def Find_java_path(current_directory):
    java_path=current_directory+"/openjdk"
    print(java_path)
    if os.path.exists(java_path):
        return java_path
    else:
        showinfo(title="提示", message="未找到Java环境，即将为您安装Java环境")
        java.install(current_directory)



def AddServerYuanBan(root, current_directory):
    utils.clear_widgets(root)
    utils.root.withdraw()
    root.title("MCSL2 服务器添加")
    versions = version_list()
    version = []
    for x in versions:
        if x['type'] == "release":
            version.append(x['id'])
    version_combo = tkinter.ttk.Combobox(root, values=version)
    version_combo.set(version[0])  # 设置默认值
    version_combo.pack()
    l=tk.Label(root, text="请输入服务器名称", font=label_font)
    l.pack()
    def cheer_download_Server_jar(server_name):
        
        json_url = ""
        version = version_combo.get()
        for v in versions:
            if v['id'] == version and v['type'] == "release":
                json_url = v["url"]
                list = []
                list.append(json_url)
                download_file.main(urls=list, folder=f'{current_directory}/MCSL/temps/{version_combo.get()}', name=f"{server_name}.json")
                break
        

        # download jar

        with open(f'{current_directory}/MCSL/temps/{version_combo.get()}/{server_name}.json','r') as json_file:
            data = json.load(json_file)

        server_url = data['downloads']['server']['url']
        os.makedirs(f"{current_directory}/MCSL/servers/{server_name.replace('/','')}", exist_ok=True)
        open(f"{current_directory}/MCSL/servers/{server_name}/version.server.txt", "w").write(version_combo.get())
        utils.root.deiconify()
        utils.clear_widgets(root)
        l = tk.Label(root, text="下载完成", font=label_font)
        l.pack()
        root.title()
        utils.download_progress(server_url, f"{current_directory}/MCSL/servers/{server_name}/server.jar") 
        
    server_name_entry = tk.Text(root, height=1, width=20)
    server_name_entry.pack()
    cheer = tkinter.ttk.Button(root, text="下载服务器", command=lambda:cheer_download_Server_jar(server_name_entry.get(1.0, "1.end")))
    cheer.pack()





def AddServerForge(root, current_directory):
    utils.clear_widgets(root)
    utils.root.withdraw()
    root.title("MCSL2 服务器添加")
    versions = version_list()
    version = []
    for x in versions:
        if x['type'] == "release" and int(str(x['id']).replace(".", "")) > 1122:
            version.append(x['id'])
    version.remove("1.7.10")
    version_combo = ttk.Combobox(root, values=version)  # 修改为 ttk.Combobox
    version_combo.set(version[0])  # 设置默认值
    version_combo.pack()
    l = tk.Label(root, text="请输入服务器名称", font=label_font)
    l.pack()
    ll = tk.Entry(root, width=20)
    ll.pack()
    b = ttk.Button(root, text="下载服务器", command=lambda: install.install_forge(version=version_combo.get(), path=f"{current_directory}/MCSL", name=ll.get()))
    b.pack()







label_font = font.Font(size=12)
def AddServer(root, current_directory):
    utils.clear_widgets(root)
    utils.root.withdraw()
    root.title("MCSL2 服务器添加")
    label = tk.Label(root, text="选择服务器类型", font=label_font)
    label.pack()
    
    a=tkinter.ttk.Combobox(root, values=["原版"])
    a.pack()
    def next_page():
        if a.get() == "原版":
            AddServerYuanBan(root, current_directory)
        elif a.get() == "Forge":
            print("forge")
            AddServerForge(root, current_directory)
        print(a.get())
    tkinter.ttk.Button(root, text="确定", command=next_page).pack()


if __name__ == '__main__':
    root = tk.Tk()
    AddServer(root, "/Volumes/扩展卡/py/MCSL2/")
    root.mainloop()
