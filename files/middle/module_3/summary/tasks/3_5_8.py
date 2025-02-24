def filter_palindromes(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    return [word for word in words if is_palindrome(word)]

# Przykład użycia:
words = ["kajak", "python", "level", "world", "radar"]
print(filter_palindromes(words))  # Output: ['kajak', 'level', 'radar']

