import math
from tkinter import ALL

# edge refers to half-edge


class Edge:
    all = []

    def __init__(self, origin, end):
        self.origin = origin  # incident on vertex
        self.end = end
        self.face = None  # incident on face
        self.prev = None
        self.next = None
        self.twin = None
        Edge.all.append(self)

    def edge(v1, v2):
        for e in Edge.all:
            if e.origin == v1 and e.end == v2:
                return e

    def __str__(self) -> str:
        return f'E({self.origin},{self.end})'

    def __repr__(self) -> str:
        return f'Edge(({self.origin},{self.end}), face={self.face}, next={self.next}, prev={self.prev} twin={self.twin})'

    def __len__(self):
        return math.sqrt((self.prev.origin.x - self.origin.x)**2 + (self.prev.origin.y - self.origin.y)**2)

    def angle(self):
        # find angle wrt x-axis
        dx = self.origin.x - self.prev.origin.x
        dy = self.origin.y - self.prev.origin.y
        dz = self.origin.z - self.prev.origin.z

        return math.acos(dx/math.sqrt(dx*dx + dy*dy + dz*dz)) if dy > 0 else 2*math.pi - math.acos(dx/math.sqrt(dx*dx + dy*dy + dz*dz))

    '''@property
    def twin(self):
        return Edge()'''
