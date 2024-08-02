from queue import Queue
graph={'A':['B','D','E','F'],'D':['A'],'B':['A','F','C'],'F':['B','A'],'C':['B'],'E':['A']}
print("given graph is:")
print(graph)
def BFS(input,source):
    Q=Queue()
    visited_vertices=list()
    Q.put(source)
    visited_vertices.append(source)
    while not Q.empty():
        vertx=Q.get()
        print(vertx,end="")
        for u in input[vertx]:
            if u in visited_vertices:
                   Q.put(u)
                visited_vertices.append(u)
    print("\nBFS traversal of graph with source A is:")
BFS(graph,"A")
