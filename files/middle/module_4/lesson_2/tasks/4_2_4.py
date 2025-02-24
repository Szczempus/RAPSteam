import importlib.util

# Sprawdzenie, czy biblioteka requests jest zainstalowana
package_name = "requests"
spec = importlib.util.find_spec(package_name)

if spec is None:
    print(
        f"Biblioteka '{package_name}' nie jest zainstalowana. Możesz ją zainstalować za pomocą: pip install {package_name}")
else:
    print(f"Biblioteka '{package_name}' jest zainstalowana.")
