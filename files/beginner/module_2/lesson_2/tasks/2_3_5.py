alfabet = ["a", "b", "c", "d"]

if __name__ == "__main__":
    # Dodajemy pojedynczą literę
    alfabet.append("e")
    # Dodajemy kilka liter jednocześnie
    alfabet.extend(["f", "g"])

    print(alfabet)
