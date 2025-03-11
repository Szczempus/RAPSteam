# Input: kurs@rapsteam.edu.pl

email = input("Podaj adres e-mail: ")
domain = email.split('@')[-1]
print("Część po znaku '@':", domain)