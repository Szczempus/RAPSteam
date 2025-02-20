import os

extension = ".txt"
current_directory = os.getcwd()

txt_files = [f for f in os.listdir(current_directory) if f.endswith(extension)]

print("\nPliki o rozszerzeniu .txt w bieżącym katalogu:")
for file in txt_files:
    print(file)
