class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = "white"
        self.distance = float('inf')
        self.p = None
        self.adjVertices = []
#
#
# vertices = 7
# listOfVertices = []
#
# for i in range(vertices):
#     listOfVertices.append(Vertex(i))
#
# for i in listOfVertices:
#     print(i.key)


l = []
l.append(0)
l.append(1)
print(l.pop())