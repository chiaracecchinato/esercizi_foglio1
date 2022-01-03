class Automobile:

    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo=casa_automo
        self.modello=modello
        self.numero_posti=numero_posti
        self.targa=targa


    def __str__(self):
        print('casa automobilistica: "{}"; modello: "{}"; numero posti auto: "{}"; numero targa: "{}"'.format(self.casa_automo, self.modello, self.numero_posti, self.targa))

    def parla(self):
        print("Broom Broom")

    def confronta(self, auto2):
        if self.casa_automo==auto2.casa_automo and self.modello == auto2.modello and self.numero_posti==self.numero_posti:
            print("le 2 auto hanno le stesse caratteristiche")    
        elif self.casa_automo==auto2.casa_automo and self.modello == auto2.modello or self.numero_posti==self.numero_posti:
            print("le 2 auto hanno la casa automobilistica e il modello uguali o il numero di posti d'auto ma non tutte e 3")
        elif self.casa_automo==auto2.casa_automo or self.modello == auto2.modello or self.numero_posti==self.numero_posti:
            print("le 2 auto hanno solo una cosa in comune")
        else:
            print("non hanno nulla in comune")

class Trasformer(Automobile):
    def __init__(self, nome, generazione, grado, reparto):
        Automobile().__init__()
        self.nome=nome
        self.generazione=generazione #num > 0
        self.grado=grado #soldato semplice, sergeente, capitano
        self.reparto=reparto #corpo a corpo, artiglieria leggera, artiglieria pesante, spionaggio
    
    def scheda_militare(self):
        print('grado: "{}"; reparto: "{}"'.format(self.grado, self.reparto))
        
my_auto1=Automobile(casa_automo="GG", modello="XT", numero_posti=5, targa="ASDFG")

my_auto2=Automobile(casa_automo="GG", modello="XT", numero_posti=5, targa="ASDFG")

my_auto1.__str__()
my_auto1.parla()
my_auto1.confronta(my_auto2)

#casa_automo="GG", modello="T-rex", numero_posti=1, targa="ASDFG",
my_trasformer=Trasformer(nome="Baby", generazione=4, grado="sergente", reparto="spionaggio")

my_trasformer.scheda_militare()