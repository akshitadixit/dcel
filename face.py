class Face:
    all = []

    def __init__(self, vertices, i):
        self.outer = False  # assuming inner face
        self.vertices = vertices
        self.edges = []
        self.i = i
        Face.all.append(self)

    def __str__(self) -> str:
        return f'F{self.i}'

    def __repr__(self) -> str:
        return f'Face(i={self.i}, vertices={" ".join(list(map(str, self.vertices)))}, edges={ " ".join(list(map(str, self.edges)))})'

    def adjacent(self):
        '''
        access adjacent face(s)
        '''
        adj = []
        for e in self.edges:
            adj.append(e.twin.face)
            # adding face on which twin(e) is incident

        return adj

    def visit_edges(self):
        '''
        walk around the boundary of a face in counter clockwise
        '''
        e = self.edges[0]
        beg = e
        while next(e) != beg:
            print(e.name)
            e = e.next
