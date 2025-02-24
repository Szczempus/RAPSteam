
# Zmienna globalna
global_var = "Jestem globalna"

def przyklad():
    # Zmienna lokalna
    local_var = "Jestem lokalna"
    print("Wewnątrz funkcji:")
    print("global_var =", global_var)  # dostęp do zmiennej globalnej
    print("local_var =", local_var)

przyklad()

print("\nNa zewnątrz funkcji:")
print("global_var =", global_var)
# Próba użycia local_var tutaj spowodowałaby błąd, ponieważ jest dostępna tylko wewnątrz funkcji.
