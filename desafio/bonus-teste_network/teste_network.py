import networkx as nx
from pylab import show

from Grafo import *

GC = GrafoCaminhos()


#Abrindo networkx
g = nx.Graph()

#Puxando arquivo de pontos e alocando em um array por linhas
arq = open('../data/edges.dat')
arq_lines = arq.readlines()


#Logica para separacao ex: linha(x): 5551 1515 - p1 = 5551, p2 = 1515
#Adicionando pontos
for line in arq_lines:
    p1 = int(line.split(" ")[0]); p2 = int(line.split()[1])
    g.add_edge(p1, p2)
#fechamento do arquivo
arq.close()

#Metodo para pegar apenas os vértices do caminho
def most_important(g, gn):
    ranking = nx.betweenness_centrality(g).items()
    Gt = g.copy()
    for k, v in ranking:
        if not k in gn:
            Gt.remove_node(k)
    print(Gt)
    return Gt

#chamado do método
Gt = most_important(g, GC.bfs(g.adj,1,5))


# criando o layout
pos = nx.spring_layout(g)
# desenhando grafo
nx.draw_networkx_nodes(g,pos,node_color='b',alpha=0.2,node_size=8)
nx.draw_networkx_edges(g,pos,alpha=0.1)
nx.draw_networkx_labels(g,pos,font_size=5,font_color='b')




# desenhando os mais importantes vértices com diferenca de estilo
nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
# exibindo os mais importantes nos
nx.draw_networkx_labels(Gt,pos,font_size=15,font_color='b')
nx.draw_networkx_edges(Gt,pos,font_size=20,font_color='y')
#exibicao
show()