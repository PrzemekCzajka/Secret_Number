import re, random

def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print("Wybierz prawidłową opcję.")

def main():
    print("WITAJ W GRZE 'SEKRETNA LICZBA'")
    print("SPRÓBUJ ODGADNĄĆ LICZBĘ WYLOSOWANĄ PRZEZ KOMPUTER")

    print("WYBIERZ POZIOM TRUDNOŚCI:")
    print("1 => ŁATWY (Liczba jednocyfrowa, ilość prób: 2)")
    print("2 => ŚREDNI (Liczba dwucyfrowa, ilość prób: 5)")
    print("3 => TRUDNY (Liczba trzycyfrowa, ilość prób: 8)")

    # Definiowanie dostępnych poziomów trudności
    poziom_trudnosci = validate_input("WYBIERZ OPCJĘ (1/2/3): ", ["1", "2", "3"])

    # Wybór odpowiedniego zakresu liczb i liczby prób
    if poziom_trudnosci == "1":
        zakres_liczb = range(1, 11)
        liczba_prob = 2
    elif poziom_trudnosci == "2":
        zakres_liczb = range(1, 101)
        liczba_prob = 5
    else:
        zakres_liczb = range(1, 1001)
        liczba_prob = 8

    # Wylosowanie liczby
    liczba = random.choice(zakres_liczb)

    # Uruchomienie gry
    for i in range(1, liczba_prob + 1):
        print(f"Pozostało ci {liczba_prob - i + 1} prób.")
        gracz = input("Zgadnij liczbę od 1 do {}: ".format(max(zakres_liczb)))

        # Walidacja czy podana wartość to liczba
        if not re.match(r"\d+", gracz):
            print("To nie jest liczba. Spróbuj ponownie.")
            continue

        gracz = int(gracz)

        if gracz == liczba:
            print("Brawo, zgadłeś!")
            break
        else:
            if gracz > liczba:
                print("Liczba jest za duża.")
            else:
                print("Liczba jest za mała.")

    if i == liczba_prob:
        print(f"Niestety, przegrałeś. Tajna liczba to {liczba}.")

if __name__ == "__main__":
    main()