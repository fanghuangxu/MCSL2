import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import time
from cml.helper import get_user_agent
import McslLib.terminal.command_terminal as command_terminal


# 创建主窗口
root = tk.Tk()
root.title("下载forge-installer.jar")
root.geometry("400x150")
# 隐藏root窗口
root.withdraw()
# 创建进度条
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.pack(pady=20)

# 创建标签显示下载进度和速度
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.withdraw()  # 隐藏主窗口

def download_progress(url, path, p2):
    root.deiconify()  # 显示主窗口
    start_download(url, path, p2)  # 开始下载
    root.mainloop()  # 运行主循环

def clear_widgets(window):
    for widget in window.winfo_children():
        if not isinstance(widget, tk.Menu):  # 检查是否为菜单
            widget.destroy()  # 销毁控件

def download_file(url, path, mode='wb', title="下载server.jar", p2=str()):  # 更改窗口标题
    try:
        root.deiconify()
        response = requests.get(url, stream=True, headers={"user-agent": get_user_agent()})
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        start_time = time.time()  # 计时开始

        with open(path, mode) as file:
            for data in response.iter_content(chunk_size=1024):  # 每次下载1KB
                downloaded_size += len(data)
                file.write(data)
                progress = (downloaded_size / total_size) * 100
                progress_bar['value'] = progress

                # 计算下载速度
                elapsed_time = time.time() - start_time
                if elapsed_time > 0:
                    speed = downloaded_size / (1024 * elapsed_time)  # 速度KB/s
                    remaining_time = (total_size - downloaded_size) / (speed * 1024)  # 剩余时间（秒）
                    status_label['text'] = (f"下载进度: {progress:.2f}%  |  速度: {speed:.2f} KB/s  "
                                             f"|  预计剩余时间: {remaining_time:.2f} 秒")

                root.update_idletasks()  # 更新进度条显示

        status_label['text'] = "下载完成！"
        root.withdraw()
        messagebox.showinfo(title, "下载完成！\n即将开始启动forge安装程序...")
        command_terminal.show_window(f"java -jar {path} --installServer {p2} --mirror https://bmclapi2.bangbang93.com/maven")

    except Exception as e:
        print("下载失败！" + str(e))

def start_download(url, path, p2):  # 更改窗口标题
    threading.Thread(target=download_file, args=(url, path, p2)).start()

# 示例调用（请使用实际的URL和路径）
# download_progress("http://example.com/server.jar", "/path/to/save/server.jar")















