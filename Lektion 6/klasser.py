import re


class Materiale():
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal

    def tostring(self):
        s = self.titel + " er et materiale fra " + str(self.aarstal) + " med idnr: " + str(self.idnr) + ". Der er " + \
            str(self.antal) + " hvoraf " + str(self.antaludlaan) + " er udlånt."
        return s

    def kan_udlaanes(self):
        if self.antaludlaan < self.antal:
            return True
        else:
            return False

    def udlaan(self):
        if self.kan_udlaanes():
            self.antaludlaan+=1
            return "Du har lånt 1 eksemplar"
        else:
            return "Der er ikke flere eksemplarer"

    def match_titel(self,search_term):
        if re.search(search_term, self.titel, re.IGNORECASE):
            return True, search_term + " fundet i " + self.titel
        else:
            return False, search_term + " ikke fundet"


class Bog(Materiale):
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900,antalsider = 100,
                 forfatter = "Mangler Forfatter"):
        super().__init__(idnr,titel,antal,antaludlaan,aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def tostring(self):
        s = self.titel + " er en bog af " +self.forfatter+ " fra "+ str(self.aarstal) + " med idnr: " + str(self.idnr)\
            + ". Der er " + str(self.antal) + " hvoraf " + str(self.antaludlaan) + " er udlånt. Den har "\
            +str(self.antalsider)+" sider."
        return s

class Film(Materiale):
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900,
                 instruktor= "Mangler Instruktør",lengde=120):
        super().__init__(idnr,titel,antal,antaludlaan,aarstal)
        self.instruktor = instruktor
        self.lengde = lengde

    def tostring(self):
        s = self.titel + " er en film instrueret af " +self.instruktor+ " fra "+ str(self.aarstal) + " med idnr: " \
            + str(self.idnr) + ". Der er " + str(self.antal) + " hvoraf " + str(self.antaludlaan) \
            + " er udlånt. Den varer " + str(self.lengde) + " minutter."
        return s

