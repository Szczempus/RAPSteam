
global_counter = 0

def modify_without_global():
    global_counter = 10
    print("Wartość global_counter wewnątrz funkcji (bez global):", global_counter)

def modify_with_global():
    global global_counter
    global_counter = 20
    print("Wartość global_counter wewnątrz funkcji (z global):", global_counter)

print("Wartość global_counter przed wywołaniem funkcji:", global_counter)
modify_without_global()
print("Wartość global_counter po wywołaniu funkcji modify_without_global:", global_counter)
modify_with_global()
print("Wartość global_counter po wywołaniu funkcji modify_with_global:", global_counter)

