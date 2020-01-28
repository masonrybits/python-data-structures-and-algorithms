from queue import Queue


class Graph:

    def __init__(self):

        self._adjacency_list = {}

    def add_node(self, value):
        """adds a vertex"""
        v = Vertex(value)

        self._adjacency_list[v] = []

        return v

    def size(self):
        '''return the number of vertices in the graph'''
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''add connection between start node and end node, with an optional weight. raise errors if neither exists.'''

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append((end_vertex, weight))

    def get_nodes(self):
        '''return a list of vertices'''
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        '''return the neighbors of a given node'''
        return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        vertices_list = []
        visited_vertices = set([vertex])
        traversal_queue = Queue()

        traversal_queue.enqueue(vertex)

        while not traversal_queue.is_empty():
            current = traversal_queue.dequeue()
            vertices_list.append(current)

            for vertex in self.get_neighbors(current):
                vertex = vertices_list[0]
                if vertex not in visited_vertices:
                    visited_vertices.add(vertex)
                    traversal_queue.enqueue(vertex)

        return vertices_list


class Vertex:
    def __init__(self, value):
        self.value = value
