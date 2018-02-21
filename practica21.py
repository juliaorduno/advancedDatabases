from GdfReader import GdfReader

def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start]= 0    # depth of start node is 0

    visited= [start]     # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be checked
    while queue:
       # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
    return explored

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

reader = GdfReader('bigbang.gdf')
reader.getGraph()

#reader.writeGdf()

bfsGraph = bfs(reader.graph, '22934684677')
dfsGraph = dfs(reader.graph, '22934684677', [])
c = 1
print 'BFS'
for node in bfsGraph:
    c +=1
    if node == '8811587900':
        break
print c

c = 1
print '\nDFS'
for node in dfsGraph:
    c+=1
    if node == '8811587900':
        break
print c


    