# Skrypt zajęć 

## Lekcja 1

Komendy zawarte w Lekcja1.txt

### Wstęp (5 min)
- [ ] Przedstawienie się i opowiedzenie o sobie i swoim doświadczeniu 
- [ ] Ustalenie poziomu grupy, zorientowanie się ile osób wie czym jest programowanie, czym jest jezyk Python, czy już coś programowali kiedyś i dlaczego tutaj są. 

### Zapoznanie uczestnika z założeniami kursu (15 min)
#### - Wprowadzenie do formy zajęć
- [ ] Objaśnienie planu prowadzenia zajęć, ile godzin na spotkanie i dogadanie się z grupą w kwestii realizacji
- [ ] Zagajenie czym jest programowanie i algorytmika, odnieśnienie się do przykładów z życia np. poranna rutyna, proces uruchomienia/naprawy samochodu

#### - Wyjaśnienie roli języka Python 
- [ ] Gdzie jest stosowany: web, embedded, ai, datam, automatyzacja
- [ ] Dlaczego jest tak popularny: prostota języka, symantyki bliska językowi angielskiemu, prostota uruchuchomienia, wszechstronność

#### - Zady i walety
- [ ] Wszechstronność jego użycia, bardzo łatwy entry point do nauki języka, składnia bliska językowi mówionemu, wspierany przez wiele popularnych edytorów, wiele bibliotek realizujących mnóstwo funkcji, szerokie wsparcie społeczności i duża ilość poradników w wielu językach
- [ ] Zużywa dużo zasobów gdy nie uruchamiany na typowych PC'tach, nie jest najabrdziej optymalny do wykonywania złożonych obliczeniowo zadań, w dużych projektach zależności czyt. biblioteki mogą zajmowąć dużą przestrzeń pamięci, dependecy hell i niekompatybilność między różnymi wersjami pythona. 

#### - Zady i walety korzystania przez terminal i skrypt

### Instalacja środowiska Python (20 min)

#### - Instalacja Pythona w systemie Windows i Linux
- [ ] Komendy od zmian folderów: cd 
- [ ] Listowanie plików: ls/dir 
- [ ] Pokazanie instalacji pythona w Ubuntu: apt install python3, python3.X
- [ ] Pokazanie instalacji ptythona w Windowsie: instalacja z instalki, dodanie ścieżek do zmiennych systemowych, restart systemu, python dostępny w konsoli

#### - Weryfikacja wersji
- [ ] python3 --version, opowiedzenie o różnicy w wersjach pythona i konieczności ich rozróżniania

#### - Writualne środowiska venv
- [ ] python -m venv /path/to/env 
- [ ] source activate
- [ ] opowiedzenie dlaczego warto tworzyć osobne środowiska

#### - Zarządzanie wersjami


### Podsumowanie (5 min)
- [ ] Plansza z rzeczami które się dowiedzieliśmy

## Lekcja 2 

### Wstęp (5 min)

### Nauczenie zasad tworzenia i struktury skryptów w języku Python (35 min)
- [ ] Zaprezentowanie skryptowości języka python za pomocą kolejności dodawania wartości do zmiennych i prezentowania ich za pomocą printf
- [ ] Wprowadzenie if __name\_\_ == __main\_\_ i jak wygląda proces przetwarzania zmiennych wewnątrz tej konstrukcji. 
- [ ] Pokazanie zasady wcięć i jakie to ma znaczenie w kodzie 
- [ ] Pokazanie przykładów fragmentów kodu i rozwiązanie zagadki co da poniższy kod 
```
a = 0
b = 0
    a = a + 5
    print(f"a: {a} \n")
    b = 5
    print(f"b: {b} \n")
c = a + b
print(f"c: {c} \n")
```
```
a = 0
b = 0 
    a = a + 1
        b = 5
        c = a + b 
    c = a + b 
    print(f"c: {c} \n")
print(f"a: {a}, b: {b} \n")
```
- [ ] Omówienie print()

### Podsumowanie (5 min)
- [ ] Plansza z rzeczami które się dowiedzieliśmy


## Lekcja 3

