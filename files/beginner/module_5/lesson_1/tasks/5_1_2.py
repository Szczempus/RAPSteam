
def celsius_na_fahrenheit(celsius):
    """
    Przelicza temperaturę ze stopni Celsjusza na Fahrenheita.

    Parametry:
    celsius (float): Temperatura w stopniach Celsjusza.

    Zwraca:
    float: Temperatura w stopniach Fahrenheita.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(f"22 stopni Celsjusza to {celsius_na_fahrenheit(22)} stopnie Fahrenheita")