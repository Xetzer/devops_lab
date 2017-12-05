"""Simple system monitor app"""
from datetime import datetime
from time import sleep
import psutil
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

CONFIG = configparser.ConfigParser()
CONFIG.read("settings.ini")
OUTP = "output." + CONFIG.get("common", "output")
PER = int(CONFIG.get("common", "interval"))*60
NUMB = int(CONFIG.get("common", "snap_num"))

class System_Mon:
    '''Class that collects system information'''
    def __init__(self):
        global NUMB
        self.snap = "SNAPSHOT " + str(NUMB)
        self.dat = "TIMESTAMP:" + str(datetime.now().strftime("%Y-%m-%d,%H:%M:%S"))
        self.cpu = "CPU usage,%:" + str(psutil.cpu_percent(interval=1, percpu=False))
        self.mem = "Memory usage,%:" + str(psutil.virtual_memory().percent)
        self.virt = "VirMem usage,%:" + str(psutil.swap_memory().percent)
        self.diskr = "Disk read,Mb:" + str(round(psutil.disk_io_counters().read_bytes / (1024 ** 2), 2))
        self.diskw = "Disk write,Mb:" + str(round(psutil.disk_io_counters().write_bytes / (1024 ** 2), 2))
        self.disku = "Disk usage,%:" + str(psutil.disk_usage('/').percent)
        self.netws = "Network sent,Mb:" + str(round(psutil.net_io_counters().bytes_sent / (1024 ** 2), 2))
        self.netwr = "Network received,Mb:" + str(round(psutil.net_io_counters().bytes_recv / (1024 ** 2), 2))
    def GetStats(self):
        '''Method that prints current system state'''
        print("{0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(self.snap, self.dat, self.cpu, self.mem, self.virt, self.diskr, self.diskw, self.disku, self.netws, self.netwr))
    def WriteStats(self):
        '''Method that writes current system state to log'''
        global NUMB
        with open(OUTP, "a") as log:
            log.write("{0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(self.snap, self.dat, self.cpu, self.mem, self.virt, self.diskr, self.diskw, self.disku, self.netws, self.netwr))
            log.close()
        NUMB += 1
        CONFIG.set("common", "snap_num", str(NUMB))
        with open("settings.ini", "w") as conffile:
            CONFIG.write(conffile)
            conffile.close()

def out():
    '''Method that treates new object of System_Mon class'''
    new_snapshot = System_Mon()
    new_snapshot.GetStats()
    new_snapshot.WriteStats()

while True:
    out()
    sleep(PER)
