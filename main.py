class Osoba:
    def __init__(self, imie: str, nazwisko: str):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Pojazd:
    def __init__(self, marka: str, model: str, rocznik: int, przejechane_kilometry: int, data_zakupu: str):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przejechane_kilometry = przejechane_kilometry
        self.data_zakupu = data_zakupu

    def __str__(self):
        return f"Marka {self.marka}, " \
               f"model: {self.model}, " \
               f"rocznik {self.rocznik}, " \
               f"przejechane kilometry: {self.przejechane_kilometry}"


class Firma:
    def __init__(self, nazwa: str, rok_zalozenia: int, wlasiciel: Osoba, adres: str):
        self.nazwa = nazwa
        self.rok_zalozenia = rok_zalozenia
        self.wlasciciel = wlasiciel
        self.adres = adres

    def __str__(self):
        return f"Firma {self.nazwa} założona w {self.rok_zalozenia} " \
               f"przez {self.wlasciciel} znajduje się {self.adres}"


class FirmaTransportowa(Firma):
    def __init__(self, pojazdy: list[Pojazd], nazwa: str, rok_zalozenia: int, wlasiciel: Osoba, adres: str):
        super().__init__(nazwa, rok_zalozenia, wlasiciel, adres)
        self.pojazdy = pojazdy


class Odcinek:
    def __init__(self, dlugosc, stacja_poczatkowa: str, stacja_koncowa: str):
        self.dlugosc = dlugosc
        self.stacja_poczatkowa = stacja_poczatkowa
        self.stacja_koncowa = stacja_koncowa

    def __str__(self):
        return f"Odcinek ma długość {self.dlugosc}. " \
               f"Zaczyna się w {self.stacja_poczatkowa} i kończy w {self.stacja_koncowa}"

    @property
    def dlugosc(self):
        return self.dlugosc

    @dlugosc.setter
    def dlugosc(self, value):
        self._dlugosc = value

    @property
    def stacja_poczatkowa(self):
        return self.stacja_poczatkowa

    @stacja_poczatkowa.setter
    def stacja_poczatkowa(self, value):
        self._stacja_poczatkowa = value

    @property
    def stacja_koncowa(self):
        return self.stacja_koncowa

    @stacja_koncowa.setter
    def stacja_koncowa(self, value):
        self._stacja_koncowa = value


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa: str, rok_zalozenia: int, wlasiciel: Osoba, adres: str):
        super().__init__(nazwa, rok_zalozenia, wlasiciel, adres)


class Kurs:
    def __init__(self, data: str, pracownik: Osoba, pojazd: Pojazd,
                 odcinki: list[Odcinek], klient: FirmaSpozywcza,
                 wykonawca: FirmaTransportowa):
        self.set_data(data)
        self.set_wykonawca(wykonawca)
        self.set_pracownik(pracownik)
        self.set_pojazd(pojazd)
        self.set_odcinki(odcinki)
        self.set_klient(klient)

    def set_data(self, data):
        self.data = data

    def set_wykonawca(self, wykonawca):
        self.wykonawca = wykonawca

    def set_pracownik(self, pracownik):
        self.pracownik = pracownik

    def set_pojazd(self, pojazd):
        self.pojazd = pojazd

    def set_odcinki(self, odcinki):
        self.odcinki = odcinki

    def set_klient(self, klient):
        self.klient = klient

    def suma_kilometrow(self):
        suma = 0
        for odcinek in self.odcinki:
            suma += odcinek.dlugosc
        return suma

    def marka_smachodu(self):
        return self.pojazd.marka

    def __str__(self):
        return f"Kurs.\n" \
               f"Data: {self.data}\n" \
               f"Przydzielony pracownik: {self.pracownik}\n" \
               f"Pojazd: {self.marka_smachodu()}\n" \
               f"Wykonawca: {self.wykonawca}\n" \
               f"Klient: {self.klient}\n" \
               f"Długość kursu: {self.suma_kilometrow()} km"


odcinek1 = Odcinek(15, "Katowice", "Ruda śląska")
odcinek2 = Odcinek(350, "Chorzów", "Wrocław")
odcinek3 = Odcinek(5, "Katowice", "Chorzów")

pracownik = Osoba("Andrzej", "Kowalski")
wlasicciel_transportowa = Osoba("Bogdan", "Chmielewski")
auto_firmowe1 = Pojazd("Toyota", "Yaris", 2008, 908562, "03-05-2017")
auto_firmowe2 = Pojazd("Toyota", "Yaris", 2010, 908962, "03-05-2018")

wykonawca = FirmaTransportowa([auto_firmowe1, auto_firmowe2],
                              "Transporterek",
                              2016,
                              wlasicciel_transportowa,
                              "Warsawska 12, Katowicec")

wlasciciel_spozywcza = Osoba("Agata", "Błędniak")

klient = FirmaSpozywcza("Pomidorek", 2010, wlasciciel_spozywcza, "Wawelska 10, Ruda Śląska")
kurs = Kurs("22-03-2021",
            pracownik,
            auto_firmowe1,
            [odcinek1, odcinek2, odcinek3],
            klient,
            wykonawca)

print(kurs)
