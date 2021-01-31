import time
from urllib.request import urlopen
import wmi
import platform
import hmac
import json
import random

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

server_ip = "127.0.0.1"
server_port = 47123

card_key_lenth = 30

# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)

# 获取取外网IP
def get_outer_ip() -> str:
    # ip = urlopen("http://ip.42.pl/raw").read().decode()  # 法一
    ip = json.load(urlopen("http://httpbin.org/ip"))["origin"]  # 法二
    print("ip:", ip)
    return ip

# 获取机器码(主板序列号+硬盘序列号)
def get_machine_code():
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
def get_operation_system():
    return platform.platform()

# 获取加密后字符
def get_encrypted_str(ori_bytes: bytes):
    encrypted = hmac.new(b"dkstFeb.1st", ori_bytes, "sha1")
    return encrypted.hexdigest()

# 生成随机卡密
def gen_rnd_card_key(lenth=card_key_lenth):
    char_list = "0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
    max_idx = len(char_list) - 1
    card_key = ""
    for _ in range(lenth):
        idx = rnd(0, max_idx)
        char = char_list[idx]
        card_key += char
    return card_key
