# Zadanie: 1_6_2.py

string_value = "42"


int_from_str = int(string_value)        
float_from_str = float(string_value)    
bool_from_str = bool(string_value)      
complex_from_str = complex(string_value) 

print("Konwersje dla str:")
print(f"int: {int_from_str} (typ: {type(int_from_str)})")
print(f"float: {float_from_str} (typ: {type(float_from_str)})")
print(f"bool: {bool_from_str} (typ: {type(bool_from_str)})")
print(f"complex: {complex_from_str} (typ: {type(complex_from_str)})\n")

float_value = 3.14

str_from_float = str(float_value)       
int_from_float = int(float_value)       
bool_from_float = bool(float_value)     
complex_from_float = complex(float_value) 

print("Konwersje dla float:")
print(f"str: {str_from_float} (typ: {type(str_from_float)})")
print(f"int: {int_from_float} (typ: {type(int_from_float)})")
print(f"bool: {bool_from_float} (typ: {type(bool_from_float)})")
print(f"complex: {complex_from_float} (typ: {type(complex_from_float)})")
