def is_prime(n):
    """Sprawdza, czy podana liczba jest liczbą pierwszą."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Liczba 7 jest liczbą pierwszą? : {is_prime(7)}")  
print(f"Liczba 10 jest liczbą pierwszą? : {is_prime(10)}")  