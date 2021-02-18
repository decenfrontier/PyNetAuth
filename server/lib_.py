import json
import os

# ---------------------- 文件操作 ----------------------
def path_exist(path: str):
    # 路径是否存在
    if os.path.exists(path):
        return True
    return False

def dir_create(dir: str):
    # 创建目录, 不存在才创建
    if not path_exist(dir):
        os.makedirs(dir)

def dir_get_files(dir: str):
    # 获取目录中的文件
    ret = ""
    for root, dirs, files in os.walk(dir):
        ret = files
        break
    return ret

def file_create(path: str, content=""):
    # 创建文件
    with open(path, "a") as f:
        f.write(content)

def file_clear_content(path: str):
    # 清空文件内容, 若没有文件会自动创建文件
    with open(path, "w+") as f:  # 打开文件并将光标置于开头
        f.truncate()  # 截断文件光标后的内容

def file_read_content(path: str) -> str:
    # 读取文件内容
    if not path_exist(path):
        file_create(path)
    content = ""
    with open(path, "r") as f:
        content = f.read()
    return content

def file_append_content(path: str, content: str):
    # 添加文件内容, 若没有文件会自动创建文件
    with open(path, "a") as f:
        f.write(content)

# json文件 -> py字典
def json_file_to_dict(path_cfg: str, default_cfg: dict):
    try:
        # 若文件不存在, 则用默认的配置字典先创建json文件
        if not path_exist(path_cfg):
            with open(path_cfg, "w", encoding="utf-8") as f:
                json.dump(default_cfg, f, ensure_ascii=False)
        with open(path_cfg, "r", encoding="utf-8") as f:
            cfg_load = json.load(f)
    except:
        print("json decode error!")
        cfg_load = {}
    return cfg_load

# py对象 -> json文件
def dict_to_json_file(py_dict: dict, path_cfg: str):
    try:
        with open(path_cfg, "w", encoding="utf-8") as f:
            json.dump(py_dict, f, ensure_ascii=False, sort_keys=True)
    except:
        print("json encode error!")