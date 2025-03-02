import cml.doc
from cml.runtime import get_jvm_runtimes, install_jvm_runtime
import sys


# 假设要安装的 JVM 版本是 'java-runtime-gamma'
jvm_version = 'java-runtime-gamma'  # 或其他有效的版本
install_path = sys.argv
current_max = 0


def set_status(status: str):
    print(status)



def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")



def set_max(new_max: int):
    global current_max
    current_max = new_max




callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}
# 调用安装函数
try:
    install_jvm_runtime(jvm_version, install_path,callback=callback)
    print(f"JVM {jvm_version} 安装成功！")
except Exception as e:
    print(f"安装 JVM 失败: {e}")









