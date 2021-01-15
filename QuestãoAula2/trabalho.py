import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt

def main(argv):
    graf = nx.DiGraph()
    size = len(argv)

    if size >= 1:
        imput_file = argv[0]
    else:
        print('imput_file necessario')
        return

    i = open(imput_file)
    csv_imput = csv.DictReader(i)

    for row in csv_imput:
        p1 = row['person1']
        p2 = row['person2']
        peso = int(row['weight'])
        conecao = int(row['conection'])
        graf.add_edge(p1,p2,weight=peso,conection=conecao)
        

    print(nx.info(graf))
    
    #medidas de centralidade
    print('\n\tmedidas de centralidade')
    #centralidade do grau (o número de conecções de um grau para todos os outros)
    print('Grau de centralidade')
    print(nx.degree_centrality(graf))
    print('\n')
    #eigenvector centrality (o quão importante é um nodo em função de quão bem conectado está)
    print('Eigenvector centrality')
    print(nx.eigenvector_centrality(graf))
    print('\n')
    #closeness centralidade (importância de um nodo em função da sua proximidade com os outros da rede)
    print('Closeness centrality')
    print(nx.closeness_centrality(graf))
    print('\n')
    #betweeness centralidade (quantifica quantas vezes um nodo aparece nos caminhos mais curtos entre dois nodos)
    print('Betweeness centrality')
    print(nx.betweenness_centrality(graf))
    
    print('Average clustering')
    print(nx.average_clustering(graf))
    print('\n\n')
    
    
    elarge = [(u, v) for (u, v, d) in graf.edges(data=True) if d['weight'] >= 3]
    esmall = [(u, v) for (u, v, d) in graf.edges(data=True) if d['weight'] < 3]
    
    forte = [(u, v) for (u, v, d) in graf.edges(data=True) if d['conection'] == 1]
    fraca = [(u, v) for (u, v, d) in graf.edges(data=True) if d['conection'] == 3]
    
    pos = nx.circular_layout(graf)  # posições para todos os nodos

    # nodos
    nx.draw_networkx_nodes(graf, pos, node_size=70)

    # arestas
    nx.draw_networkx_edges(graf, pos, edgelist=elarge,width=0.5)
    nx.draw_networkx_edges(graf, pos, edgelist=esmall,width=0.5, alpha=0.5, edge_color='b', style='dashed')
    nx.draw_networkx_edges(graf, pos, edgelist=forte,width=0.5, alpha=0.5, edge_color='r', style='dotted')
    nx.draw_networkx_edges(graf, pos, edgelist=fraca,width=0.5, alpha=0.5, edge_color='#FFFFCC', style='dotted')
    
    # labels
    nx.draw_networkx_labels(graf, pos, font_size=6, font_family='sans-serif')

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
