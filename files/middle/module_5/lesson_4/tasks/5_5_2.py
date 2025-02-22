import psutil

print("📊 Rozmiary dostępnych dysków:")
for partition in psutil.disk_partitions():
    usage = psutil.disk_usage(partition.mountpoint)
    print(f"- {partition.device}: {usage.total / (1024 ** 3):.2f} GB")
