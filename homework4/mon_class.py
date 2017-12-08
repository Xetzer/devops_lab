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

class System_Mon:
    '''Class that collects system information'''
    def __init__(self):
        global numb
        self.snap = "SNAPSHOT " + str(numb)
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
        global numb
        with open(outp, "a") as log:
            log.write("{0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(self.snap, self.dat, self.cpu, self.mem, self.virt, \
                                                                          self.diskr, self.diskw, self.disku, self.netws, self.netwr))
        numb += 1
        config.set("common", "snap_num", str(numb))
        with open("settings.ini", "w") as conffile:
            config.write(conffile)

def out():
    '''Method that treates new object of System_Mon class'''
    new_snapshot = System_Mon()
    new_snapshot.GetStats()
    new_snapshot.WriteStats()

while True:
    out()
    sleep(per)
