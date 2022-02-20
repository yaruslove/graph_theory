import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()

graph.add_nodes_from(['A','B','C','D','E','F'])
graph.add_edges_from([('A','B'), ('B','C'), ('C','A'),('B','D'),('B','E'),('D','E')])

pre={}
post={}

def Previsit(v, pre, clock):
    pre[v]=clock
    clock+=1
    return clock

def Postvisit(v, post, clock):
    post[v]=clock
    clock+=1
    return clock

visited=dict()
for v in graph:
    visited[v]=False

def Explore(v,graph,pre,post,clock,visited):
    visited[v]=True
    clock = Previsit(v,pre,clock)
    for u in graph[v]:
        if not visited[u]:
            clock = Explore(u,graph,pre,post,clock,visited)
    clock = Postvisit(v,post,clock)
    return clock
            
def dfs(graph,pre,post,visited):
    clock=0
    for v in graph:
        if not visited[v]:
            clock = Explore(v,graph,pre,post,clock,visited)

dfs(graph,pre,post,visited)

print("Pre:\t",sorted(pre.items()))
print("Post:\t",sorted(post.items()))

nx.draw_networkx(graph)
plt.show()
