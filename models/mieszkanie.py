from typing import Union

from models.developer import Developer
from models.nieruchomosc import Nieruchomosc


class Mieszkanie(Nieruchomosc):
    def __init__(self, pietro: int, miejsce_parkingowe: bool, balkon: bool, powierzchnia: float,
                 wlasciciel: Union[Developer, str],
                 rok_budowy: int, cena: float):
        super().__init__(powierzchnia, wlasciciel, rok_budowy, cena)
        self._pietro = pietro
        self._miejsce_parkingowe = miejsce_parkingowe
        self._balkon = balkon

    @property
    def pietro(self) -> int:
        return self._pietro

    @pietro.setter
    def pietro(self, pietro: int):
        self._pietro = pietro

    @property
    def miejsce_parkingowe(self) -> bool:
        return self._miejsce_parkingowe

    @miejsce_parkingowe.setter
    def miejsce_parkingowe(self, miejsce_parkingowe: bool):
        self._miejsce_parkingowe = miejsce_parkingowe

    @property
    def balkon(self) -> bool:
        return self._balkon

    @balkon.setter
    def balkon(self, balkon: bool):
        self._balkon = balkon

    def __str__(self) -> str:
        return super(Mieszkanie, self).__str__() + f'Pietro: {self._pietro},\n' \
                                                   f'Miejsce parkingowe: {self._miejsce_parkingowe},\n' \
                                                   f'Balkon: {self._balkon},\n'
