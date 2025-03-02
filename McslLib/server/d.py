import os
import threading
import requests

def download_file(url, output_dir, filename=None):
    if not filename:
        filename = url.split('/')[-1]
    file_path = os.path.join(output_dir, filename)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {filename} successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")
def threaded_download(urls, output_dir, num_threads=4):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    threads = []
    for url in urls:
        filename = url.split('/')[-1]
        thread = threading.Thread(target=download_file, args=(url, output_dir, filename))
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

