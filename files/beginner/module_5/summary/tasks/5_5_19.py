# Input: 5,3,6,8,2,exit

def input_numbers():
    numbers = []
    while True:
        user_input = input("Wpisz liczbę (lub 'exit' żeby wyjść): ")
        if user_input.lower() == 'exit':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers


input_numbers()
