"""An example with inheritance - I'm not sure if I should use classes like this"""
from datetime import datetime
from time import sleep
import psutil
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
config.read("settings.ini")
output = "output." + config.get("common", "output")
period = int(config.get("common", "interval"))*60

class SystemMonitor:
    '''Class that collects system information'''
    def __init__(self, number):
        self.number = number
        self.date = "TIMESTAMP:" + str(datetime.now().strftime("%Y-%m-%d,%H:%M:%S"))
        self.cpu = "CPU usage,%:" + str(psutil.cpu_percent(interval=1, percpu=False))
        self.memory = "Memory usage,%:" + str(psutil.virtual_memory().percent)
        self.virtual = "VirMem usage,%:" + str(psutil.swap_memory().percent)
        self.disk_read = "Disk read,Mb:" + str(round(psutil.disk_io_counters().read_bytes / (1024 ** 2), 2))
        self.disk_write = "Disk write,Mb:" + str(round(psutil.disk_io_counters().write_bytes / (1024 ** 2), 2))
        self.disk_usage = "Disk usage,%:" + str(psutil.disk_usage('/').percent)
        self.net_sent = "Network sent,Mb:" + str(round(psutil.net_io_counters().bytes_sent / (1024 ** 2), 2))
        self.net_received = "Network received,Mb:" + str(round(psutil.net_io_counters().bytes_recv / (1024 ** 2), 2))

class FormatSnapshot(SystemMonitor):
    '''Class that prints current system state and writes it to log'''
    def print_stats(self):
        '''Method that prints current system state'''
        print("SNAPSHOT {0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(self.number, self.date, self.cpu, self.memory,
                                                                         self.virtual, self.disk_read, self.disk_write,
                                                                         self.disk_usage, self.net_sent, self.net_received))
    def write_stats(self):
        '''Method that writes current system state to log'''
        with open(output, "a") as log:
            log.write("SNAPSHOT {0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(self.number, self.date, self.cpu, self.memory,
                                                                                   self.virtual, self.disk_read, self.disk_write,
                                                                                   self.disk_usage, self.net_sent, self.net_received))
        self.number += 1
        config.set("common", "snap_num", str(self.number))
        with open("settings.ini", "w") as config_file:
            config.write(config_file)

def out():
    '''Function that creates new object of FormatSnapshot class'''
    number = int(config.get("common", "snap_num"))
    new_snapshot = FormatSnapshot(number)
    new_snapshot.print_stats()
    new_snapshot.write_stats()

while True:
    out()
    sleep(period)
