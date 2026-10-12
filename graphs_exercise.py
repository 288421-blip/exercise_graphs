# TASK 1 ############################################################
def build_adjacency_list(edges, directed=False):
    graph = {}
    for u,v in edges:
        if u not in graph:
            graph [u] = []
        if v not in graph:
            graph[v] = []

    for u, v in edges:
        graph[u].append(v)
        if directed == False:
            graph[v].append(u)

    return graph
    #if directed == False:
     #   graph = {"P1": ["P2", "P3"],
     #           "P2": ["P1", "P3"],
     #            "P3": ["P1", "P2", "P3"],
     #            "P4": ["P3", "P5"],
     #            "P5": ["P4"]}
    #else:
     #   graph = {"P1": ["P2", "P3"],
     #            "P2": ["P3"],
     #            "P3": ["P4"],
     #            "P4": ["P5"],
     #            "P5": []}

def degrees(graph):
    degrees_dict = {}
    for vertex in graph:
        degrees_dict[vertex] = len(graph[vertex])

    return degrees_dict

def in_out_degree(graph):
    in_degree = {}
    out_degree = {}
    for vertex in graph:
        out_degree[vertex] = 0
        in_degree[vertex] = 0
            
    for vertex in graph:
        out_degree[vertex] = len(graph[vertex])  # out_degree[v] = len(graph[v])
            
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1
                
    return in_degree, out_degree



V = {"P1", "P2", "P3", "P4", "P5"}

E = [
    ("P1", "P2"), 
    ("P1", "P3"), 
    ("P2", "P3"), 
    ("P3", "P4"), 
    ("P4", "P5")
]

# Comprobacion
#print(build_adjacency_list(E, False))
#print(build_adjacency_list(E, True))

#print(degrees(build_adjacency_list(E, False)))
#print(degrees(build_adjacency_list(E, True)))

print(in_out_degree(build_adjacency_list(E, False)))
print(in_out_degree(build_adjacency_list(E, True)))


# TASK 3 ############################################################
def dfs(graph, start):
    visited = [start]
    stack = [start]   # es el camino actual, su ultimo elemento es el vertice en el que se esta

    while stack:
        vertex = stack[-1]
        smallest = None
        for neighbor in graph[vertex]:
            if neighbor not in visited and (smallest is None or neighbor < smallest):
                smallest = neighbor

        if smallest is None:
            stack.pop()              # no quedan vecinos: retrocedemos
        else:
            visited.append(smallest)
            stack.append(smallest)

    return visited


def connected_components(graph):
    components = []
    found = []  # vértices ya asignados a algún componente

    for vertex in graph:
        if vertex not in found:
            reachable = dfs(graph, vertex)
            components.append(set(reachable))  # la salida debe ser una lista de sets
            found.extend(reachable)

    return components


def is_weakly_connected(graph):
    # Construir la "sombra" no dirigida
    shadow = {vertex: [] for vertex in graph}
    for u in graph:
        for v in graph[u]:
            shadow[u].append(v)
            shadow[v].append(u)

    return len(connected_components(shadow)) == 1


# TASK 4 #######################################################
def eulerian_type(graph, directed = False):
    if directed == False:       # undirected
        if len(connected_components(graph)) != 1:
            return "None" 

        odd = 0
        for vertex in graph:
            if len(graph[vertex]) % 2 == 1:  # grado impar
                odd += 1

        if odd == 0:  # si no hay ningun grado impar (son todos pares): circuito
            return "Circuit"
        
        if odd == 2:  # si hay dos vértices que tienen grado impar: camino
            return "Path"
        return "None"

    else:        # directed
        if is_weakly_connected(graph) == False:
            return "None"    

        in_degree, out_degree = in_out_degree(graph)
        start = 0
        end = 0
        for vertex in graph:
            excess = out_degree[vertex] - in_degree[vertex]
            if excess == 1:
                start += 1
            elif excess == -1:
                end += 1
            elif excess != 0:
                return "None"

        if start == 0 and end == 0:
            return "Circuit"

        if start == 1 and end == 1:
            return "Path"

        return None


