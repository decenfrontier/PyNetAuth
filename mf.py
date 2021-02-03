# my function, 客户端登录界面, 和 主界面的函数库

import time
import urllib.request
import wmi
import platform
import hmac
import json
import random
import ssl
import logging
import os
import pythoncom

from PySide2.QtCore import QThread

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

cur_time_stamp = time.time()
cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

PATH_WORK = os.getcwd()
PATH_SAVE = "C:\\a_b_c"
PATH_GNRL_JSON = f"{PATH_SAVE}\\gnrl.json"
PATH_PLAN_JSON = f"{PATH_SAVE}\\plan.json"

# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)

def time_diff(start_sec, end_sec):
    gap_sec = end_sec - start_sec
    gap_min = gap_sec // 60
    return gap_min

# def mdelay(min_ms: int, max_ms=None):
#     if max_ms is None:
#         t_ms = min_ms
#     else:
#         t_ms = rnd(min_ms, max_ms)
#     t_s = t_ms / 1000
#     time.sleep(t_s)

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
    log_info("初始化日志模块成功")

def log_info(msg):
    logging.info(msg)
    print(msg)


def log_debug(msg):
    logging.debug(msg)
    print(msg)

# ------------------------- 网络验证-客户端专用 -------------------------
server_ip = "127.0.0.1"
server_port = 47123
client_account = ""
client_comment = ""
# 登录时从服务端获取的数据
heart_gap_sec = 10  # 心跳间隔秒数, 默认600秒, 即10分钟

# 获取外网IP
def get_outer_ip() -> str:
    # ip = urllib.request.urlopen("http://ip.42.pl/raw").read().decode()  # 法一
    req = urllib.request.urlopen("http://httpbin.org/ip")
    ip = json.load(req)["origin"]  # 法二
    print("ip:", ip)
    return ip

# 获取IP归属地
def get_ip_location(ip: str) -> str:
    appcode = "3799d32779864269b80bd92e70619498"
    url = f"https://hcapi20.market.alicloudapi.com/ip?ip={ip}"
    request = urllib.request.Request(url)
    request.add_header("Authorization", "APPCODE " + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read().decode()  # 返回json字符串
    if not content:
        return ""
    ret_dict = json.loads(content)  # json字符串 转 py字典
    if ret_dict["msg"] != "success":
        return ""
    data = ret_dict["data"]
    country, region, city, isp = data["country"], data["region"], data["city"], data["isp"]
    location = f"{country}-{region}-{city}-{isp}"
    print("location:", location)
    return location

# 获取机器码(主板序列号+硬盘序列号)
def get_machine_code():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        disk_serial = c.Win32_DiskDrive()[0].SerialNumber
        disk_serial = disk_serial.strip(".").replace("_", "")
        machine_code = board_serial + disk_serial
        machine_code = machine_code[12:]+machine_code[:12]
        machine_code = machine_code[::-1]
    except:
        machine_code = ""
    print("机器码:", machine_code)
    return machine_code

# 获取操作系统
def get_operation_system() -> str:
    return platform.platform()

# 获取加密后字符
def get_encrypted_str(ori_bytes: bytes) -> str:
    encrypted = hmac.new(b"dkstFeb.1st", ori_bytes, "sha1")
    return encrypted.hexdigest()

