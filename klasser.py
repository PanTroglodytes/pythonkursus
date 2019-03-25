import re


class Materiale():
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900, reservationer = 0):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal
        self.reservationer = reservationer

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
            self.antaludlaan += 1
            return True
        else:
            return False

    def kan_afleveres(self):
        if self.antaludlaan > 0:
            return True
        else:
            return False

    def aflevere(self):
        if self.kan_afleveres():
            self.antaludlaan -= 1
            return True
        else:
            return False

    def match_titel(self,search_term):
        if re.search(search_term, self.titel, re.IGNORECASE):
            return True
        else:
            return False



class Bog(Materiale):
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900,antalsider = 100,
                 forfatter = "Mangler Forfatter", reservationer = 0):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal, reservationer)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def tostring(self):
        s = "Bog".ljust(5) + self.titel.ljust(35) + "Forfatter:".ljust(12) +self.forfatter.ljust(22)+ "År: "+ str(self.aarstal) \
        + " ID: " + str(self.idnr) + " Sider:".ljust(11) + str(self.antalsider) + " Inventar: " + str(self.antal).ljust(3) \
        + " Udlånt: " + str(self.antaludlaan).ljust(3) + "Res.: " + str(self.reservationer)
        return s

class Film(Materiale):
    def __init__(self,idnr = 0,titel = "Mangler titel",antal = 1,antaludlaan = 0,aarstal = 1900,
                 instruktor= "Mangler Instruktør",lengde=120, reservationer = 0):
        super().__init__(idnr,titel,antal,antaludlaan,aarstal, reservationer)
        self.instruktor = instruktor
        self.lengde = lengde

    def tostring(self):
        s = "Film".ljust(5) + self.titel.ljust(35) + "Instruktør:".ljust(12) +self.instruktor.ljust(22)+ "År: "+ str(self.aarstal) \
            + " ID: " + str(self.idnr) + " Minutter:".ljust(11) + str(self.lengde).ljust(3) + " Inventar: " + str(self.antal).ljust(3) \
            + " Udlånt: " + str(self.antaludlaan).ljust(3) + "Res.: " + str(self.reservationer)

        return s

class CD(Materiale):
    def __init__(self, idnr = 0, titel = "Mangler titel", antal = 1, antaludlaan = 0, aarstal = 1990,
                 kunstner = "Mangler kunstner", tracks = 12, reservationer = 0):
        super().__init__(idnr,titel,antal,antaludlaan,aarstal, reservationer)
        self.kunstner = kunstner
        self.tracks = tracks

    def tostring(self):
        s = "CD".ljust(5) + self.titel.ljust(35) + "Kunstner:".ljust(12) +self.kunstner.ljust(22)+ "År: "+ str(self.aarstal) \
            + " ID: " + str(self.idnr) + " Tracks: ".ljust(11) + str(self.tracks).ljust(3) + " Inventar: " + str(self.antal).ljust(3) \
            + " Udlånt: " + str(self.antaludlaan).ljust(3) + "Res.: " + str(self.reservationer)

        return s