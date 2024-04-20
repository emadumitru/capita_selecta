import psutil
import time

def monitor_cpu_usage():
    while True:
        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(1)

def get_cpu_usage():
    return psutil.cpu_percent()

if __name__ == "__main__":
    monitor_cpu_usage()