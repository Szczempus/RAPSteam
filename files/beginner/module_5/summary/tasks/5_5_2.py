#Input: Kapustka

def count_vowels(word):
    """
    Counts the number of vowels in a given word.

    Parameters:
    word (str): The word to count vowels in.

    Returns:
    int: The number of vowels in the word.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Wpisz słowo: ")
count_vowels(word)
