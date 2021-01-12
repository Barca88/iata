import csv
import networkx as net
# importar a biblioteca matplotlib.pyplot
import matplotlib.pyplot as plt

# open the file
in_file=csv.reader(open('lista_arestas.txt','r'))

g=net.Graph()
for line in in_file:
    g.add_edge(line[0],line[1],weight=line[2],conf=line[3])

print(g.nodes())
print(g.edges())


