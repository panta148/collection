"""
this is breath first search(BFS) algorithm implementation 
"""
'''
the algorithms of BFS is as follow:
1.place the start node at the queueu
2.if the queue is empty retuen false and stop
3.if the first element on the queuee is goal node retuen success and stop otherwise 
4.remove and expand the first element froom the queue and place all the element at the end of the queue
5.return too the state 2
'''

# this function is for making the graph  with the dictionary input


def createGraph(graph):
    n = int(input("Enter the number of nodes in graph -> "))
    for i in range(n):
        node = input(
            "Enter nodes and connectedNodes in the following format \n node:connectedNode1,connectedNode2.....and so on ->").split(":")
        graph[node[0]] = node[1].split(",")
    return graph


def bfs(graph, start, dest):
    result = ['Not reachable', list()]
    visited = list()
    queue = list()
    queue.append(start)
    visited.append(start)
    while queue:
        currentNode = queue.pop(0)
        if currentNode not in graph.keys():
            continue
        for node in graph[currentNode]:
            if node not in graph.keys():
                continue
            if node == dest:
                result[0] = 'Reachable'
                break
            if node not in visited:
                visited.append(node)
                queue.append(node)

    result[1] = visited
    return result


makegraph = dict()
finalgraph = createGraph(makegraph)
start = input("Enter the starting point of the travesal => ")
end = input("Enter the ending point of the travesal => ")
print("\n Final graph is look like these\n")
for item, value in finalgraph.items():
    print('\t\t\t\t', item, ":", value)
result = bfs(finalgraph, start, end)
print("Result:", result[0])
print("Path traversed:", result[1])
