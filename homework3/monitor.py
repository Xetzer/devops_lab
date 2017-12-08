"""Simple system monitor app"""
from datetime import datetime
from time import sleep
import psutil
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
config.read("settings.ini")
outp = "output." + config.get("common", "output")
per = int(config.get("common", "interval"))*60
numb = int(config.get("common", "snap_num"))

def stats():
    """Function to get system stats"""
    while True:
        global numb
        snap = "SNAPSHOT " + str(numb)
        dat = "TIMESTAMP:" + str(datetime.now().strftime("%Y-%m-%d,%H:%M:%S"))
        cpu = "CPU usage,%:" + str(psutil.cpu_percent(interval=1, percpu=False))
        mem = "Memory usage,%:" + str(psutil.virtual_memory().percent)
        virt = "VirMem usage,%:" + str(psutil.swap_memory().percent)
        diskr = "Disk read,Mb:" + str(round(psutil.disk_io_counters().read_bytes/(1024**2), 2))
        diskw = "Disk write,Mb:" + str(round(psutil.disk_io_counters().write_bytes / (1024 ** 2), 2))
        disku = "Disk usage,%:" + str(psutil.disk_usage('/').percent)
        netws = "Network sent,Mb:" + str(round(psutil.net_io_counters().bytes_sent / (1024 ** 2), 2))
        netwr = "Network received,Mb:" + str(round(psutil.net_io_counters().bytes_recv / (1024 ** 2), 2))
        print("{0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(snap, dat, cpu, mem, virt, diskr, diskw, disku, netws, netwr))
        with open(outp, "a") as log:
            log.write("{0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(snap, dat, cpu, mem, virt, diskr, diskw, disku, netws, netwr))
        numb += 1
        config.set("common", "snap_num", str(numb))
        with open("settings.ini", "w") as conffile:
            config.write(conffile)
        sleep(per)
stats()
