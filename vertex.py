class Vertex:
    all = []

    def __init__(self, x, y, z, i):
        self.x = x
        self.y = y
        self.z = z
        self.edges = []  # list of incident half-edges
        self.i = i
        Vertex.all.append(self)

    def __str__(self) -> str:
        return f'V{self.i}'

    def __repr__(self) -> str:
        return f'Vertex(i={self.i}, ({self.x},{self.y},{self.z}), edges={ " ".join(list(map(str, self.edges)))})'

    '''@property
    def edges(self, *args, **kwargs):
        # incident half-edges' list around the vertex
        # initialize/access half-edges here
        pass'''

    def visit_edges(self):
        '''
        visit all edges around given vertex
        '''
        e = self.edges[0]
        beg = e
        while next(e) != beg:
            print(e.name)
            e = e.next

    def visit_vertices(self):
        '''
        visit all vertices connected to given vertex
        '''
        e = self.edges[0]
        beg = e
        while next(e) != beg:
            print(e.origin.name)
            e = e.next
