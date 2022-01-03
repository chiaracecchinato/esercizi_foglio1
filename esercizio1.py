class Ese1:
    def stampa(self, lista):
        self.lista=lista
        for item in lista:
            print('"{}"'.format(item))

    def statistiche(self, lista):
        self.lista=lista
        max=0
        min=0
        if type(self.lista)==int:
            n=len(lista)
            for item in self.lista:
                somma+=item
            media=somma/n
            i=0
            for item in self.lista:
                if i==0:
                    max=item
                    min=item
                if item>max:
                    max=item
                elif item<min:
                    min=item
        print('la somma è: "{}", la media: "{}", il massimo: "{}", il minimo: "{}"'.format(somma, media, max, min))

       

    def somma_vettoriale(self, lista1, lista2):
        self.lista1=lista1
        self.lista2=lista2
        if type(self.lista1)==int & type(self.lista2):
            n1=len(self.lista1)
            ok1="liste di interi"
            n2=len(self.lista2)
        else:
            lista=[]
            print('"{}"'.fromat(lista))
        listanuova=[]
        if n1==n2:
            for item1, item2 in self.lista1, self.lista2:
                sommavett+=item1+item2
                listanuova=sommavett
        print('somma vettoriale (se lista vuota: non stessa lunghezzza): "{}"'.format(listanuova))

lista=[1,2,3,4]
lista1=[2,3,6,7]
lista2=[5,8,1,0]
my_es=Ese1()
my_es.stampa(lista)
my_es.statistiche(lista)
my_es.somma_vettoriale(lista1, lista2)