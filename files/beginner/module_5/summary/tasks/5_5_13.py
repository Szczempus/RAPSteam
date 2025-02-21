#Input: hello

def double_letters(text):
    result = ''
    for char in text:
        result += char * 2
    return result

word = input("Podaj słowo: ")
print(double_letters(word))

