import time
from urllib.request import urlopen
import wmi
import platform
import hmac
import json

qss_style = """
    * {
        font-size: 11px;
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


# 获取取外网IP
def get_outer_ip() -> str:
    # 法一
    # ip_bytes = urlopen("http://ip.42.pl/raw").read()
    # ip = ip_bytes.decode()

    # 法二
    ip = json.load(urlopen("http://httpbin.org/ip"))["origin"]

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