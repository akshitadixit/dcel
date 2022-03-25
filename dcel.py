import imp
from readply import ply
from face import Face
from edge import Edge
from vertex import Vertex
from array import array
from pprint import pp


class DCEL:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def process(self, img):
        p = ply()
        p.read(img=img)
        # p.vertices, p.faces, p.edges
        for v in range(p.v):
            x, y, z = p.vertices[v]
            p.vertices[v] = Vertex(x, y, z, v)

        for f in range(p.f):
            p.faces[f] = Face([p.vertices[i] for i in p.faces[f]], f)

        for e in range(p.e):
            edge = p.edges[e]
            p.edges[e] = Edge(p.vertices[edge[0]], p.vertices[edge[1]])
            temp = Edge(p.vertices[edge[1]], p.vertices[edge[0]])
            p.edges[e].twin, temp.twin = temp, p.edges[e]
            # vert
            p.vertices[edge[1]].edges.append(p.edges[e])
            p.vertices[edge[0]].edges.append(temp)

        # face ke edges
        for face in p.faces:
            for v in range(-1, len(face.vertices)-1, 1):
                edge = Edge.edge(face.vertices[v], face.vertices[v+1])
                face.edges.append(edge)
                edge.face = face
            for e in range(-1, len(face.edges)-1, 1):
                face.edges[e].next = face.edges[e+1]
                face.edges[e+1].prev = face.edges[e]
                face.edges[e+1].twin.next = face.edges[e].twin
                face.edges[e].twin.prev = face.edges[e+1].twin

        '''
        Uncomment the code below to view all vertices, edges and faces.
        pp(Vertex.all)
        pp(Edge.all)
        pp(Face.all)
        '''

# linear for v, e and f

'''
utility code for DCEL
'''
unit = DCEL()
unit.process('f:\sem\CS-667\hw\dcel\plies\\ant.ply')


# any(b[idx : idx + len([0,1])] == [0,1] for idx in range(len(b) - len([0,1]) + 1))
# check sublist in list
