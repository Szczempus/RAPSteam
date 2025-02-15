# Zadanie: 1_6_1.py


int_value = 42
float_value = 3.14
complex_value = 1 + 2j

bool_value = True

str_value = "Hello, World!"
list_value = [1, 2, 3]
tuple_value = (4, 5, 6)
bytes_value = b"byte_data"

set_value = {1, 2, 3}

dict_value = {"key1": "value1", "key2": "value2"}

none_value = None

print("Typy liczbowe:")
print(f"int_value: {int_value} (typ: {type(int_value)})")
print(f"float_value: {float_value} (typ: {type(float_value)})")
print(f"complex_value: {complex_value} (typ: {type(complex_value)})\n")

print("Typ logiczny:")
print(f"bool_value: {bool_value} (typ: {type(bool_value)})\n")

print("Typy sekwencyjne:")
print(f"str_value: {str_value} (typ: {type(str_value)})")
print(f"list_value: {list_value} (typ: {type(list_value)})")
print(f"tuple_value: {tuple_value} (typ: {type(tuple_value)})")
print(f"bytes_value: {bytes_value} (typ: {type(bytes_value)})\n")

print("Typ zbiorowy:")
print(f"set_value: {set_value} (typ: {type(set_value)})\n")

print("Typ mapujący:")
print(f"dict_value: {dict_value} (typ: {type(dict_value)})\n")

print("Typ braku wartości:")
print(f"none_value: {none_value} (typ: {type(none_value)})")
