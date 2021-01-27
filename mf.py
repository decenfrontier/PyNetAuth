import time
from urllib.request import urlopen
import wmi
import platform

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
    ip_bytes = urlopen("http://ip.42.pl/raw").read()
    ip = ip_bytes.decode()
    return ip


# 获取机器码(主板序列号+cpu序列号)
def get_machine_code():
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        cpu_serial = c.Win32_Processor()[0].ProcessorId
        machine_code = board_serial + cpu_serial
    except:
        machine_code = ""
    return machine_code

# 获取操作系统
def get_operation_system():
    return platform.platform()


