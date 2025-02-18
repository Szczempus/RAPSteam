
def merge_dictionaries(dict1, dict2):
    """
    Łączy ze sobą dwa słowniki podane jako argumenty tej funkcji i zwraca w postaci jednego słownika.
    
    Parametry:
    dict1 (dict): Pierwszy słownik do połączenia.
    dict2 (dict): Drugi słownik do połączenia.
    
    Zwraca:
    dict: Nowy słownik zawierający wszystkie pary klucz-wartość z dict1 i dict2. 
          Jeśli klucz występuje w obu słownikach, wartość z dict2 nadpisuje wartość z dict1.
    """
    merged_dict = dict1.copy()  # Kopiujemy pierwszy słownik, aby nie modyfikować oryginału
    merged_dict.update(dict2)   # Aktualizujemy kopię słownika o pary klucz-wartość z drugiego słownika
    return merged_dict
