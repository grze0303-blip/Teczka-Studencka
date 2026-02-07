for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


////////////////////


zakupy = []

while True:
    produkt = input("Podaj produkt (lub wpisz 'koniec' aby zakończyć): ")
    if produkt.lower() == "koniec":
        break
    zakupy.append(produkt)

print("Twoja lista zakupów:")
for item in zakupy:
    print(item)


/////////////////////



wejscie = input("Podaj tagi oddzielone przecinkami: ")

tagi = wejscie.split(",")
oczyszczone = []

for tag in tagi:
    oczyszczone.append(tag.strip())

unikalne = set(oczyszczone)

print("Liczba wszystkich podanych tagów:", len(oczyszczone))
print("Liczba unikalnych tagów:", len(unikalne))
print("Unikalne tagi (alfabetycznie):")

for tag in sorted(unikalne):
    print("-", tag)

////////////////////////


kontakty = {}

while True:
    print("1 - Dodaj kontakt")
    print("2 - Wyświetl kontakty")
    print("3 - Zakończ")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        imie = input("Podaj imię: ")
        numer = input("Podaj numer telefonu: ")
        kontakty[imie] = numer
    elif wybor == "2":
        if len(kontakty) == 0:
            print("Brak zapisanych kontaktów")
        else:
            print("Lista kontaktów:")
            for klucz, wartosc in kontakty.items():
                print(klucz, "->", wartosc)
    elif wybor == "3":
        break
    else:
        print("Niepoprawna opcja")

///////////////////////

pracownicy = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 6000},
    {"imie": "Jan", "stanowisko": "Manager", "pensja": 9000},
    {"imie": "Kasia", "stanowisko": "Specjalista", "pensja": 6500},
    {"imie": "Tomasz", "stanowisko": "Dyrektor", "pensja": 12000}
]

suma = 0
for pracownik in pracownicy:
    suma += pracownik["pensja"]

srednia = suma / len(pracownicy)
print("Średnia pensja:", srednia)

najwiecej = pracownicy[0]
for pracownik in pracownicy:
    if pracownik["pensja"] > najwiecej["pensja"]:
        najwiecej = pracownik

print("Najlepiej zarabia:", najwiecej)

print("Specjaliści:")
for pracownik in pracownicy:
    if pracownik["stanowisko"] == "Specjalista":
        print(pracownik["imie"])

