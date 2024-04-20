### Type: CPU usage monitor --- Style: Modular

import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def display_cpu_usage(cpu_usage):
    print(f"Current CPU Usage: {cpu_usage}%")

def monitor_cpu_usage():
    while True:
        cpu_usage = get_cpu_usage()
        display_cpu_usage(cpu_usage)
        time.sleep(1)

if __name__ == "__main__":
    monitor_cpu_usage()