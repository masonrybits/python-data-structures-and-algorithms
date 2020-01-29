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
        visited_vertices = set()
        traversal_queue = Queue()

        traversal_queue.enqueue(vertex)

        while not traversal_queue.is_empty():
            current = traversal_queue.dequeue()
            vertices_list.append(current)

            for edge in self.get_neighbors(current):
                vertex = edge[0]
                if vertex not in visited_vertices:
                    visited_vertices.add(vertex)
                    traversal_queue.enqueue(vertex)

        return vertices_list

    def get_edge(graph, cities):
        cost = 0
        is_neighbor = False
        vertices = graph.get_nodes()

        if not cities or not vertices:
            return f'{is_neighbor} : ${cost}'

        chosen_vertices = []

        for city in cities:
            for vertex in vertices:
                if city == vertex.value:
                    chosen_vertices.append(vertex)
        if len(cities) != len(chosen_vertices):
            return f'{is_neighbor} : ${cost}'

        neighbors = graph.get_neighbors(chosen_vertices[0])

        for i in range(1, len(chosen_vertices)):
            is_neighbor = False
            for neighbor in neighbors:
                if neighbor[0] == chosen_vertices[i]:
                    cost += neighbor[1]
                    is_neighbor = True
                    break
            if not is_neighbor:
                return f'{is_neighbor} : $0'


class Vertex:
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    pass
