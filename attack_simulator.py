import csv
import random
import time
from datetime import datetime

LOG_FILE = r"C:\splunk_logs\auth_attack_log.csv"

ATTACK_IPS = [
    "185.220.101.4",
    "45.95.147.20",
    "91.219.236.12"
]

INTERNAL_IPS = [
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.15",
    "192.168.1.20"
]

USERS = ["admin", "user1", "user2", "helpdesk", "guest"]

def generate_attack_event():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = random.choice(["admin", "admin", "admin", "helpdesk"])
    ip = random.choice(ATTACK_IPS)
    status = "fail"
    return [timestamp, user, ip, status]

def generate_normal_event():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = random.choice(["user1", "user2", "guest"])
    ip = random.choice(INTERNAL_IPS)
    status = random.choices(["success", "fail"], weights=[85, 15], k=1)[0]
    return [timestamp, user, ip, status]

def write_event(event):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(event)

def main():
    print(f"Writing simulated auth events to: {LOG_FILE}")
    print("Press Ctrl+C to stop.\n")

    while True:
        # 70% chance of attack traffic, 30% chance of normal traffic
        if random.random() < 0.7:
            event = generate_attack_event()
            event_type = "ATTACK"
        else:
            event = generate_normal_event()
            event_type = "NORMAL"

        write_event(event)
        print(f"[{event_type}] {event}")

        # Wait a little so events stream in gradually
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()