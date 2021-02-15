# my function, 客户端登录界面, 和 主界面的函数库

import time
import wmi
import platform
import json
import random
import logging
import os
import pythoncom

from PySide2.QtCore import QThread

from client import my_crypto

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
PATH_LOGIN_JSON = f"{PATH_SAVE}\\login.json"
PATH_GNRL_JSON = f"{PATH_SAVE}\\gnrl.json"
PATH_PLAN_JSON = f"{PATH_SAVE}\\plan.json"


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

def json_to_py(path: str):
    # json文件 -> py对象
    try:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
    except:
        print("json decode error!")
        d = {}
    return d

def py_to_json(pyobj: object, path: str):
    # py对象 -> json文件
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(pyobj, f, ensure_ascii=False, sort_keys=True)
    except:
        print("json encode error!")



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

# ------------------------- 网络验证相关 -------------------------
client_ver = "3.6.8"
server_ip = "127.0.0.1"
server_port = 47123
machine_code = get_machine_code()
client_comment = ""

# 从服务端获取的数据
aes_key = "*d#f12j@34rt7%gh."  # AES密钥, 登录界面初始化时获取, 先随机写一个迷惑破解者
user_account = ""  # 用户账号, 登录成功才获取
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
aes = my_crypto.AesEncryption(aes_key)  # 先构造一个假的


