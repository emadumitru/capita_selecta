### Type: CPU usage monitor --- Style: Complex

import psutil
import time

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def print_cpu_usage():
    while True:
        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(1)

if __name__ == "__main__":
    print("Starting CPU Usage Monitor...")
    print_cpu_usage()