# stworzenie ksiązki telefonicznej
# wykorzystaj pętlę while
# dodaj kontakt, usun kontakt, wyszukaj kontakt, lista kontaktow
contacts = {}
while True:
    print(f"""
1. Dodaj kontakt
2. Usuń kontakt
3. Wyszukaj kontakt
4. Wyświetl listę kontaktów
5. Koniec""")

    try:
        odp = input("Wybierz opcję")  # str

        if odp == "1":
            name = input("Podaj imię kontaktu:")
            number = input("Podaj numer telefonu kontaktu(tylko cyfry):")
            # A string is a digit string if all characters in the string are digits
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierac cyfry")
            else:
                contacts[name.lower()] = number
                print("Kontakt został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name.lower() in contacts:
                # del contacts[name.lower()]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name.capitalize()} nr telefonu: {contacts[name.lower()]}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Błąd:", e)
