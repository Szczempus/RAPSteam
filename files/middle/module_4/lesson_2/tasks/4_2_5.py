import pkg_resources

# Pobranie listy zainstalowanych bibliotek
zainstalowane_biblioteki = sorted([str(d) for d in pkg_resources.working_set])

# Wyświetlenie listy
print("Lista zainstalowanych bibliotek w środowisku Python:")
for biblioteka in zainstalowane_biblioteki:
    print(biblioteka)
