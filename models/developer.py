class Developer:
    def __init__(self, nazwa: str, telefon: int, email: str):
        self._nazwa = nazwa
        self._telefon = telefon
        self._email = email

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nazwa: str):
        self._nazwa = nazwa

    @property
    def telefon(self) -> int:
        return self._telefon

    @telefon.setter
    def telefon(self, telefon: int):
        self._telefon = telefon

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    def __str__(self) -> str:
        return f'Nazwa developera: {self._nazwa},\n' \
               f'Telefon: {self._telefon},\n' \
               f'Email: {self._email}'
