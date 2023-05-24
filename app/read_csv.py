#importar modulo csv
import csv
#funcion lectura de csv
def read_csv(path):
  #se abre el archivo csv 
  with open(path, 'r') as csv_file:
    # se crea el lector de columnas, delimiter es el caracter con que se separa cada columna
    reader = csv.reader(csv_file, delimiter =',')
    # se obtiene el nombre de las columnas, sabemos es la primera fila, lo necesitamos despues
    header = next(reader)
    # lista que se retorna con los datos
    data_list = []
    
    # iterados para ir por cada fila que se lee.
    for row in reader:
      iterable = zip(header,row)
      #se convierte lois datos en un diccionario
      country_dict = {key: value for key, value in iterable }
      data_list.append(country_dict)
    return data_list
     


if __name__ == '__main__':
  data_list = read_csv('world_population.csv')
  print(data_list[97])
  

