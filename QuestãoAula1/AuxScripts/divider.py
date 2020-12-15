import sys
import csv

def main(argv):
    size = len(argv)

    if size >= 5:
        imput_file = argv[0]
        output1 = argv[1]
        output2 = argv[2]
        coluna = argv[3]
        valor = argv[4]
    else: 
        print('ler.csv output1.csv output2.csv coluna valor')
        return

    i = open(imput_file)
    o1 = open(output1,mode='a')
    o2 = open(output2,mode='a')

    csv_f = csv.DictReader(i)
    csv_o1 = csv.writer(o1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_o2 = csv.writer(o2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    c = 0
    c1 = 0
    c2 = 0

    for row in csv_f:
        if c == 0:
            csv_o1.writerow(row)
            csv_o2.writerow(row)
        linha = [row['dt_iso'],row['city_name'],row['lat'],row['lon'],row['temp'],row['humidity']]
        if row[coluna] == valor:
            csv_o1.writerow(linha)
            c1 += 1
        else:
            csv_o2.writerow(linha)
            c2 += 1
        c += 1


    print('Total de linhas lidas '+ str(c))
    print('Total de linhas escritas no '+ output1 + ' ' + str(c1))
    print('Total de linhas escritas no Output2 '+ output2 + ' ' + str(c2))

if __name__ == "__main__":
    main(sys.argv[1:])