"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        if vertex_id not in self.vertices:
            self.vertices[vertex_id] =  set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)



    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()



    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print(starting_vertex)
        #creating a set to store visited nodes
        visited = set()


        queue = Queue()

        #load the starting vertex into the que
        queue.enqueue(starting_vertex)
        #while the queue has a length
        while len(queue.queue) > 0:
            #remove the first node put in the list and set it to current node
            #print(f'queue before pop: {queue.queue}')
            currNode = queue.popleft()
            #print(f'queue after pop: {queue.queue}')
            #if the node has not been visited
            if currNode not in visited:
                #add the node to visited
                visited.add(currNode)
                print(currNode)
                #check the neighbors of the current node
                for neighbor in self.get_neighbors(currNode):
                    #if they are havent been visited add them to the path, and put them in the queue
                    if neighbor not in visited:
                        queue.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #setting up a stack
        stack = Stack()
        #adding the starting vertex to the stack
        stack.push(starting_vertex)
        #setting up a set to store visited values
        visited = set()
        #set up variable for returning the path
        path = []
        #if there is a length to the stack continue
        while len(stack.stack) > 0:
            #remove current node in stack and set currNode = to the value of that node
            currNode = stack.pop()
            print(currNode)
            # if the currNode is not currently in the visited set
            if currNode not in visited:
                #add it
                visited.add(currNode)
                #check each neighbor and add it to the stack
                for neighbor in self.get_neighbors(currNode):
                    stack.push(neighbor)


    def dft_recursive_helper(self, path, visited):
        #setting current value equal to the last thing in path
        curr = path[-1]
        #if it is not currently in visited
        if curr not in visited:
        #add it to visited:
            visited.add(curr)
            #for each neighbor of this node
            for neighbor in self.get_neighbors(curr):
                #if its not in visited
                if neighbor not in visited:
                    #add it to the path
                    path.append(neighbor)
                    #recurse until we run out of nodes that arent in visited
                    self.dft_recursive_helper(path, visited)


        return path








    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        establish a base case (when to return from your function)
            when you find the node return that currNode
            when you dont find the node return an empty set
        establish a recurse case(when to recurse)


        """
        #declare visited set

        visited = set()

        return self.dft_recursive_helper([starting_vertex], visited)
        # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        search works but i need to find a way to find the shortest path and track it in a list preferably in one pass
        """
        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])
        #if the starting_vertex is the destination
        if starting_vertex  ==  destination_vertex:
            return [starting_vertex], destination_vertex
        #otherwise start while loop
        while len(queue.queue) > 0:
            #set the current operating node to the first thing in the queue
            currPath = queue.popleft()
            currNode = currPath[-1]
            #check if this node has been visited and idd it if not
            if currNode not in visited:

                #check neighbors of currNode
                for neighbor in self.get_neighbors(currNode):
                    print(f'get_neighbors: {self.get_neighbors(currNode)}')
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.enqueue(neighbor)
                    #if the neighbors havent been visited
                    if neighbor == destination_vertex:
                        return newPath, neighbor
            visited.add(currNode)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        #adding the starting vertex to the stack
        stack.push(starting_vertex)
        #setting up a set to store visited values
        path = []
        visited = set()
        #if there is a length to the stack continue
        while len(stack.stack) > 0:
            #remove current node in stack and set currNode = to the value of that node
            currNode = stack.pop()
            # if the currNode is not currently in the visited set
            if currNode not in visited:
                #add it
                visited.add(currNode)
                path.append(currNode)
                if currNode ==destination_vertex:
                    return path
                #check each neighbor and add it to the stack
                for neighbor in self.get_neighbors(currNode):
                    stack.push(neighbor)
                     # TODO
    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        # set current vertex to the node pri
        curr_vertex = curr_path[-1]
        #break statement, if the current vertex is what wea re looking for then return that path(meaning the last one in the array)
        if curr_vertex == destination_vertex:
            return curr_path
        #add the current vertext to the visited vertex so we dont access it again
        visited.add(curr_vertex)
        #for each neighbor of the current vertex
        for neighbor in self.get_neighbors(curr_vertex):
            #if the neighbor has not been visited
            if neighbor not in visited:
                #make a list containing each element in curr_path
                newPath = list(curr_path)
                #append the new element to the path at the end so we operate on it during the next pass
                newPath.append(neighbor)
                # when the variable is declared recurse, once the path is found we move to the next if statement, if there is a length of the path then that means that we found the path otherwise we return an empty array
                res = self.dfs_recursive_helper(newPath, destination_vertex, visited)

                if len(res) > 0:
                    return res
        return []

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        establish a base case (when to return from your function)
            when you find the node return that currNode
            when you dont find the node return an empty set
        establish a recurse case(when to recurse)

        This should be done using recursion.
        """
        #setting up the visited set, then return the helper function
        visited = set()
        #setting first iteration of recursion and the return will be the reult of recursing that function inside itslef until completion
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)
        # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(f'bft{graph.bft(1)}')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print(f'recursove: {graph.dft_recursive(1)}')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'bfs: {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
