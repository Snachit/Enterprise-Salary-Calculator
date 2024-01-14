from ClassEmploye import *
class Formateur(Employe):
    _remunerationHSup = 70.00

    def __init__(self, nom="", dateNaissance=datetime(2000, 1, 1), dateEmbauche=None, salaireBase=0, heureSup=0):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._heureSup = heureSup

    @property
    def RemunerationHSup(self):
        return Formateur._remunerationHSup

    @RemunerationHSup.setter
    def RemunerationHSup(self, value):
        Formateur._remunerationHSup = value

    @property
    def HeureSup(self):
        return self._heureSup

    @HeureSup.setter
    def HeureSup(self, value):
        self._heureSup = value

    def SalaireAPayer(self):
        nbreHS = self._heureSup
        if nbreHS >= 30:
            nbreHS = 30
        return (self._salaireBase + nbreHS * Formateur._remunerationHSup) * (1 - IR.getIR(self._salaireBase * 12))

    def __str__(self):
        return super().__str__() + "-" + str(self._heureSup)