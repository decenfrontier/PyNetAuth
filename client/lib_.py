# my function, 客户端登录界面, 和 主界面的函数库
import base64
import time
import wmi
import platform
import json
import random
import logging
import os
import pythoncom
import socket
import ctypes

from win32com.client import Dispatch
from PySide2.QtCore import QThread

from client import crypto_

qss_style = """
    * {
        font-size: 12px;
        font-family: "Microsoft YaHei";
    }
    QTableView {
        selection-color: #000000;
	    selection-background-color: #c4e1d2; 
    }
    QTableView::item:hover	{	
	    background-color: #a1b1c9;		
    }
"""

wnd_login = None
wnd_main = None

cur_time_stamp = int(time.time())
cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

PATH_WORK = os.getcwd()
PATH_SAVE = "C:\\a_b_c"
PATH_TEMP = f"{PATH_SAVE}\\temp"
PATH_JSON_LOGIN = f"{PATH_SAVE}\\login.json"
PATH_JSON_MAIN = f"{PATH_SAVE}\\main.json"
PATH_JSON_PLAN = f"{PATH_SAVE}\\plan.json"

DLL_DM_NAME = "Qt5Sqd.dll"  # dm.dll
DLL_REGDM_NAME = "Qt5Xmr.dll"  # DmReg.dll
DLL_LW_NAME = "lw.dll"
DLL_TR_NAME = "TURING.dll"

COM_NAME_LW = "lw.lwsoft3"
COM_NAME_DM = "dm.dmsoft"
COM_NAME_TR = "TURING.FISR"

# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)


def time_diff(start_sec: int, end_sec: int):
    gap_sec = end_sec - start_sec
    gap_min = gap_sec // 60
    return gap_min


def msleep(min_ms: int, max_ms=None):
    if max_ms is None:
        t_ms = min_ms
    else:
        t_ms = rnd(min_ms, max_ms)
    QThread.msleep(t_ms)

# ---------------------- 日志操作 ----------------------
def init_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s  %(message)s",
                        filename=f"{PATH_SAVE}\\run.log",
                        filemode="w",
                        datefmt="%m-%d  %H:%M:%S")


def log_info(msg):
    logging.info(msg)
    print(msg)


def log_debug(msg):
    logging.debug(msg)
    print(msg)

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

def file_remove(path: str):
    # 删除文件, 存在才删除
    if path_exist(path):
        os.remove(path)

def file_rename(dir: str, old_file: str, new_file: str):
    # 文件重命名
    try:
        os.rename(f"{dir}\\{old_file}", f"{dir}\\{new_file}")
    except:
        log_info("file_rename异常")
        raise OSError

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

# 注册组件到系统
def reg_com_to_system(obj_name):
    # type: (str) -> bool
    obj_dll_dict = {COM_NAME_LW: DLL_LW_NAME, COM_NAME_DM: DLL_DM_NAME, COM_NAME_TR: DLL_TR_NAME}
    dll_name = obj_dll_dict[obj_name]

    cwd_path = os.getcwd()  # 获取工作目录
    path_dll = f"{cwd_path}\\dll\\{dll_name}"
    print(path_dll)
    if obj_name == COM_NAME_DM:
        DmReg = ctypes.WinDLL(f"dll\\{DLL_REGDM_NAME}")
        ret = DmReg.SetDllPathW(path_dll, 1)
    else:  # 此种注册方式需要以管理员运行
        ret = os.system(f"regsvr32 {path_dll} /s")
        ret = True if ret == 0 else False
    if ret:
        return True
    return False

# 创建com组件对象
def create_com_obj(com_name: str):
    obj = None
    try:
        if com_name == COM_NAME_LW:
            obj = CreateObject(com_name)  # op, lw
        else:
            obj = Dispatch(com_name)  # dm, tr
    except:
        log_info(f"创建com对象{com_name}失败")
    return obj

