from models.developer import Developer
from models.dom import Dom

from models.mieszkanie import Mieszkanie
from models.zamowienie import Zamowienie

developer = Developer("TomBuD Nieruchomości", 785692365, "tomasz@tombud.com")

dom = Dom(2500, True, 154, "Andrzej Nowak", 2017, 860000)
mieszkanie = Mieszkanie(4, False, True, 57, "Adam Kowalski", 2011, 120000)
kawalerka = Mieszkanie(1, False, False, 38, "Grażyna Motko", 2010, 100000)

zamowienie = Zamowienie(developer, "Anna Domańska", [dom, mieszkanie, kawalerka])

print(zamowienie.__str__())
print(zamowienie.oblicz_laczna_pwoierzchnie())

print("łaczna kwota zamowienia:", zamowienie.oblicz_wartosc())
print("łaczna powierzchnia mieszkalna:", zamowienie.oblicz_laczna_pwoierzchnie())
