import threading
import requests
import os

def download_file(url, folder, name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        file_name = name  # 从URL获取文件名
        
        with open(f"{folder}/{file_name}", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # 分块下载文件
                file.write(chunk)
        
        print(f"{file_name} 下载完成！")
    except Exception as e:
        print(f"下载出错: {e}")

def main(urls, folder,name):
    print(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)  # 创建文件夹

    threads = []
    
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url, folder,name))
        threads.append(thread)
        thread.start()  # 启动线程

    for thread in threads:
        thread.join()  # 等待所有线程完成