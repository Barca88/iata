import sys
import pandas as pd
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

def main(argv):
    imput_file = argv[0]
    dataset = pd.read_csv(imput_file, engine='python')

    print('Datas')
    datas = dataset['dt_iso'].unique()
    #print(datas)
    print('Total = '+ str(len(datas)))

    print('Cidades')
    city = dataset['city_name'].unique()
    print(city) 
    print('Total = '+ str(len(city)))

    print('Latitudes')
    lat = dataset['lat'].unique()
    print(lat)
    print('Total = '+ str(len(lat)))

    print('Longitudes')
    lon = dataset['lon'].unique()
    print(lon)
    print('Total = '+ str(len(lon)))

    print('Temperaturas')
    temp = dataset['temp'].unique()
    #print(temp)
    print('Total = '+ str(len(temp)))

    print('Humidades')
    hum = dataset['humidity'].unique()
    print(hum)
    print('Total = '+ str(len(hum)))

    print('\nNumero Total de Linhas: '+ str(len(dataset.index)))

if __name__ == "__main__":
   main(sys.argv[1:])