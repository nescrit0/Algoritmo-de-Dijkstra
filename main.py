import networkx as nx
import matplotlib.pyplot as plt
import random

#Creamos nuestra variable random para asignar el tiempo de coste al azar
n=[m for m in range (1,100)]
random.shuffle(n)

# Crando el grafo
class Grafo:
  def __init__(self, graph):
    self.G = nx.Graph()
    self.graph = graph
    self.nodes = list(graph.keys())

  #Creando los bordes
  def bordes(self, a, b, weight):
    self.G.add_edge(a, b, weight=weight)
  
  # Mostrar el grafo
  def mostrar(self):
    pos = nx.spring_layout(self.G)
    weights = nx.get_edge_attributes(self.G, "weight")
    self.G.add_nodes_from(self.nodes)

    plt.figure()
    #Esto es simplemente para darle un poco de estilo al codigo
    nx.draw(
      self.G, pos, edge_color='black', width=1, linewidths=1,
      node_size=500, node_color='blue', alpha=0.9,
      labels={node: node for node in self.G.nodes()}
    )
    nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
    plt.axis('off')
    plt.show()

  
  def Mostrar_grafo(self):
    for i in self.graph:
      for j in self.graph[i]:
        self.bordes(i, j['v'], j['tiempo'])

    self.mostrar()

    # Asignamos nuestros datos
graph = {
    'Guadalajara': [{'v': 'Venta del astillero','tiempo': n[0]}, {'v': 'Tala','tiempo': n[1]}],
    'Venta del astillero': [{'v': 'Guadalajara','tiempo': n[2]}, {'v': 'Magdalena','tiempo':n[3]}],
    'Magdalena': [{'v': 'Venta del astillero','tiempo': n[4]}, {'v': 'Ixtlan del rio','tiempo': n[5]}],
    'Ixtlan del rio': [{'v': 'Magdalena','tiempo': n[6]}, {'v': 'Compostela','tiempo': n[7]}, {'v': 'Amatlan','tiempo': n[8]}],
    'Compostela': [{'v': 'Ixtlan del rio','tiempo': n[9]}, {'v': 'Guayabitos','tiempo': n[10]}],
    'Guayabitos': [{'v': 'Compostela','tiempo': n[11]}, {'v': 'Sayulita','tiempo': n[12]}],
    'Sayulita': [{'v': 'Guayabitos','tiempo': n[13]}, {'v': 'Bucerias','tiempo': n[14]}],
    'Bucerias': [{'v': 'Sayulita','tiempo': n[15]}, {'v': 'Puerto Vallarta','tiempo': n[16]}],
    'Puerto Vallarta': [{'v': 'Bucerias','tiempo': n[17]}, {'v': 'San Sebastian','tiempo': n[18]}],
    'San Sebastian': [{'v': 'Puerto Vallarta','tiempo': n[19]}, {'v': 'Mascota','tiempo': n[20]}],
    'Mascota': [{'v': 'San Sebastian','tiempo': n[21]}, {'v': 'Ateanguillo','tiempo': n[22]}],
    'Ateanguillo': [{'v': 'Mascota','tiempo': n[23]}, {'v': 'Estanzuela','tiempo': n[24]}],
    'Estanzuela': [{'v': 'Ateanguillo','tiempo': n[25]}, {'v': 'Ameca','tiempo': n[26]}],
    'Ameca': [{'v': 'Estanzuela','tiempo': n[27]}, {'v': 'Tala','tiempo': n[28]}],
    'Tala': [{'v': 'Ameca','tiempo': n[29]}, {'v': 'Guadalajara','tiempo': n[30]},{'v': 'Ahualulco','tiempo': n[31]}],
    'Ahualulco': [{'v': 'Tala','tiempo': n[32]}, {'v': 'Etzatlan','tiempo': n[33]}],
    'Etzatlan': [{'v': 'Ahualulco','tiempo': n[34]}, {'v': 'Amatlan','tiempo': n[35]}],
    'Amatlan': [{'v': 'Etzatlan','tiempo': n[36]}, {'v': 'Ixtlan del rio','tiempo': n[37]}]
}

# Mostramos nuestro primer grafo
G = Grafo(graph=graph)
G.Mostrar_grafo()

# Con esta funcion nos da el costo de la ruta que en su caso son el tiempo
def costo(path):
  path_weight = 0

  for index, value in enumerate(path):
    try:
      for j in graph[value]:
        if j['v'] == path[index + 1]:
            path_weight += j['tiempo']
    except:
      break

  return path_weight

# Con esta funcion empleamos el algoritmo de dijkstra para encontrar 
# el camino con menor costo
def encontrar_ruta_corta(graph, start, end, path =[]):
  path = path + [start]
  shortest = None
  weights = None

  if start == end: return path

  for node in graph[start]:
      if node['v'] not in path:
          newpath = encontrar_ruta_corta(graph, node['v'], end, path)
          if newpath:
            new_wexight = costo(newpath)
            if not weights or new_wexight < weights:
              shortest = newpath
              weights = new_wexight

  return shortest

ruta_corta = encontrar_ruta_corta(graph, 'Guadalajara', 'Puerto Vallarta')
costo_de_ruta_corta = costo(ruta_corta)

print('Ruta con menor tiempo :', ruta_corta)
print('Minutos :', costo_de_ruta_corta,'min')


grafo_final = {}

# Aqui generamos nuestro grafo final 
for index, value in enumerate(ruta_corta):
  try:
    for j in graph[value]:
      if j['v'] == ruta_corta[index + 1]:
        grafo_final.update({value: [j]})
  except:
    break

# Mostramos nuestro grafo final
Fuga = Grafo(grafo_final)

for i in grafo_final:
  for j in grafo_final[i]:
        Fuga.bordes(i, j['v'], j['tiempo'])

Fuga.mostrar()
