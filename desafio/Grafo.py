#Classe que representa um grafo com seus vértices e arestas.
class Grafo(object):
    def __init__(self):
        self.lista_vizinhos = {}
        self.__lista_vertices = []

    #Método para adicionar um vértice.
    def add_vertice(self, vertice):
        self.__lista_vertices.append(vertice)

    #Método para adicionar aresta, se caso um dos vértices não tenha sido adicionado ainda ele é criado automaticamente.
    def add_aresta(self, vertice, outro_vertice):
        #Se vértice não existe no vetor de arestas nesse momento ele é criado
        if not vertice in self.lista_vizinhos:
            self.lista_vizinhos[vertice] = []
        self.lista_vizinhos[vertice].append(outro_vertice)
        #Se a segunda vertice não está criado  no vetor de arestas nesse momento ele é criado
        if not outro_vertice in self.lista_vizinhos:
            self.lista_vizinhos[outro_vertice] = []
        self.lista_vizinhos[outro_vertice].append(vertice)

    #Retorna uma lista de arestas vinculada a um vértice que é passado por parâmetro.
    def vizinhos(self, vertice):
        if vertice in self.lista_vizinhos:
            return self.lista_vizinhos[vertice]
        else:
            return []

    #Retorna uma lista com todos os vértices atuais do grafo.
    def lista_vertices(self):
        for vertice in self.lista_vizinhos.keys():
            if vertice not in self.__lista_vertices:
                self.add_vertice(vertice)
        return self.__lista_vertices

    #Método para deletar uma aresta vinculada a dois vértices.
    def deleta_aresta(self, vertice, outro_vertice):
        self.vizinhos(vertice).remove(outro_vertice)
        self.vizinhos(outro_vertice).remove(vertice)

    #Método para deletar um vértice e todas arestas com dependência do mesmo.
    def deleta_vertice(self, vertice):
        #Percorrendo vetor de arestas, para deletar todas arestas de uma Vértice
        for outro_vertice in self.lista_vizinhos[vertice]:
            self.deleta_aresta(vertice, outro_vertice)
        del self.lista_vizinhos[vertice]
        del self.__lista_vertices[vertice]

    #Retorna o grafo com todos os seus vértices e arestas.
    def getGrafo(self):
        return self.lista_vizinhos



#==============================================================================================


#Classe com métodos de busca de caminhos de grafos.
class GrafoCaminhos(object):
    def __init__(self):
        print("Iniciado")

    #Retorna uma Lista de Caminho relacionando duas vértices sendo uma o parâmetro inicio do percurso e outra o parâmetro fim do percurso,
    #esse método retorna o primeiro caminho achado no loop, sem lógica de proximidade.
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


    #Retorna uma Lista de Caminho relacionando duas vértices sendo uma o parâmetro inicio do percurso e outra o parâmetro fim do percurso,
    #método com lógica de Breadth-First Search – BFS(Busca em Largura) que retorna o caminho mais próximo dos dois pontos.
    def bfs(self, grafo, inicio, fim):
        # cria a fila vazia
        fila = []
        # adiciona um item ao fim da lista
        fila.append([inicio])

        while fila:
            # pega o primeiro caminho da fila
            caminho = fila.pop(0)
            # pega a ultima vertice do caminho
            vertice = caminho[-1]
            # verifica o fim do caminho
            if vertice == fim:
                return caminho
            # enumera todas vértices  adjasentes, controe um novo caminha e coloca na fila
            for adjasente in grafo.get(vertice, []):
                novo_caminho = list(caminho)
                novo_caminho.append(adjasente)
                fila.append(novo_caminho)


#==============================================================================================

#>>>>>>>>>>>Bônus<<<<<<<<<<<
#Classe com métodos de cálculos para Classe Grafo
class GrafoCalc(object):
    #construtor da classe, exige que passe como parâmetro um objeto da classe Grafo
    def __init__(self, pGrafo):
        if isinstance(pGrafo,Grafo):
            self.__grafo = pGrafo
        else:
            raise TypeError("Parâmetro {} não é do tipo {}".format(pGrafo, Grafo.__name__))


    #Retorna uma lista com o vértice com maior número de arestas no grafo,
    #caso haver vértices com a mesma quantidade de arestas esses também são retornados na lista.
    def verticesQuente(self):
        cont = 0
        lista = {}
        #percorrendo todas vértices de um grafo
        for vertice in self.__grafo.getGrafo():
            #Entra Se número total de arestas for maior ou igual  que contador(cont)
            if cont <= len(self.__grafo.getGrafo()[vertice]):
                #se o número total de aresta for maior, significa que tem um novo total máximo, então a lista antiga é apagada para ser substituída
                if cont != len(self.__grafo.getGrafo()[vertice]):
                    lista.clear()
                #adicionando o maior número ao contador
                cont = len(self.__grafo.getGrafo()[vertice])
                #adicionando vértice e seu número total de arestas na lista
                lista[vertice] = cont
        return lista


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

    #Retornando apenas uma vértice e suas arestas
    print("Vértice {0}, arestas: ".format('5'), grafo.vizinhos('5'))

    print("===============")

    #Retornando uma possibilidade de caminho
    print("Caminho, de v{0} até v{1} :".format('5','1'),grafo_c.encontra_caminho(grafo.getGrafo(), '5', '1'))

    print("===============")

    #Retornando o caminho mais curto usando a lógica de busca em largura
    print("Caminho mais próximo usando lógica de Breadth-First(Busca em largura) de v{0} até v{1}: ".format('5', '1'), grafo_c.bfs(grafo.getGrafo(), '5', '1'))

    print("===============")

    print(">>>>Bônus<<<")

    #Instanciando classeCalc passando um grafo
    grafo_calc = GrafoCalc(grafo)

    #Retornando vértices com maior número de arestas
    print("Vértice(s) com maior número de arestas: {0} (vertice : total de arestas)".format(grafo_calc.verticesQuente()))

