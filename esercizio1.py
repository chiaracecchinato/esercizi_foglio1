def stampa(self):
    lista=[1,2,3,4]
    for item in lista:
        print('"{}"'.format(item))

def statistiche(self):
    lista=[1,2,3,4]
    max=0
    min=0
    if type(lista)==int:
        n=len(lista)
        for item in lista:
            somma+=item
        media=somma/n
        i=0
        for item in lista:
            if i==0:
                max=item
                min=item
            if item>max:
                max=item
            elif item<min:
                min=item
    print('la somma è: "{}", la media: "{}", il massimo: "{}", il minimo: "{}"',format(somma, media, max, min))

       

def somma_vettoriale(self):
    lista1=[2,3,6,7]
    lista2=[5,8,1,0]
    if type(lista1)==int & type(lista2):
        n1=len(self.lista1)
        ok1="liste di interi"
        n2=len(self.lista2)
    else:
        lista=[]
        print('"{}"'.fromat(lista))
    listanuova=[]
    if n1==n2:
        for item1, item2 in lista1, lista2:
            sommavett+=item1+item2
            listanuova=sommavett
    print('somma vettoriale (se lista vuota: non stessa lunghezzza): "{}"'.format(listanuova))