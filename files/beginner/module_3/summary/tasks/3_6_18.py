# Input: PL1234567890

vat_id = input("Podaj identyfikator VAT UE: ").upper()

if len(vat_id) > 2 and vat_id[:2].isalpha() and vat_id[2:].isalnum():
    print("Identyfikator VAT UE jest poprawny.")
else:
    print("Niepoprawny identyfikator VAT UE.")
