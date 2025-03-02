import tkinter as tk
from tkinter import scrolledtext, ttk
import subprocess
import pty
import os
import threading
import queue
import colorama
from colorama import init, Fore, Back, Style
import McslLib.counts.count as count
from tkinter.messagebox import showinfo


# 初始化colorama
init(autoreset=True)

class Terminal:
    def __init__(self, master, java, server):
        self.master = master
        self.master.title("server控制台")

        # 使用 ttk.Style 来设置样式
        style = ttk.Style()
        style.configure('Terminal.TScrolledText', foreground='white', background='black')

        self.terminal_output = scrolledtext.ScrolledText(master, width=100, height=30, bg='black', fg='white', wrap=tk.WORD, insertbackground='white')
        self.terminal_output.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.terminal_output.config(state=tk.DISABLED)

        self.input_entry = tk.Entry(master, bg='black', fg='white', insertbackground='white')
        self.input_entry.pack(fill=tk.X)
        self.input_entry.bind("<Return>", self.on_enter)
        self.input_entry.bind("<KeyRelease>", self.info)
        self.input_entry.focus_set()
        self.info_list=tk.Listbox(master,width=100,height=10)
        self.info_list.pack()
        self.queue = queue.Queue()

        # 创建伪终端
        self.master_fd, self.slave_fd = pty.openpty()

        # 启动java进程
        self.process = subprocess.Popen(
            [java, "-jar", server],
            stdin=self.slave_fd,
            stdout=self.slave_fd,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        # 启动线程来读取输出
        threading.Thread(target=self.read_output, daemon=True).start()

        self.master.after(100, self.update_output)

        # 创建菜单
        menu = tk.Menu(master)
        master.config(menu=menu)
        help_menu = tk.Menu(menu)
        help_menu.add_command(label="帮助", command=self.help)
        menu.add_cascade(label="帮助", menu=help_menu)

    def help(self):
        a=tk.Tk()
        a.title("帮助")
        la=tk.Label(a,text="输入要查询的指令，按回车键后，会显示指令的帮助")
        la.pack()
        enter=tk.Entry(a)
        enter.pack()
        def info(x):
            try:
                help=count.minecraft_commands_help[str(x)]
            except KeyError:
                help="指令不存在"
            showinfo(title="帮助",message=help)
            a.destroy()
        enter.bind("<Return>",lambda x:info(enter.get()))
        a.mainloop()

    def info(self, message):
        command=self.input_entry.get()
        command=command.split(" ")
        self.info_list.delete(0,tk.END)
        for x in count.minecraft_commands:
            if command[0] in x:
                self.info_list.insert(tk.END,x)
            print(command[0])
            print(count.minecraft_commands)
            print(command[0] in x)
        
    def on_enter(self, event):
        command = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        # 在命令前添加提示符
        self.queue.put(Fore.GREEN + command + Style.RESET_ALL + '\n')
        # 发送命令到java进程
        os.write(self.master_fd, (command + '\n').encode('utf-8'))

    def read_output(self):
        while self.process.poll() is None:  # 检查进程是否结束
            try:
                output = os.read(self.master_fd, 1024).decode('utf-8', errors='replace')
                if output:
                    self.queue.put(output)
            except Exception as e:
                print(f"读取输出时发生错误: {e}")
                break

    def process_output(self, output):
        # 处理ANSI转义序列
        return output

    def update_output(self):
        try:
            while True:
                output = self.queue.get_nowait()
                if output:
                    self.terminal_output.config(state=tk.NORMAL)
                    self.terminal_output.insert(tk.END, output)
                    self.terminal_output.see(tk.END)  # 确保自动滚动到最下面
                    self.terminal_output.config(state=tk.DISABLED)
        except queue.Empty:
            pass
        self.master.after(100, self.update_output)

def show_window(java,server):
    root=tk.Tk()
    terminal = Terminal(root,java,server)
    root.mainloop()

# show_window("/Volumes/扩展卡/py/MCSL2/test/runtime/java-runtime-gamma/mac-os/java-runtime-gamma/jre.bundle/Contents/Home/bin/java","server.jar")
