import re, random

def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print("Wybierz prawidłową opcję.")

def validate_guess(prompt, valid_range):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            guess = int(user_input)
            if guess in valid_range:
                return guess
            else:
                print("Podaj liczbę z właściwego przedziału.")
        else:
            print("To nie jest liczba. Spróbuj ponownie.")

def main():
    print("WITAJ W GRZE 'SEKRETNA LICZBA'")
    print("SPRÓBUJ ODGADNĄĆ LICZBĘ WYLOSOWANĄ PRZEZ KOMPUTER")

    print("WYBIERZ POZIOM TRUDNOŚCI:")
    print("1 => ŁATWY (Liczba jednocyfrowa, ilość prób: 2)")
    print("2 => ŚREDNI (Liczba dwucyfrowa, ilość prób: 5)")
    print("3 => TRUDNY (Liczba trzycyfrowa, ilość prób: 8)")

    # Definiowanie dostępnych poziomów trudności
    poziom_trudnosci = validate_input("WYBIERZ 1, 2 LUB 3: ", ["1", "2", "3"])

    # Wybór odpowiedniego zakresu liczb i liczby prób
    if poziom_trudnosci == "1":
        zakres_liczb = range(1, 10)
        liczba_prob = 2
    elif poziom_trudnosci == "2":
        zakres_liczb = range(1, 100)
        liczba_prob = 5
    else:
        zakres_liczb = range(100, 1000)
        liczba_prob = 8

    # Wylosowanie liczby
    liczba = random.choice(zakres_liczb)

    # Uruchomienie gry
    for i in range(1, liczba_prob + 1):
        print(f"Pozostało ci {liczba_prob - i + 1} prób.")
        gracz = validate_guess(f"Zgadnij liczbę od 1 do {max(zakres_liczb)}: ", zakres_liczb)

        if gracz == liczba:
            print("Brawo, udało Ci się zgadnąć ukrytą liczbę!")
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