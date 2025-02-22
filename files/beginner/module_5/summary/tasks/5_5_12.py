# Input: Kapustka,zupa,kubek,exit

def join_words(words):
    result = ""
    for word in words:
        result += word + " "
    return result.strip()


def main():
    words = []
    while True:
        word = input("Podaj słowo (lub 'exit' aby zakończyć): ")
        if word.lower() == 'exit':
            break
        words.append(word)

    joined_text = join_words(words)
    print("Połączone słowa:", joined_text)


if __name__ == "__main__":
    main()
