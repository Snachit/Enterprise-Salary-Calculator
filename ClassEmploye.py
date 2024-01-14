from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Employe(ABC):
    cpt = 0

    def __init__(self, nom="", dateNaissance=datetime(2000, 1, 1), dateEmbauche=None, salaireBase=0):
        self._nom = nom
        self._dateNaissance = dateNaissance
        self._salaireBase = salaireBase
        Employe.cpt += 1
        self._mtle = Employe.cpt
        self._dateEmbauche = datetime.now() if dateEmbauche is None else dateEmbauche
        self.check_age_at_embauche()

    @property
    def Matricule(self):
        return self._mtle

    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        self._nom = value

    @property
    def DateNaissance(self):
        return self._dateNaissance

    @DateNaissance.setter
    def DateNaissance(self, value):
        self._dateNaissance = value

    @property
    def DateEmbauche(self):
        return self._dateEmbauche

    @DateEmbauche.setter
    def DateEmbauche(self, value):
        self._dateEmbauche = value
        self.check_age_at_embauche()

    @property
    def SalaireBase(self):
        return self._salaireBase

    @SalaireBase.setter
    def SalaireBase(self, value):
        self._salaireBase = value

    def check_age_at_embauche(self):
        age_at_embauche = (self._dateEmbauche - self._dateNaissance).days / 365
        if age_at_embauche < 16:
            raise ValueError("L'âge au recrutement doit être supérieur à 16 ans")

    @abstractmethod
    def SalaireAPayer(self):
        pass

    def Age(self):
        return int((datetime.now() - self._dateNaissance).days / 365)

    def Anciennete(self):
        return int((datetime.now() - self._dateEmbauche).days / 365)

    def DateRetraite(self, ageRetraite):
        return self._dateNaissance + timedelta(days=ageRetraite * 365)

    def __str__(self):
        return f"{self._mtle}-{self._nom}-{self._dateNaissance.strftime('%d/%m/%Y')}-{self._dateEmbauche.strftime('%d/%m/%Y')}-{self._salaireBase}"

    def __eq__(self, other):
        if not isinstance(other, Employe):
            return False
        return self._mtle == other._mtle