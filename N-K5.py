def srednia_kroczaca():
    suma = 0.0
    licznik = 0
    while True:
        nowa_liczba = yield
        if nowa_liczba is not None:
            suma += nowa_liczba
            licznik += 1
            print(suma / licznik)

korutyna = srednia_kroczaca()
next(korutyna)

korutyna.send(10)
korutyna.send(20)
korutyna.send(30)
korutyna.send(40)

///////////////////



class ResetKorutyny(Exception):
    pass

def korutyna(f):
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        next(g)
        return g
    return wrapper

@korutyna
def srednia_kroczaca():
    suma = 0.0
    licznik = 0
    while True:
        try:
            nowa_liczba = yield
            if nowa_liczba is not None:
                suma += nowa_liczba
                licznik += 1
                print(suma / licznik)
        except ResetKorutyny:
            suma = 0.0
            licznik = 0
            print("Zresetowano korutynę")

kalkulator = srednia_kroczaca()

kalkulator.send(10)
kalkulator.send(20)
kalkulator.send(30)

kalkulator.throw(ResetKorutyny)

kalkulator.send(5)
kalkulator.send(15)

/////////////////////

class ResetProcesora(Exception):
    pass

def korutyna(f):
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        next(g)
        return g
    return wrapper

@korutyna
def procesor_polecen():
    dane = []
    while True:
        try:
            polecenie = yield
            if polecenie is None:
                continue

            if polecenie.strip() == "POKAZ":
                print(dane)
                continue

            try:
                akcja, wartosc = polecenie.split(":", 1)
            except ValueError:
                print("Niepoprawne polecenie")
                continue

            akcja = akcja.strip().upper()
            wartosc = wartosc.strip()

            if akcja == "DODAJ":
                dane.append(wartosc)
            elif akcja == "USUN":
                if wartosc in dane:
                    dane.remove(wartosc)
            else:
                print("Nieznana akcja")
        except ResetProcesora:
            dane = []
            print("Zresetowano procesor")

procesor = procesor_polecen()

procesor.send("DODAJ:jabłko")
procesor.send("DODAJ:banan")
procesor.send("DODAJ:gruszka")
procesor.send("POKAZ")
procesor.send("USUN:banan")
procesor.send("POKAZ")
procesor.throw(ResetProcesora)
procesor.send("POKAZ")

///////////////////

class Odliczanie:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        aktualna = self.start
        while aktualna > 0:
            yield aktualna
            aktualna -= 1
        yield "START!"

odliczanie_do_startu = Odliczanie(5)

for wartosc in odliczanie_do_startu:
    print(wartosc)

//////////////////////


class LicznikJednorazowy:
    def __init__(self, max_val):
        self.max = max_val
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            wartosc = self.n
            self.n += 1
            return wartosc
        else:
            raise StopIteration


licznik = LicznikJednorazowy(3)

print("Pierwsza iteracja:")
for x in licznik:
    print(x)

print("Druga iteracja:")
for x in licznik:
    print(x)

////////////////////////


