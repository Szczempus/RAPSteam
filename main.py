import glob
import os

import win32com.client as win32
from pygments import highlight
from pygments.formatters import RtfFormatter
from pygments.lexers import PythonLexer


def py_to_rtf(py_file, rtf_file, style_name="colorful"):
    """
    Konwgpertuje plik .py na plik .rtf z kolorowaniem Pygments.
    """
    with open(py_file, "r", encoding="utf-8") as f:
        code = f.read()
    rtf_content = highlight(code, PythonLexer(), RtfFormatter(style=style_name))
    with open(rtf_file, "w", encoding="utf-8") as f:
        f.write(rtf_content)


def copy_rtf_to_clipboard(word_app, rtf_path):
    """
    Otwiera tymczasowo plik RTF w Wordzie i kopiuje zawartość do Schowka
    za pomocą Range.Copy() (bez Selection).
    """
    rtf_doc = word_app.Documents.Open(os.path.abspath(rtf_path))

    # Pobierz range z całego dokumentu RTF
    rtf_range = rtf_doc.Range()
    # Kopiuj do Schowka
    rtf_range.Copy()

    # Zamknij dokument RTF bez zapisywania
    rtf_doc.Close(SaveChanges=False)

    # Usuń RTF
    os.remove(rtf_path)


def replace_placeholder_with_table(doc, placeholder_text):
    """
    Szuka 'placeholder_text' w doc.Content (obiekt Range).
    Gdy znajdzie, usuwa placeholder i wstawia tabelę 1x1,
    do której wkleja zawartość Schowka przez Range.Paste().

    Zwraca True, jeśli usunięto placeholder, False w przeciwnym razie.
    """
    main_range = doc.Content
    find = main_range.Find

    find.Text = placeholder_text
    find.ClearFormatting()
    find.Replacement.ClearFormatting()

    # Wrap=0 => wdFindStop (brak kontynuacji wyszukiwania od początku)
    find.Wrap = 0

    found = find.Execute()
    if not found:
        return False

    # Po .Execute(), obiekt main_range jest zaktualizowany
    # i wskazuje na znaleziony fragment (tzw. "found range").
    # Możemy pobrać jego Start/End:
    start_pos = main_range.Start
    end_pos = main_range.End

    # Utwórz Range dokładnie w miejscu znalezionego placeholdera
    found_range = doc.Range(Start=start_pos, End=end_pos)

    # Usuwamy placeholder (zamieniamy na pusty string)
    found_range.Text = ""

    # Teraz chcemy wstawić TABELĘ 1x1 w miejscu start_pos
    insert_range = doc.Range(Start=start_pos, End=start_pos)
    table = doc.Tables.Add(insert_range, 1, 1)

    # Pobierz Range komórki tabeli (1,1)
    cell_range = table.Cell(1, 1).Range
    # Uwaga: Word automatycznie dodaje znak końca komórki,
    # więc najczęściej realny tekst to cell_range.Text == '\r\a'

    # Wklej zawartość Schowka do tej komórki (Range, nie Selection)
    cell_range.Paste()

    return True


# -------------------------------------------------------------------
# 4. Główna funkcja
# -------------------------------------------------------------------
def main():
    word_app = win32.Dispatch("Word.Application")
    # Możesz dać False, żeby wszystko działo się w tle.
    word_app.Visible = True

    doc_path = "python_podstawowy.docx"
    output_doc_path = "python_podstawowy_final.docx"

    try:
        # Otwórz dokument bazowy
        doc = word_app.Documents.Open(os.path.abspath(doc_path))

        # ----------------------------------------------------------------
        # Znajdź wszystkie pliki .py w katalogu files/beginner/
        # ----------------------------------------------------------------
        py_files = glob.glob(os.path.join("files/beginner", "**", "*.py"), recursive=True)

        for py_file in py_files:
            # Pobierz nazwę pliku bez ścieżki i rozszerzenia
            base_name = os.path.splitext(os.path.basename(py_file))[0]

            # Tworzymy placeholder w formacie zgodnym ze strukturą katalogów
            # np. "lesson_2/code/bad.py" -> "lesson_2_code_bad"
            relative_path = os.path.relpath(py_file, "files/beginner")
            # if last dir is not /code/ then skip
            elements = relative_path.split(os.sep)
            if not elements[-2] in ["code", "tasks"] or "__init__" in relative_path:
                continue
            placeholder_name = relative_path.replace(os.sep, "_").replace("code_", "").replace("tasks_", "")
            placeholder_name = f"[{placeholder_name}]"

            # 1. Generuj RTF
            rtf_file = os.path.join("files", base_name + ".rtf")
            py_to_rtf(py_file, rtf_file, style_name="colorful")

            # 2. Kopiuj do Schowka
            copy_rtf_to_clipboard(word_app, rtf_file)

            # 3. Zastąp placeholder w dokumencie
            replaced = replace_placeholder_with_table(doc, placeholder_name)
            if replaced:
                print(f"Wstawiono kod z {py_file} w miejsce: {placeholder_name}")
            else:
                print(f"Nie znaleziono placeholdera: {placeholder_name}")

        # Zapisz wynik
        doc.SaveAs(os.path.abspath(output_doc_path))
        doc.Close()

    finally:
        word_app.Quit()

    print(f"Gotowe! Wynik zapisany jako: {output_doc_path}")


if __name__ == "__main__":
    main()
