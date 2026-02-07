class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

gracz_obj = Gracz("Aragorn", 100)

print(gracz_obj.imie)
print(gracz_obj.hp)



//////////////


class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"{self.imie} otrzymuje {ilosc} obrażeń")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', hp={self.hp})"


gracz = Gracz("Aragorn", 100)

print(gracz)
gracz.pokaz_status()
gracz.otrzymaj_obrazenia(30)
print(gracz)



//////////////////




class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        Gracz.liczba_graczy += 1

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"


print("Liczba graczy przed stworzeniem obiektów:", Gracz.liczba_graczy)

g1 = Gracz("Aragorn", 100)
g2 = Gracz("Legolas", 90)
g3 = Gracz("Gimli", 110)

print("Liczba graczy po stworzeniu obiektów:", Gracz.liczba_graczy)



//////////////////////


class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def __str__(self):
        return f"{super().__str__()}, Siła: {self.sila}"

    def atak(self):
        print(f"{self.imie} atakuje z siłą {self.sila}")


wojownik = Wojownik("Boromir", 120, 25)

print(wojownik)
wojownik.pokaz_status()
wojownik.atak()


////////////////////


class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Mam {self.hp} HP.")


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Jestem Wojownik {self.imie}. Mam {self.hp} HP i siłę {self.sila}.")

    def atak(self):
        print(f"{self.imie} atakuje z siłą {self.sila}")


class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        print(f"Jestem Mag {self.imie}. Mam {self.hp} HP i {self.mana} many.")


druzyna = [
    Gracz("Aragorn", 100),
    Wojownik("Boromir", 120, 25),
    Mag("Gandalf", 80, 200)
]

for postac in druzyna:
    postac.przedstaw_sie()
////////////////


class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Mam {self.hp} HP.")


gracz = Gracz("Aragorn", 100)

print("HP początkowe:", gracz.hp)
gracz.hp = -50
print("HP po ustawieniu -50:", gracz.hp)
///////////////////////

class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        if len(self.przedmioty) == 0:
            print("Ekwipunek jest pusty")
        else:
            print("Ekwipunek:")
            for przedmiot in self.przedmioty:
                print("-", przedmiot)


class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        self.ekwipunek = Ekwipunek()

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Mam {self.hp} HP.")


gracz = Gracz("Aragorn", 100)

gracz.ekwipunek.dodaj_przedmiot("Miecz")
gracz.ekwipunek.dodaj_przedmiot("Tarcza")

gracz.przedstaw_sie()
gracz.ekwipunek.pokaz_przedmioty()
/////////////////////////

class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Mam {self.hp} HP.")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __eq__(self, other):
        if isinstance(other, Gracz) and self.imie == other.imie:
            return True
        return False


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Jestem Wojownik {self.imie}. Mam {self.hp} HP i siłę {self.sila}.")

    def __str__(self):
        return f"Wojownik {self.imie} (HP: {self.hp}, Siła: {self.sila})"

    def __add__(self, other):
        if not isinstance(other, Wojownik):
            return NotImplemented
        nowe_imie = f"{self.imie} i {other.imie}"
        nowe_hp = self.hp + other.hp
        nowa_sila = self.sila + other.sila
        return Wojownik(nowe_imie, nowe_hp, nowa_sila)


g1 = Gracz("Aragorn", 100)
g2 = Gracz("Aragorn", 50)
g3 = Gracz("Legolas", 90)

print(g1 == g2)
print(g1 == g3)

w1 = Wojownik("Aragorn", 100, 20)
w2 = Wojownik("Boromir", 120, 25)

fuzja = w1 + w2
print(fuzja)
fuzja.przedstaw_sie()

////////////////////////////
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}. Mam {self.hp} HP.")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __eq__(self, other):
        if isinstance(other, Gracz) and self.imie == other.imie:
            return True
        return False


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Jestem Wojownik {self.imie}. Mam {self.hp} HP i siłę {self.sila}.")

    def __str__(self):
        return f"Wojownik {self.imie} (HP: {self.hp}, Siła: {self.sila})"

    def __add__(self, other):
        if not isinstance(other, Wojownik):
            return NotImplemented
        nowe_imie = f"{self.imie} i {other.imie}"
        nowe_hp = self.hp + other.hp
        nowa_sila = self.sila + other.sila
        return Wojownik(nowe_imie, nowe_hp, nowa_sila)


g1 = Gracz("Aragorn", 100)
g2 = Gracz("Aragorn", 50)
g3 = Gracz("Legolas", 90)

print(g1 == g2)
print(g1 == g3)

w1 = Wojownik("Aragorn", 100, 20)
w2 = Wojownik("Boromir", 120, 25)

fuzja = w1 + w2
print(fuzja)
fuzja.przedstaw_sie()
