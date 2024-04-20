import psutil
import time

def track_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent()
        print(f"Current CPU Usage: {cpu_usage}%")
        time.sleep(1)

if __name__ == "__main__":
    track_cpu_usage()
