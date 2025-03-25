def add_and_divide(matrix1, matrix2):
    """
    Funkcja dodaje odpowiadające elementy dwóch dwuwymiarowych list (macierzy) i dzieli wynik każdej sumy przez 3.

    Argumenty:
      matrix1: Pierwsza dwuwymiarowa lista (macierz) liczb.
      matrix2: Druga dwuwymiarowa lista (macierz) liczb.
    
    Zwraca:
      Nową dwuwymiarową listę, gdzie każdy element jest wynikiem operacji:
         (matrix1[i][j] + matrix2[i][j]) / 3
      Zakłada się, że obie macierze mają te same wymiary.
    """
    
    result = []

    for i in range(len(matrix1)):
        row1 = matrix1[i]
        row2 = matrix2[i]
        
        new_row = []
        
        for j in range(len(row1)):
 
            element1 = row1[j]
            element2 = row2[j]
            
            suma = element1 + element2
            divided_value = suma / 3
            new_row.append(divided_value)

        result.append(new_row)
    
    return result

matrix1 = [
    [3, 6, 9],
    [2, 4, 6]
]

matrix2 = [
    [1, 2, 3],
    [7, 8, 9]
]

wynik = add_and_divide(matrix1, matrix2)
print(f"Wynik operacji add_and_divide: na macierzach: {matrix1} i {matrix2} to:")
print(wynik)
