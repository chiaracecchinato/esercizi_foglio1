from datetime import datetime

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))


    def get_data(self):
        
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            data_vendite = []

            my_file = open(self.name, 'r')

            for line in my_file:
                
                elements = line.split(',')
                
                elements[-1] = elements[-1].strip()

                my_date=datetime.strptime(elements[0], '%d-%m-%Y')

                for item in my_date:
                    data_vendite.append(item)
                
                for data in data_vendite:
                    print(data.strftime('%d-%m-%Y'))
            
            # Chiudo il file
            my_file.close()
            
            # Quando ho processato tutte le righe, ritorno i dati
            return data_vendite

mio_file = CSVFile(name='shampoo_sales.csv')
#print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))
