from pathlib import Path

current_directory = Path.cwd()

size_limit = 100 * 1024  # 100 KB
large_files = [f for f in current_directory.iterdir() if f.is_file() and f.stat().st_size > size_limit]

print("\nPliki większe niż 100 KB:")
for file in large_files:
    print(f"{file.name} - {file.stat().st_size / 1024:.2f} KB")
