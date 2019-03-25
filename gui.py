from tkinter import *
from tkinter import messagebox
import klasser as k

# Dette er objekterne, der kan lånes og afleveres
bog1 = k.Bog(12345680, "Python Crash Course", 1, 0, 2016, 525, "Eric Matthes")
bog2 = k.Bog(12345687, "Teach Yourself SQL in 24 Hours", 10, 5, 2011, 473, "Ryan Stephens")
bog3 = k.Bog(12343300, "TCP/IP-bogen", 2, 0, 2004, 270, "Jakob Mose")
film1 = k.Film(12345681, "Alien", 15, 2, 1978, "Ridley Scott", 124)
film2 = k.Film(12388745, "Robocop", 1, 0, 1987, "Paul Verhoeven", 102)
film3 = k.Film(98765422, "Over the Top", 900, 0, 1987, "Menahem Golan", 93)
cd1 = k.CD(87325489, "Flood", 2, 1, 1990, "They Might Be Giants", 19)
cd2 = k.CD(36456484, "Tusk", 3, 2, 1979, "Fleetwood Mac", 20)
cd3 = k.CD(98374573, "Dark Side of the Moon", 19, 10, 1973, "Pink Floyd", 10)

# Dette er en liste over objekterne
listMaterialer = [bog1, bog2, bog3, film1, film2, film3, cd1, cd2, cd3]

# Dette er en passworddatabase, der bruges når man vil slette et objekt
password_db = ['password123']
admin_rights = ['False']

# Dette er en funktion, der laver error-popup
def error_message(error_string):
    print("Error: " + error_string)
    messagebox.showerror("Error!", error_string)


# Denne funktion foretager et opslag i bibliotekets database, bruges både ved aflevering, sletning og udlån.
# Den returnerer objektet eller int0 hvis søgningen ikke har resultat
def database_id_lookup(materialeid, materialeliste):
    output = 0
    while output == 0:
        for mat in materialeliste:
            if str(mat.idnr) == materialeid:
                output = mat
        break
    print(output)
    return output

class Application(Frame):

# udlånsfunktionen bruger lookup-funktionen til at finde den ønskede bog. Der foretages check på om materialet findes,
# om det er tilgængeligt, om det er reserveret, og i så fald om låneren har en reservation
    def udlaan(self):
        idnr = self.id_entry.get()
        print("id der skal lånes: " + idnr)
        self.listGui.delete('1.0', END)
        lookup = database_id_lookup(idnr, listMaterialer)
        if not isinstance(lookup, k.Materiale):
            error_message("Ugyldigt ID!")
        else:
            if lookup.kan_udlaanes():
                if lookup.reservationer > 0:
                    reply = messagebox.askquestion("Materialet er reserveret", "Dette materiale kan kun lånes, "
                                           "hvis du har en reservation. \nHar du en reservation?")
                    if reply == 'yes' and lookup.kan_udlaanes():
                        lookup.udlaan()
                        lookup.reservationer -= 1
                    else:
                        print("nej til reservation")
                        self.vis_hele_listen()
                else:
                    lookup.udlaan()
            else:
                error_message("Kan ikke udlånes!")
        self.listGui.delete('1.0', END)
        self.vis_hele_listen()

# aflever-funktionen bruger lookup til at finde materialet, og der foretages check på,
# om der er udlånt eksemplarer, ved hjælp af kan_afleveres-funktionen indbygget i materialeklassen
    def aflever(self):
        idnr = self.aflever_entry.get()
        print("id der skal afleveres: " + idnr)
        self.listGui.delete('1.0', END)
        lookup = database_id_lookup(idnr, listMaterialer)
        if not isinstance(lookup, k.Materiale):
            error_message("Ugyldigt ID!")
        else:
            if lookup.kan_afleveres():
                lookup.aflevere()
            else:
                error_message("Kan ikke afleveres!")
        self.listGui.delete('1.0', END)
        self.vis_hele_listen()

# Søgefunktionen sammensætter en tekststreng af de søgbare felter, og sætter materialet ind i text-widget'en hvis
# søgestreng er fundet
    def sog_i_listen(self):
        search_text = self.entry.get()
        print("søge tekst: "+search_text)
        if search_text == '':
            error_message("Tom søgestreng!")
            return
        self.listGui.delete('1.0', END)

        for mat in listMaterialer:
            searchable_terms = ""
            searchable_terms += mat.titel + "\n"
            searchable_terms += str(mat.aarstal) + "\n"
            if isinstance(mat, k.Bog):
                searchable_terms += mat.forfatter + "\n"
            if isinstance(mat, k.Film):
                searchable_terms += mat.instruktor + "\n"
            if isinstance(mat, k.CD):
                searchable_terms += mat.kunstner + "\n"
            if search_text.lower() in searchable_terms.lower():
                self.listGui.insert(INSERT, mat.tostring()+"\n")
                print(searchable_terms)

