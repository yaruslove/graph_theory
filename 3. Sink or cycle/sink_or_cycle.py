import networkx as nx

import matplotlib.pyplot as plt


# Мы посмотрим на примеры работы с ориентированными графами


# Задаем граф
G = nx.DiGraph()

G.add_edge('A','B')
G.add_edges_from([('B','C'), ('C','A'), ('C','D'), ('C','E'),('D','E'),('F','C')])


# Сначала мы отдельно реализуем проверку вершины на то, является ли она стоком.

# Затем мы реализуем функцию, которая находит вершину, которая либо является стоком, либо лежит на цикле. 
# Для этого достаточно для каждой вершины выбрать фиксированное исходящее ребро и переходить по этим ребрам n раз, где n — число вершин в графе.

# Наконец, затем мы реализуем функцию, которая находит в графе либо сток, либо цикл. 
# Для этого воспользуемся предыдущей функцией, и если она возвращает вершину на цикле, то мы проходим по циклу пока не попадем в начальную вершину второй раз, параллельно запоминая вершины цикла.



# В этом блоке нужно реализовать проверку вершины на то, является ли она стоком

def sink(G, v):
    # Добавьте здесь ваше решение
    return len(G[v]) == 0

v = 'C'
# v = 'E'
print(f'Вершина {v} является стоком: {sink(G, v)}')


# В этом блоке нужно реализовать функцию, которая по данному графу и данной вершине находит вершину, достижимую из данной, либо лежащую на цикле, либо являющуюся стоком

def find_cycle_or_sink(G, v):
    # Добавьте здесь ваше решение
    for _ in range(G.number_of_nodes()):
        if sink(G, v):
            return v
        v = list(G[v])[0]
    return v

print(find_cycle_or_sink(G, 'F'))

# В этом блоке нужно реализовать функцию, которая по данному графу и данной вершине, лежащей на цикле, выдает этот цикл

def build_cycle(G, v):
    cycle = [ v ]
    # Добавьте здесь ваше решение
    while list(G[v])[0] != cycle[0]:
        u = list(G[v])[0]
        cycle.append(u)
        v = u
    return cycle

v = find_cycle_or_sink(G, 'C')
if sink(G, v):
    print(f'Сток: {v}')
else:
    print(f'Цикл: {build_cycle(G, v)}')


# Отрисуем граф
nx.draw_networkx(G)
plt.show()