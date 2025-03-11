import os

# os.mkdir("mój folder")

path = "./mój folder"

print(os.path.exists(path))

with open (path + "/plik tekstowy.txt", "w") as file:
    file.write("Hello World \n This is a test file \n")

text_file = path + "/plik tekstowy.txt"

with open (text_file, "r") as file:
    print(file.read())
