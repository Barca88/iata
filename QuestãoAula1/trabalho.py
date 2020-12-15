import sys
import csv
from datetime import datetime

def main(argv):
    size = len(argv)

    if size >= 2:
        imput_file = argv[0]
        output_file = argv[1]
    else:
        print('imput_file e output_file necessarios')

    i = open(imput_file)
    csv_f = csv.DictReader(i)

    #Estções data de inicio
    primavera = datetime(2020,3,20,16,0,0)
    pri = primavera.strptime("%m/%d/%Y, %H:%M:%S")
    print('primavera '+ pri)
    verao = datetime(2020,6,20,23,0,0)
    ver = verao.strptime("%m/%d/%Y, %H:%M:%S")
    print('verao '+ ver)
    outono = datetime(2020,9,22,15,0,0)
    out = outono.strptime("%m/%d/%Y, %H:%M:%S")
    print('outono '+ out)
    inverno = datetime(2020,12,21,10,0,0)
    inv = inverno.strptime("%m/%d/%Y, %H:%M:%S")
    print('inverno '+ inv)

    #for row in csv_f:
    #    data = datetime.strptime(row['dt_iso'])
    #    print(datetime)

if __name__ == "__main__":
    main(sys.argv[1:])s