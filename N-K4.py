plik = open("dziennik.txt", "w")
plik.write("Pierwszy wpis.\n")
plik.write("Wszystko działa.\n")
plik.close()

plik = open("dziennik.txt", "r")
zawartosc = plik.read()
print("Zawartość po zapisie:")
print(zawartosc)
plik.close()

plik = open("dziennik.txt", "a")
plik.write("Dodaję kolejną linię.\n")
plik.close()

plik = open("dziennik.txt", "r")
zawartosc = plik.read()
print("Zawartość po dopisaniu:")
print(zawartosc)
plik.close()

/////////////////////
from datetime import datetime

plik = open("wiek.txt", "w")
plik.write("25")
plik.close()

def oblicz_rok_urodzenia(sciezka_pliku):
    try:
        plik = open(sciezka_pliku, "r")
        zawartosc = plik.read()
        plik.close()
        wiek = int(zawartosc)
        aktualny_rok = datetime.now().year
        rok_urodzenia = aktualny_rok - wiek
        print("Rok urodzenia:", rok_urodzenia)
    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku!")
    except ValueError:
        print("BŁĄD: Zawartość pliku nie jest poprawną liczbą!")

oblicz_rok_urodzenia("wiek.txt")
oblicz_rok_urodzenia("zla_sciezka.txt")

plik = open("wiek.txt", "w")
plik.write("abc")
plik.close()

oblicz_rok_urodzenia("wiek.txt")

//////////////////////
with open("dziennik_with.txt", "w") as plik:
    plik.write("Pierwszy wpis.\n")
    plik.write("Wszystko działa.\n")

with open("dziennik_with.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość po zapisie:")
    print(zawartosc)

with open("dziennik_with.txt", "a") as plik:
    plik.write("Dodaję kolejną linię.\n")

with open("dziennik_with.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość końcowa:")
    print(zawartosc)

/////////////////////////

class NiepoprawnaIloscProduktuError(ValueError):
    pass

def dodaj_do_koszyka(produkt, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscProduktuError("Ilość produktów musi być dodatnia!")
    print(f"Dodano do koszyka: {produkt} (ilość: {ilosc})")

dodaj_do_koszyka("Jabłko", 3)

try:
    dodaj_do_koszyka("Banan", -2)
except NiepoprawnaIloscProduktuError as e:
    print("Błąd podczas dodawania do koszyka:", e)

////////////////


def zlicz_bledy(sciezka_pliku):
    liczba_bledow = 0
    try:
        with open(sciezka_pliku, "r") as plik:
            for linia in plik:
                try:
                    poziom, wiadomosc = linia.strip().split(":", 1)
                    if poziom == "ERROR":
                        liczba_bledow += 1
                except ValueError:
                    continue
        return liczba_bledow
    except FileNotFoundError:
        return 0


print(zlicz_bledy("log.txt"))



///////////////////////

import pickle

class StanGry:
    def __init__(self, nazwa_gracza, punkty, ekwipunek):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return f"StanGry(nazwa_gracza='{self.nazwa_gracza}', punkty={self.punkty}, ekwipunek={self.ekwipunek})"


stan = StanGry("Aragorn", 1500, ["Miecz", "Tarcza", "Mikstura"])

with open("stan_gry.pkl", "wb") as f:
    pickle.dump(stan, f)

with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

print(wczytany_stan)
print(type(wczytany_stan))


//////////////////
import csv

with open("pracownicy.csv", "w", newline="") as f:
    f.write("imie,stanowisko,pensja\n")
    f.write("Anna,Specjalista,6000\n")
    f.write("Jan,Manager,9000\n")
    f.write("Kasia,Specjalista,abc\n")
    f.write("Tomasz,Dyrektor,12000\n")

def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    wyniki = []
    try:
        with open(sciezka_pliku, "r", newline="") as plik:
            reader = csv.DictReader(plik)
            for wiersz in reader:
                try:
                    wiersz["pensja"] = int(wiersz["pensja"])
                    wyniki.append(wiersz)
                except ValueError:
                    continue
        return wyniki
    except FileNotFoundError:
        return []

pracownicy = wczytaj_pracownikow("pracownicy.csv")
print(pracownicy)

////////////////////////
import csv

sprzedaz = [
    {"produkt": "Jabłko", "sprzedana_ilosc": 120, "przychody": 360.0},
    {"produkt": "Banan", "sprzedana_ilosc": 80, "przychody": 280.0},
    {"produkt": "Pomarańcza", "sprzedana_ilosc": 65, "przychody": 325.0}
]

def zapisz_raport_sprzedazy(sciezka_pliku: str, dane: list):
    if not dane:
        print("Brak danych do zapisania")
        return

    pola = list(dane[0].keys())

    with open(sciezka_pliku, "w", newline="") as plik:
        writer = csv.DictWriter(plik, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane)

zapisz_raport_sprzedazy("raport.csv", sprzedaz)
print("Zapisano raport do pliku raport.csv")

//////////////////////////


import json

with open("konfiguracja.json", "w") as f:
    f.write("""
{
    "aplikacja": {
        "nazwa": "MojaAplikacja",
        "wersja": "1.0"
    },
    "baza_danych": {
        "host": "localhost",
        "port": 5432,
        "uzytkownik": "admin",
        "haslo": "tajne"
    }
}
""")

def wczytaj_konfiguracje(sciezka_pliku: str) -> dict:
    try:
        with open(sciezka_pliku, "r") as plik:
            dane = json.load(plik)
        return dane
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

konfiguracja = wczytaj_konfiguracje("konfiguracja.json")

if konfiguracja:
    print(konfiguracja["baza_danych"]["uzytkownik"])
else:
    print("Nie udało się wczytać konfiguracji")

/////////////


import json

moje_dane = {
    "imie": "Jan",
    "wiek": 30,
    "ulubiony_kolor": "żółty",
    "miasto": "Kraków"
}

def zapisz_jako_json(dane: dict | list, sciezka_pliku: str):
    try:
        with open(sciezka_pliku, "w", encoding="utf-8") as plik:
            json.dump(dane, plik, indent=4, ensure_ascii=False)
        print("Dane zostały poprawnie zapisane do pliku JSON")
    except IOError:
        print("BŁĄD: Nie udało się zapisać danych do pliku")

zapisz_jako_json(moje_dane, "dane.json")


////////////////////


import json
from pydantic import BaseModel, ValidationError

with open("produkt.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "nazwa_produktu": "Laptop Pro",
            "id_produktu": "LP-2026-001",
            "cena": 4999.99,
            "dostepny": True,
            "tagi": ["laptop", "praca", "premium"],
            "specyfikacja": {
                "procesor": "Intel Core i7",
                "ram_gb": 16
            }
        },
        f,
        indent=4,
        ensure_ascii=False
    )

class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int

class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel

def wczytaj_i_waliduj_produkt(sciezka: str) -> ProduktModel | None:
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            dane = json.load(f)
        produkt = ProduktModel.parse_obj(dane)
        return produkt
    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku!")
        return None
    except json.JSONDecodeError:
        print("BŁĄD: Niepoprawny format JSON!")
        return None
    except ValidationError as e:
        print("BŁĄD WALIDACJI:", e)
        return None

produkt = wczytaj_i_waliduj_produkt("produkt.json")

if produkt is not None:
    print(produkt.nazwa_produktu)
    print(produkt.specyfikacja.procesor)

//////////////////////////