# Denne funktionen sætter hele materialelisten ind i text-widget'en
    def vis_hele_listen(self):
        print("Vis hele listen")
        self.listGui.delete('1.0', END)
        for mat in listMaterialer:
            self.listGui.insert(INSERT, mat.tostring()+"\n")

# Slette-funktionen bruger lookup-funktionen for at se, om materialet findes. Så er der et check på, om brugeren er
# logget på, og en bekræftelses-popup
    def slet(self):
        idnr = self.slette_entry.get()
        print("id der skal slettes: " + idnr)
        self.listGui.delete('1.0', END)
        lookup = database_id_lookup(idnr, listMaterialer)
        if admin_rights[0] == 'False':
            error_message("Du skal være logget på for at slette.")
        elif not isinstance(lookup, k.Materiale):
            error_message("Ugyldigt ID!")
        else:
            reply = messagebox.askokcancel("Pas på!", "Vil du slette " + str(lookup.titel) + "?")
            if reply:
                listMaterialer.remove(lookup)
                print("materiale slettet")
        self.vis_hele_listen()

# Reservationsfunktionen bruger lookup for at finde materialet. Der er et check på, om man forsøger at reservere
# et materiale, der allerede står på hylden
    def reserver(self):
        idnr = self.reservere_entry.get()
        print("id der skal reserveres: " + idnr)
        self.listGui.delete('1.0', END)
        lookup = database_id_lookup(idnr, listMaterialer)
        if not isinstance(lookup, k.Materiale):
            error_message("Ugyldigt ID!")
        elif lookup.kan_udlaanes():
            error_message("Materialet står på hylden, reservation ikke tilladt")
        else:
            lookup.reservationer += 1
        self.vis_hele_listen()

# Logon-funktionen checker om det password, man skriver ind i feltet står i password-databasen.
# Ændrer i så fald admin_rights
    def logon(self):
        password = self.password_entry.get()
        self.password_entry.delete(0, 'end')
        if password in password_db:
            admin_rights[0] = "True"
        print(admin_rights[0])
        self.status_string.set(" Admin rights: " + admin_rights[0])


    def create_widgets(self):
        frame = Frame(self)
        frame2 = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame,text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
        self.visListe.pack({"side": "left"})

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        # input felt til sletning.
        self.L1 = Label(frame2, text="ID for sletning:")
        self.L1.pack(side=LEFT)
        self.slette_entry = Entry(frame2, bd=5)
        self.slette_entry.pack(side=LEFT)

        # definition og mapping af sletteknap
        self.sletteKnap = Button(frame2, text="Slet")
        self.sletteKnap["command"] = self.slet
        self.sletteKnap.pack({"side": "left"})

        # input felt til reservation.
        self.L1 = Label(frame2, text="ID for reservation:")
        self.L1.pack(side=LEFT)
        self.reservere_entry = Entry(frame2, bd=5)
        self.reservere_entry.pack(side=LEFT)

        # definition og mapping af reservationsknap
        self.reservereKnap = Button(frame2, text="Reservér")
        self.reservereKnap["command"] = self.reserver
        self.reservereKnap.pack({"side": "left"})

        # input felt til password.
        self.L1 = Label(frame2, text="Admin Password:")
        self.L1.pack(side=LEFT)
        self.password_entry = Entry(frame2, bd=5, show='*')
        self.password_entry.pack(side=LEFT)

        # definition og mapping af log_on_knap
        self.logonKnap = Button(frame2, text="Log på")
        self.logonKnap["command"] = self.logon
        self.logonKnap.pack({"side": "left"})

        # admin rights statusfelt
        self.status_string = StringVar()
        self.L1 = Label(frame2, textvariable=self.status_string)
        self.L1.pack(side=LEFT)
        self.status_string.set("Admin rights: " + admin_rights[0])



        # Her definerer vi en Text widget - dvs
        # den kan indeholde multiple linjer
        # ideen er så at hver linje indeholde et styk materiale
        # Nedenunder kan du se hvordan listen af materiale løbes
        # igennem og toString metoden bliver kaldt og så bliver
        # der indsat en ny linje i Text widgeten
        self.listGui = Text(self, width=145)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.tostring()+"\n")
        frame.pack()
        self.listGui.pack()
        frame2.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
