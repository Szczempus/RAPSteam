import psutil

print("Wykryte urządzenia:")
for partition in psutil.disk_partitions():
    print(f"- {partition.device} ({partition.fstype})")
