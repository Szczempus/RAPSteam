
def word_occurrences(sentences, word):
    count = 0
    for sentence in sentences:
        count += sentence.split().count(word)
    return count

# Przykład użycia:
sentences = ["To jest pierwsze zdanie", "To jest drugie zdanie", "To jest trzecie zdanie"]
word = "jest"
print(word_occurrences(sentences, word))  # Output: 3
