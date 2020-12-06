import sys
import copy

'''
Credit for Vertexd class goes to bogotobogo.com
https://www.bogotobogo.com/python/python_graph_data_structures.php
'''
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    '''
    Author: Ethan Steidl
    '''
    def remove_neighbor(self, neighbor):
        self.adjacent.pop(neighbor, None)

    def get_connections(self):
        return list(self.adjacent.keys())

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        #print (self.adjacent.keys())
        return self.adjacent[neighbor]

'''
Credit for Graph class goes to bogotobogo.com
https://www.bogotobogo.com/python/python_graph_data_structures.php
'''
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    '''
    Author: Ethan Steidl
    '''
    def path_cost(self, path):
        start = 0

        total = 0
        while(start < len(path)-1):
            total += self.edge_cost(path[start], path[start+1])
            start += 1
        return total

    '''
    Author: Ethan Steidl
    '''
    def edge_cost(self,start, end):
        return (self.vert_dict[start]).adjacent[end]

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    '''
    Author: Ethan Steidl
    '''
    def remove_vertex(self, node):
        self.num_vertices = self.num_vertices - 1
        for v in self.vert_dict[node].get_connections():
            self.vert_dict[v].remove_neighbor(node)
        self.vert_dict.pop(node, None)

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor((self.vert_dict[to]).id, cost)
        self.vert_dict[to].add_neighbor((self.vert_dict[frm]).id, cost)

    '''
    Author: Ethan Steidl
    This was modified from add_edge
    '''
    def add_edge_directed(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor((self.vert_dict[to]).id, cost)

    '''
    Author: Ethan Steidl
    '''
    def remove_edge_directed(self, frm, to):
        self.vert_dict[frm].remove_neighbor((self.vert_dict[to]).id)

    '''
    Author: Ethan Steidl
    '''
    def remove_edge(self, frm, to):
        self.vert_dict[frm].remove_neighbor((self.vert_dict[to]).id)
        self.vert_dict[to].remove_neighbor((self.vert_dict[frm]).id)

    def get_vertices(self):
        return self.vert_dict.keys()



    '''
    Author: Ethan Steidl
    This implementation of Yen's algorithm was inspired by Wikipedia
    https://en.wikipedia.org/wiki/Yen%27s_algorithm
    '''
    def yen(self,start, end, K):
        A = []  #return value of shortest paths
        A.append(self.dijkstra(start, end)) #add absolute shortest
        distances = []  #distances that coresspond to paths in B
        B = [[]]        #short paths found
        B.pop(0)

        for k in range(1,K):
            for i in range(0, len(A[k-1])-2):

                #search for shortest path from i to end
                spurNode = A[k-1][i]
                rootPath = A[k-1][0:i+1]

                temp_graph = copy.deepcopy(self)    #copy the graph to restore later

                #truncation of edges
                for p in A:
                    if(len(p) == 0):
                        continue
                    if rootPath == p[0:i+1]:
                        self.remove_edge(A[0][i], A[0][i+1])

                #truncation of nodes
                for rootPathNode in rootPath:
                    if(rootPathNode == spurNode):
                        continue

                    self.remove_vertex(rootPathNode)

                #solve short paths
                spurPath = self.dijkstra(spurNode, end)
                totalPath = rootPath[:-1] + spurPath

                self = temp_graph #restore the deleted edges and nodes

                #add path if not found
                if(totalPath[-1] == end and totalPath not in B):
                    B.append(totalPath)
                    distances.append(self.path_cost(totalPath))


            #if there was no path, handle case
            if (len(B) == 0):
                continue


            #sort paths based on distances and add shortest to A
            zipped = zip(distances,B)
            B = [i for _, i in sorted(zipped)]
            distances.clear()
            A.append(B[0])
            B.pop(0)

        return A


    '''
    Author: Ethan Steidl
    This implementation of Dijkstra's was inspired by Ben Alex Keen
    https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
    '''
    def dijkstra(self, start, end):

        #initialize variables
        shortest_paths = {start: (None, 0)}
        visited = set()
        current_node = start

        #loop until the end is found
        while current_node != end:
            #add the current node and get its adjacencies
            visited.add(current_node)
            v = self.get_vertex(current_node)
            destinations = v.get_connections()#(self.vert_dict[current_node]).get_connections()

            #find weight so far to current node
            weight_to_current_node = shortest_paths[current_node][1]

            #for each adjacent node, find the weight from begining to it.
            #Add it to the path, but if a shorter path has been found, pursue the
            #shorter path
            for next_node in destinations:
                vertex = self.get_vertex(current_node)
                weight = vertex.get_weight(next_node)
                weight += weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            #check if it is possible to reach the end, if not return an empty list
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return []

            #set the current node to the shortest node in the list
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        #organize the nodes from the shortast paths
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node

        #reverse as it has been solved backwards
        path = path[::-1]
        return path