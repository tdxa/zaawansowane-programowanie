from typing import Union

from models.developer import Developer


class Nieruchomosc:
    def __init__(self, powierzchnia: float, wlasciciel: Union[Developer, str], rok_budowy: int, cena: float):
        self._powierzchnia = powierzchnia
        self._wlasciciel = wlasciciel
        self._rok_budowy = rok_budowy
        self._cena = cena

    @property
    def powierzchnia(self) -> float:
        return self._powierzchnia

    @powierzchnia.setter
    def powierzchnia(self, powierzchnia: float):
        self._powierzchnia = powierzchnia

    @property
    def wlasciciel(self) -> Union[Developer, str]:
        return self._wlasciciel

    @wlasciciel.setter
    def wlasciciel(self, wlasciciel: Union[Developer, str]):
        self._wlasciciel = wlasciciel

    @property
    def rok_budowy(self) -> int:
        return self._rok_budowy

    @rok_budowy.setter
    def rok_budowy(self, rok_budowy: int):
        self._rok_budowy = rok_budowy

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, cena: float):
        self._cena = cena

    def __str__(self) -> str:
        return f'Powierzchnia: {self._powierzchnia},\n' \
               f'Własciciel: {self._wlasciciel},\n' \
               f'Rok budowy: {self._rok_budowy},\n' \
               f'Cena: {self._cena},\n'
