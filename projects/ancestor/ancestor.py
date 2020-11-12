#test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#Step 1, represent the starting node by setting it equal to the index of the node in the graph
'''
   10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''
from collections import deque
from collections import defaultdict
#issue is finding a way to store the oldest parent values and then evaluate which one to return
#main issue is that the current implamentation requires the while loop to run
#i need to either switch to nested for loops (inifecient)
#or find a way to properly track without retuninig a value
def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    stack.append((starting_node, 0))# node and distance
    visited = set()
    earliestAncestor = (starting_node, 0)
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)
        if currNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = currNode
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))



def createGraph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
