#Input: 10, 20, 30, 40, 50

import random

number_to_guess = random.randint(1, 50)

while True:
    user_guess = int(input("Zgadnij liczbę (od 1 do 50): "))
    
    if user_guess < number_to_guess:
        print("Za niska!")
    elif user_guess > number_to_guess:
        print("Za wysoka!")
    else:
        print("Gratulacje! Zgadłeś poprawną liczbę.")
        break