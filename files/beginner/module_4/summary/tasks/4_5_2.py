# Input: To jest zdanie

text = input("Podaj tekst: ")
if not text.endswith("."):
    text += "."
print(text)
