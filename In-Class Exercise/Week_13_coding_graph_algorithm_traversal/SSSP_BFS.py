class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    def bfs(self, start, end):
        queue = []
        queue.append([start]) # store full path, not only node

        while queue:
            path = queue.pop(0) # FIFO, remove first item from queue
            node = path[-1] # take the last node from current path
            if node == end: # if the destination reached then
                return path # return the shortest path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path) # copy the current path
                new_path.append(adjacent) # add neighbour node
                queue.append(new_path) # add new path to queue


my_graph = {"a": ["b", "c"],
            "b": ["d", "g"],
            "c": ["d", "e"],
            "d": ["f"],
            "e": ["f"],
            "g": ["f"]}


graph_path = Graph(my_graph)
print(graph_path.bfs("a", "d"))