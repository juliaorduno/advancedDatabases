class GdfReader:
    def __init__(self, file):
        self.file = file
        self.graph = {}
        self.nodesInfo = {}
        self.nodes = 0
        self.edges = 0

    def getGraph(self):
        onEdge = False
        with open(self.file) as fp:
            for line in fp:
                if not onEdge:
                    if "edgedef" in line:
                        onEdge = True
                    elif "nodedef" not in line:
                        self.nodes += 1
                        line = line.split(',')[0:2]
                        self.nodesInfo[line[0]] = line[1]
                        self.graph[line[0]] = []
                else:
                    self.edges += 1
                    line = line.split(',')[0:2]
                    self.graph[line[0]].append(line[1])

    def writeGdf(self, graph):
        f = open("newgdg.gdf","w")
        f.write("nodedef>name VARCHAR,username VARCHAR\n")

        for key in self.nodesInfo:
            f.write(key + ',' + self.nodesInfo[key] + "\n")

        f.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN\n")

        for key in graph:
            for nodeid in graph[key]:
                f.write(key + ',' + nodeid + ',true\n')


                        

                        