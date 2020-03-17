import functools

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
            for next_vertex in self.vertices[v]:
                q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size():
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)
            for next_vertex in self.vertices[v]:
                s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited={}):
        visited[starting_vertex] = True
        print(starting_vertex)
        for v in self.vertices[starting_vertex]:
            if v not in visited:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size > 0:
            path = q.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
            visited.add(vertex)

            for next_vertex in self.vertices[vertex]:
                new_path = list(path)
                new_path.append(next_vertex)
                q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path

                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    s.push(new_path)
        return None

    def previous_children(self, starting_vertex):
        queue = Queue()
        visited = set()
        paths = []
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            current_vertex = path[-1]
            if current_vertex not in visited:
                if not len(self.vertices[current_vertex]):
                    paths.append(path)
                visited.add(current_vertex)
                for next_vertex in self.vertices[current_vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)
        right_path = functools.reduce(lambda a,b: a if len(a) > len(b) else b, paths)
        if len(right_path) > 1:
            return right_path[-1]
        return -1


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for edge in ancestors:
        if edge[0] not in graph.vertices:
            graph.add_vertex(edge[0])
        if edge[1] not in graph.vertices:
            graph.add_vertex(edge[1])
    for edge in ancestors:
        graph.add_edge(edge[1], edge[0])
    return graph.previous_children(starting_node)
