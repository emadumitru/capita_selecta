### Type: CPU usage monitor --- Style: Simple

import psutil
import time

def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent()
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(1)

if __name__ == "__main__":
    monitor_cpu_usage()