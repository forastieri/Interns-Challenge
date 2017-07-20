#Classe para representar um grafo com suas vértices e arestas
class Grafo:
    def __init__(self):
        self.lista_vizinhos = {}
        self._lista_vertices = []

    #Método para adicionar um vértice
    def add_vertice(self, vertice):
        self._lista_vertices.append(vertice)

    #Métodod para adicionar aresta
    def add_aresta(self, vertice, outro_vertice):
        #Se vértice não existe no vetor de arestas nesse momento ele é criado
        if not vertice in self.lista_vizinhos:
            self.lista_vizinhos[vertice] = []
        self.lista_vizinhos[vertice].append(outro_vertice)
        #Se a segunda vertice não está criado  no vetor de arestas nesse momento ele é criado
        if not outro_vertice in self.lista_vizinhos:
            self.lista_vizinhos[outro_vertice] = []
        self.lista_vizinhos[outro_vertice].append(vertice)

    #Método para chamar uma vértice e suas arestas
    def vizinhos(self, vertice):
        if vertice in self.lista_vizinhos:
            return self.lista_vizinhos[vertice]
        else:
            return []

    # método para retorna lista de vértices apenas
    def lista_vertices(self):
        for vertice in self.lista_vizinhos.keys():
            if vertice not in self._lista_vertices:
                self.add_vertice(vertice)
        return self._lista_vertices

    #Método para deletar aresta de duas vértices bidimensional
    def deleta_aresta(self, vertice, outro_vertice):
        self.vizinhos(vertice).remove(outro_vertice)
        self.vizinhos(outro_vertice).remove(vertice)

    #Método para deletar uma Vertice e suas arestas
    def deleta_vertice(self, vertice):
        #Percorrendo vetor de arestas, para deletar todas arestas de uma Vértice
        for outro_vertice in self.lista_vizinhos[vertice]:
            self.deleta_aresta(vertice, outro_vertice)
        del self.lista_vizinhos[vertice]
        del self._lista_vertices[vertice]

    #Retorno do grafo
    def getGrafo(self):
        return self.lista_vizinhos



#==============================================================================================


#classe com métodos para percorrer os caminhos de um grafo
class GrafoCaminhos:
    def __init__(self):
        print("Iniciado")

    #Encontrar um caminho (com voltas ou não) de uma vértice até outra sem proximidade
    def encontra_caminho(self, grafo, inicio, fim, caminho=None):
        #Se não tem um pré caminho ele é criado nesse momento, usando para lógica de loop do método para retorna o vetor de caminho percorrido
        if caminho is None: caminho = []
        caminho += [inicio]
        #Se o caminho de uma vértice até outra é achado, retorna o vetor do caminho
        if inicio == fim:
            return caminho
        #Se vértice inicial não existe, retorna none
        if not inicio in grafo:
            return None
        #Percorrendo trilha de arestas de um determinado vértice que foi definido como parâmetro[inicio] e analisando suas arestas para anotar o caminho do achado
        for aresta in grafo[inicio]:
            #Se caso aresta não está no vetor de caminhos, ele é adicionando como novo inicio de vértice e o método encontra_caminho é acionado novamente
            if aresta not in caminho:
                novo_caminho = self.encontra_caminho(grafo, aresta, fim, caminho)
                if novo_caminho: return novo_caminho
        return None


    #Método com lógica de Breadth-First Search - BFS(Busca em largura)
    def bfs(self, grafo, inicio, fim):
        # cria a fila vazia
        fila = []
        # adiciona um item ao fim da lista
        fila.append([inicio])

        while fila:
            # pega o primeiro caminho da fila
            caminho = fila.pop(0)
            # pega o ultimo no do caminho
            no = caminho[-1]
            # verifica o fim do caminho
            if no == fim:
                return caminho
            # enumera todos os nos adjasentes, controe um novo caminha e coloca na fila
            for adjasente in grafo.get(no, []):
                novo_caminho = list(caminho)
                novo_caminho.append(adjasente)
                fila.append(novo_caminho)


#==============================================================================================


if __name__ == "__main__":

    #Instanciando classe Grafo e classe GrafoCaminhos
    grafo = Grafo()
    grafo_c = GrafoCaminhos()

    # Puxando arquivo
    arq = open('data/edges.dat')
    arq_lines = arq.readlines()

    # Logica para separacao ex: linha(x): 5551 1515 - p1 = 5551, p2 = 1515
    # Adicionando pontos
    for line in arq_lines:
        p1 = line.split(" ")[0]; p2 = line.split()[1]
        grafo.add_aresta(p1, p2)
    # fechamento do arquivo
    arq.close()

    print("================")

    #Retornando grafo com todas suas vértices e arestas
    print("Grafo: ",grafo.getGrafo())

    print("===============")

    #Retornando lista de vértices
    print("Lista de Vértices: ",grafo.lista_vertices())

    print("===============")

    #Retornando apenas uma vertice e suas arestas
    print("Vértice {0}, arestas: ".format(5), grafo.vizinhos('5'))

    print("===============")

    #Retornando uma possibilidade de caminho
    print("Caminho, de v{0} até v{1} :".format('5','1'),grafo_c.encontra_caminho(grafo.getGrafo(), '5', '1'))

    print("===============")

    #Retornando o caminho mais curto usando a lógica de busca em largura
    print("Caminho mais próximo usando lógica de Breadth-First(Busca em largura) de v{0} até v{1}: ".format('5', '1'), grafo_c.bfs(grafo.getGrafo(), '5', '1'))

    print("===============")





