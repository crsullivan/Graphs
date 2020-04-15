

"""
Simple graph implementation
"""
from util import Stack  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
    

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # graph.add_edge(pair[0], pair[1])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    print('starting neighbors', graph.get_neighbors(starting_node))

    # s = Stack()
    # s.push(starting_node)
    # visited = set()

    # while s.size() > 0: 
    #     v = s.pop()
    #     if v not in visited:
    #         print(v)
    #         visited.add(v)
    #         for neighbor in graph.get_neighbors(v):
    #             s.push(neighbor)

   
   
   
   
   
    s = Stack()
    s.push(starting_node)
    visited = set()
    path=[]
    while s.size() > 0: 
        v = s.pop()
        if v not in visited:
            print('v', v)
            visited.add(v)
            path.append(v)
            for neighbor in graph.get_neighbors(v):
                print(neighbor)
                s.push(neighbor)
    print('path', path)
    final = path[-1]
    print('final', final)
    if len(path) == 1:
        return -1
    if len(path) >= 3:
        print('len', len(path))
        if path[-1] in graph.get_neighbors(path[-3]) and path[-2] in graph.get_neighbors(path[-3]):
            return min(graph.get_neighbors(path[-3]))
    return final

    
    
    
    
    
    
    
    
    
    
    
    
    # print("starting", starting_node)
    # print("ancestors", ancestors)
    # pairs = []
    # for pair in ancestors:
    #     if starting_node in pair:
    #         pairs.append(pair)
    #         print('pairs', pairs)
    # # last_pair = pairs[-1:]
    # # print('last_pair', last_pair)
    # # last_ancestor = last_pair[0]
    # # print('last_ancestor', last_ancestor[0])
    # # if last_ancestor[0] == starting_node:\
    # #     return -1
    # # return last_ancestor[0]