
def count_letters(word):
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count

word = "Hello World"
print(f"Słowo {word} zawiera {count_letters(word)} liter")
