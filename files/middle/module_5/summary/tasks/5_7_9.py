# Input: onomatopeja
import re

class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Hasło musi mieć co najmniej 8 znaków.")
    if not any(char.isupper() for char in password):
        raise InvalidPasswordError("Hasło musi zawierać co najmniej jedną dużą literę.")
    if not any(char.islower() for char in password):
        raise InvalidPasswordError("Hasło musi zawierać co najmniej jedną małą literę.")
    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Hasło musi zawierać co najmniej jedną cyfrę.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise InvalidPasswordError("Hasło musi zawierać co najmniej jeden znak specjalny.")

try:
    password = input("Podaj hasło: ")
    validate_password(password)
    print("Hasło zaakceptowane!")
except InvalidPasswordError as e:
    print(f"Błąd: {e}")