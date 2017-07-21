# Desafio Semantix 

**Linguagem utilizada:** Python3

Para o desafio da semantix foi criado um arquivo python com o nome: grafo.py, dentro desse file foi implementado três classes sendo duas necessária para o desafio e uma como bônus.

**Classes:** Grafo, GrafoCaminho e GrafoCalc.

## Grafo

Classe que representa um grafo com seus vértices e arestas.

####  Métodos:
* **-add_vertice(vertice):** Método para adicionar um vértice.
*	**-add_aresta(vertice1, vertice2):** Método para adicionar aresta, se caso um dos vértices não tenha sido adicionado ainda ele é criado automaticamente.  
*	**-vizinhos(Vertice):** Retorna uma lista de arestas vinculada a um vértice que é passado por parâmetro. 
*	**-lista_vertice():** Retorna uma lista com todos os vértices atuais do grafo.
*	**-deleta_aresta(vertice1, vertice2):** Método para deletar uma aresta vinculada a dois vértices. 
*	**-deleta_vertice(vertice):** Método para deletar um vértice e todas arestas com dependência do mesmo.   
*	**-getGrafo():**  Retorna o grafo com todos os seus vértices e arestas.

## GrafoCaminho

Classe com métodos de busca de caminhos de grafos.

#### Métodos:
*	**-encontra_caminho(Grafo, inicio, fim):** Retorna uma Lista de Caminho relacionando  duas vértices sendo uma o parâmetro inicio  do percurso e outra o parâmetro fim do percurso, esse método retorna o primeiro caminho achado no loop, sem lógica de proximidade.  
*	**-bfs(Grafo, inicio, fim):** Retorna uma Lista de Caminho relacionando  duas vértices sendo uma o parâmetro inicio  do percurso e outra o parâmetro fim do percurso, método com lógica de Breadth-First Search – BFS(Busca em Largura) que retorna o caminho mais próximo dos dois pontos. 

## GrafoCalc
###### <Classe Bônus Desafio >

Classe com métodos de cálculos para Classe Grafo

#### Métodos:
* **-VerticesQuentes():** Retorna uma lista com o vértice com maior número de arestas no grafo, caso haver vértices com a mesma quantidade de arestas  esses também são retornados na lista.  

## Exemplo:

Após instanciar a Classe Grafo e atribuir os valores do grafo, podemos utilizar os seguintes métodos.
```
print(grafo.getGrafo())
Retorno do Grafo  >> 
```
```
print(grafo.,lista_vertices())
Retorno de todos os vértices >> 
```
```
print(grafo.vizinhos([vx]))
Retorna um vértice e suas arestas dependentes >> 
```
Após instanciar a Classe GrafoCaminho  e com uma Instancia da Classe Grafo atribuída, podemos utilizar os seguintes métodos.
```
print(grafo_caminho.encontra_caminho(grafo.getGrafo(), [vx], [vy]))
Retorna o primeiro caminho encontrado do ponto inicial ao ponto final no grafo >>
```
```
print(grafo_caminho.bfs(grafo.getGrafo(), [vx], [vy]))
Retorna o caminho mais curto de um ponto inicial ao ponto final usando lógica de busca em largura no grafo >>
```
###### >>Bônus<<
Para instanciar a Classe GrafoCalc  temos que  atribuir no seu construtor uma instância da classe Grafo, após,  podemos utilizar os seguinte(s) método(s).
```
print(grafo_calc.verticesQuente())
Retorna uma lista do(s) vértice(s) com mais arestas e total >>>  
```

## Autor
**Fábio Forastieri**

## Bônus - Amostra de Grafo com teste em APIs de network para Grafos 
Essa é uma amostra aparte do desafio, utilizando APIs do python para testar a interação na rede junto com classes criadas com lógica de busca de Caminhos próximos.

#### Execução
Dentro da pasta bonus-teste_network contem um arquivo python chamado teste_network.py com a  lógica da implementação.
#### Dependência 
Com o python3 temos que instalar os seguintes módulos: **Networkx** e **Pylab** 
#### Resultado  
Para caminho de vértice 1 até vértice 5, temos a seguinte saída no Grafo:

