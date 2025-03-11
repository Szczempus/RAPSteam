# Plik: string_concatenation.py

# Dane wejściowe
hello = "Hello"
world = "World"
name = "John"

# Operator +
plus_concat = hello + " " + world

# Metoda join()
join_concat = " ".join([hello, world])

# f-string
f_string_concat = f"Hi {name}"

# Metoda .format()
format_concat = "Hi {}".format(name)

# Wyświetlenie wyników
print("Operator +      :", plus_concat)
print("Metoda join()   :", join_concat)
print("f-string        :", f_string_concat)
print("Metoda .format():", format_concat)
