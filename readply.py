'''
reading a ply file without external libraries
'''


class ply:

    def __init__(self):
        self.img = None
        self.vertices = []
        self.v = 0
        self.faces = []
        self.f = 0
        self.edges = []
        self.e = 0

    def __edges(self):
        for face in self.faces:
            for i in range(-1, len(face)-1):
                if [face[i], face[i+1]] not in self.edges and [face[i+1], face[i]] not in self.edges:
                    self.edges.append([face[i], face[i+1]])
                    self.e += 1

    def read(self, img):
        self.img = img
        with open(self.img, 'r') as img:
            line = img.readline()
            while line:
                # print(line)
                if line.split()[0] == 'element':
                    if line.split()[1] == 'vertex':
                        self.v = int(line.split()[2])
                    if line.split()[1] == 'face':
                        self.f = int(line.split()[2])

                elif line.split()[0] == 'end_header':
                    for i in range(self.v):
                        val = img.readline()
                        self.vertices.append(list(map(int, val.split())))
                    for i in range(self.f):
                        val = img.readline()
                        self.faces.append(list(map(int, val.split()[1:])))

                line = img.readline()

        self.__edges()


'''
p = ply()
p.read(img='f:\sem\CS-667\hw\dcel\plies\\ant.ply')
print(p.faces, '\n')
print(p.e, p.edges, '\n')
print(p.vertices, '\n')
'''