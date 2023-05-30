# Representação da corrente de Markov atrvés de um programa que gera novos textos.  


import random 


# Definindo o gráfico nos termos do vértice. 
class Vertex(object): 
  
# Construtor dos vértices. 
    def __init__(self, value):
     
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []
 
    # Representação do vértice em String. 
    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])
  
    # Adiciona arestas ao vértice.  
    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight
  
    # Incrementa o peso da aresta atual e o vértice fornecido. 
    def increment_edge(self, vertex): 
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
      
    # Retorna uma lista com os vértices adjacentes ao vértice atual. 
    def get_adjacent_nodes(self):
        return self.adjacent.keys()
  
    # Lista para selecionar o próximo vértice com base na probabilidade. 
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items(): 
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)
  
    # Retorna o próximo vértice com base nas probabilidades dos vértices adjacentes. 
    def next_word(self): 
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]
    
    
    
class Graph: 
    def __init__(self):
        self.vertices = {}
    
    # Colocar valores nos vértices. 
    def get_vertex_values(self): 
        return set(self.vertices.keys())
  
    # Adicionar vértices. 
    def add_vertex(self, value): 
        self.vertices[value] = Vertex(value)
    
    # "Pegar" um vértice. 
    def get_vertex(self, value): 
        if value not in self.vertices: 
            self.add_vertex(value)
        return self.vertices[value]
  
    # Gerar um nvo texto com o mapeamento. 
    def get_next_word(self, current_vertex): 
        return self.vertices[current_vertex.value].next_word()
    
    # Mapear as probabilidades para cada vértice
    def generate_probability_mappings(self): 
        for vertex in self.vertices.values():
            vertex.get_probability_map()
    
    