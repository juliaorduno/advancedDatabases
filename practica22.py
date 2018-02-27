from GdfReader import GdfReader

reader = GdfReader('bigbang.gdf')
reader.getGraph()
reader.getInGraph()

ranks = {}

for node in reader.graph:
    c = len(reader.graph[node])
    ranks[node] = [1, c]


def pageRank(ranks, graph, inGraph, d):

    for node in ranks:
        neighbors = 0
        pr = 0
        for n in inGraph[node]:
            if len(reader.graph[n]) > 0:
                pr = ranks[n][0]
                c = ranks[n][1]
                neighbors += pr/c
        pr = (1-d) + d * neighbors
        ranks[node][0] = pr
    
    return ranks

for i in range(20):
    pageRanks = pageRank(ranks, reader.graph, reader.inGraph, 0.7)

total = 0
c = 0
maxRank = '44596321012'
minRank = '44596321012'
for node in reader.graph:
    c += 1
    if node in pageRanks:
        total += pageRanks[node][0]
        if pageRanks[node][0] > pageRanks[maxRank][0]:
            maxRank = node
        if pageRanks[node][0] < pageRanks[minRank][0]:
            minRank = node

print "\nAVERAGE = " + str(total/c)
print "\nMAX RANK = " + reader.nodesInfo[maxRank] + " : " + str(pageRanks[maxRank][0])
print "\nMIN RANK = " + reader.nodesInfo[minRank] + " : " + str(pageRanks[minRank][0])


