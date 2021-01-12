import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt

def main(argv):
    graf = nx.DiGraph()
    size = len(argv)

    if size >= 2:
        imput_file = argv[0]
        output_file = argv[1]
    else:
        print('imput_file e output_file necessarios')
        return

    i = open(imput_file)
    csv_imput = csv.DictReader(i)
    o = open(output_file, 'a')

    csv_output = csv.writer(o, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    c = 0
    for row in csv_imput:
        p1 = row['person1']
        p2 = row['person2']
        peso = int(row['weight'])
        conecao = int(row['conection'])
        # print(p1 + ',' + p2 + ',' + str(peso) + ',' + str(conecao))
        graf.add_edge(p1,p2,weight=peso,cor=conecao)
        c+=1

    print('Total = '+str(c))
    
    #medidas de centralidade

#centralidade do grau (o número de conecções de um grau para todos os outros)
    print(nx.degree_centrality(graf))

#eigenvector centrality (o quão importante é um nodo em função de quão bem conectado está)
    print(nx.eigenvector_centrality(graf))

#closeness centralidade (importância de um nodo em função da sua proximidade com os outros da rede)
    print(nx.closeness_centrality(graf))

#betweeness centralidade (quantifica quantas vezes um nodo aparece nos caminhos mais curtos entre dois nodos)
    print(nx.betweenness_centrality(graf))

    
    nx.spring_layout(graf)
    nx.draw_networkx(graf)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
