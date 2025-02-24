# Input: Kurs

input_string = input("Podaj tekst do odwrócenia: ")

reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(f"Odwrócony napis {input_string} : {reversed_string}")