# ------------------------- 网络验证相关 -------------------------
# 获取机器码(主板序列号+硬盘序列号)
def get_machine_code():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        disk_serial = c.Win32_DiskDrive()[0].SerialNumber
        disk_serial = disk_serial.strip(".").replace("_", "")
        machine_code = board_serial + disk_serial
        machine_code = machine_code[12:] + machine_code[:12]
        machine_code = machine_code[::-1]
    except:
        machine_code = ""
    print("机器码:", machine_code)
    return machine_code

# 获取操作系统
def get_operation_system() -> str:
    return platform.platform()

# 连接服务端tcp
def connect_server_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err_no = tcp_socket.connect_ex((server_ip, server_port))
    if err_no != 0:
        return None
    return tcp_socket

# 发送数据给服务端
def send_to_server(tcp_socket: socket.socket, client_info_dict: dict):
    # 内容 转 json字符串
    client_info_dict["内容"] = json.dumps(client_info_dict["内容"], ensure_ascii=False)
    # 根据消息类型决定是否对内容aes加密
    if client_info_dict["消息类型"] != "初始":
        # 对json内容进行aes加密
        client_info_dict["内容"] = aes.encrypt(client_info_dict["内容"])
    # 把整个客户端信息字典 转 json字符串
    json_str = json.dumps(client_info_dict, ensure_ascii=False)
    # json字符串 base85编码
    send_bytes = base64.b85encode(json_str.encode())
    try:
        tcp_socket.send(send_bytes)
        print(f"客户端数据, 发送成功: {json_str}")
    except Exception as e:
        log_info(f"客户端数据, 发送失败: {e}")

# 从服务端接收数据
def recv_from_server(tcp_socket: socket.socket):
    tcp_socket.settimeout(5)  # 设置为非阻塞接收, 只等5秒
    recv_bytes = ""
    try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
        recv_bytes = tcp_socket.recv(4096)
    except:
        ...
    tcp_socket.settimeout(None)  # 重新设置为阻塞模式
    if not recv_bytes:  # 若客户端退出,会收到一个空str
        return "", {}
    # base85解码
    json_str = base64.b85decode(recv_bytes).decode()
    print(f"收到服务端的消息: {json_str}")
    # json字符串 转 py字典
    server_info_dict = json.loads(json_str)
    msg_type = server_info_dict["消息类型"]
    server_content_str = server_info_dict["内容"]
    # 把内容json字符串 转 py字典
    if msg_type != "初始":  # 若不为初始类型的消息, 要先aes解密
        # 先aes解密, 获取json字符串
        server_content_str = aes.decrypt(server_content_str)
    # json字符串 转 py字典
    server_content_dict = json.loads(server_content_str)
    return msg_type, server_content_dict

client_ver = "3.6.7"
server_ip = "127.0.0.1"
server_port = 47123
machine_code = get_machine_code()

normal_user = "*d#fl1I@34rt7%gh."  # 正常用户备注
danger_user = "*d#flI1@34rt7%gh."  # 危险用户备注
client_comment = normal_user

# 从服务端获取的数据
aes_key = "*d#f1Il@34rt7%gh."  # AES密钥, 登录界面初始化时获取, 先随机写一个迷惑破解者
user_account = "aaa"  # 用户账号, 登录成功才获取
pwd_pic = "1234"  # 图片密码, 先随机写一个迷惑破解者
pwd_zk = "5678"  # 字库密码, 先随机写一个迷惑破解者
addr_crack = "0x8CFF98"  # 大漠破解VIP内存地址

notice = "加载公告失败..."  # 公告
url_update = "https://www.baidu.com"  # 更新网址
url_card = "https://www.bilibili.com"  # 发卡网址
allow_login = False  # 允许登录
allow_reg = False  # 允许注册
allow_unbind = False  # 允许解绑
latest_ver = "x.x.x"  # 最新版本

# 构造加密类实例化对象
aes = crypto_.AesEncryption(aes_key)  # 先构造一个假的

