from typing import Union

from models.developer import Developer


class Zamowienie:
    def __init__(self, sprzedajacy: Union[Developer, str], kupujacy: Union[Developer, str], zawartosc):
        self._sprzedajacy = sprzedajacy
        self._kupujacy = kupujacy
        self._zawartosc = zawartosc
        self._wartosc = self.oblicz_wartosc()

    @property
    def sprzedajacy(self) -> Union[Developer, str]:
        return self._sprzedajacy

    @sprzedajacy.setter
    def sprzedajacy(self, sprzedajacy: Union[Developer, str]):
        self._sprzedajacy = sprzedajacy

    @property
    def kupujacy(self) -> Union[Developer, str]:
        return self._kupujacy

    @kupujacy.setter
    def kupujacy(self, kupujacy: Union[Developer, str]):
        self._kupujacy = kupujacy

    @property
    def wartosc(self) -> float:
        return self._wartosc

    @wartosc.setter
    def wartosc(self, wartosc: float):
        self._wartosc = wartosc

    @property
    def zawartosc(self) -> list:
        return self._zawartosc

    @zawartosc.setter
    def zawartosc(self, zawartosc: list):
        self._zawartosc = zawartosc

    def oblicz_wartosc(self):
        return round(sum(nieruchomosc.cena for nieruchomosc in self.zawartosc), 2)

    def oblicz_laczna_pwoierzchnie(self):
        return sum(nieruchomosc.powierzchnia for nieruchomosc in self.zawartosc)

    def __str__(self) -> str:
        return f'-----Sprzedaje: {self._sprzedajacy},\n' \
               f'-----Kupuje: {self._kupujacy},\n' \
               f'-----Wartosc zamowienia: {self.oblicz_wartosc()} zł,\n' \
               f'-----Zawartosc: \n' + '\n'.join(str(nieruchomosc) for nieruchomosc in self.zawartosc)
