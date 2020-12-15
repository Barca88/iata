import sys
import csv
import math
from datetime import datetime
from meteocalc import Temp, heat_index

def estacao(data):
    #Estções data de inicio segundo https://www.calendarr.com/portugal/estacoes-do-ano/
    primavera = datetime(data.year,3,20,16,0,0)
    verao = datetime(data.year,6,20,23,0,0)
    outono = datetime(data.year,9,22,15,0,0)
    inverno = datetime(data.year,12,21,10,0,0)

    #Primaver->Verao->Outono->Inverno
    if data < primavera:
        return 'inverno'
    elif data < verao:
        return 'primavera'
    elif data < outono:
        return 'verao'
    elif data < inverno:
        return 'outono'
    else:
        return 'inverno'

def tempIdeal(estacao):
    if estacao == 'inverno' or estacao == 'outono':
        return 15
    else:
        return 25

def main(argv):
    size = len(argv)

    if size >= 2:
        imput_file = argv[0]
        output_file = argv[1]
    else:
        print('imput_file e output_file necessarios')

    i = open(imput_file)
    csv_imput = csv.DictReader(i)
    o = open(output_file,'a')
    # Assumindo que o ficheio ouput está criado com a linha que identifica as colunas
    # ['estacao','tIdeal','toDo']
    csv_output = csv.writer(o, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    c = 0
    for row in csv_imput:
        data = datetime.strptime(row['dt_iso'],"%Y-%m-%d %H:%M:%S")
        temperatura = Temp(row['temp'], 'c')
        humidade = int(row['humidity'])
        # Heat Index is an index that combines air temperature and relative 
        # humidity in an attempt to determine the human-perceived equivalent temperature.
        hi = heat_index(temperatura,humidade)
        estacaoAno = estacao(data)
        tIdeal = tempIdeal(estacaoAno)

        diffTemp = tIdeal - hi.c
        if diffTemp > 0:
            r = 'airconditioning+{'+ str(diffTemp) +'}'
        else:
            r = 'airconditioning{'+ str(diffTemp) +'}'

        linha = [estacaoAno,str(tIdeal),r]
        csv_output.writerow(linha)
        c+=1
    print('Total de linhas tratadas: ' + str(c))
if __name__ == "__main__":
    main(sys.argv[1:])