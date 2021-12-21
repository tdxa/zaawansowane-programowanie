from typing import Union

from models.developer import Developer
from models.nieruchomosc import Nieruchomosc


class Dom(Nieruchomosc):
    def __init__(self, powierzchnia_dzialki: float, garaz: bool, powierzchnia: float, wlasciciel: Union[Developer, str],
                 rok_budowy: int,
                 cena: float):
        super().__init__(powierzchnia, wlasciciel, rok_budowy, cena)
        self._powierzchnia_dzialki = powierzchnia_dzialki
        self._garaz = garaz

    @property
    def powierzchnia_dzialki(self) -> float:
        return self._powierzchnia_dzialki

    @powierzchnia_dzialki.setter
    def powierzchnia_dzialki(self, powierzchnia_dzialki: float):
        self._powierzchnia_dzialki = powierzchnia_dzialki

    @property
    def garaz(self) -> bool:
        return self._garaz

    @garaz.setter
    def garaz(self, garaz: bool):
        self._garaz = garaz

    def __str__(self) -> str:
        return super(Dom, self).__str__() + f'Powierzchnia dzialki / ogrodka: {self._powierzchnia_dzialki},\n' \
                                            f'Garaz: {self._garaz},\n'
