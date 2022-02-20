# Здесь мы загружаем библиотеку для работы с графами

import networkx as nx
import matplotlib.pyplot as plt

# Эта функция по данному списку чисел строит дерево с соответствующими степенями вершин, мы обсуждали эту задачу на занятии
# Мы используем эту функцию здесь для генерации тестовых примеров


def create_tree(degrees):

    graph = nx.Graph()
    n = len(degrees)
    # Здесь мы проверяем условия, которым должен удовлетворять набор чисел
    if any([elem <= 0 for elem in degrees]) or sum(degrees) != 2 * n - 2:
        return None

    # Здесь мы заводим граф и заводим вершины в нем
    graph.add_nodes_from(range(n))
    for _ in range(n - 1):
        # Выбираем какую-нибудь вершину степени 1
        i = degrees.index(1)
        degrees[i] -= 1
        # Выбираем вершину максимальной степени 
        j = degrees.index(max(degrees))
        graph.add_edge(i, j)
        degrees[j] -= 1

    return graph


# Здесь мы задаем пример дерева, он может быть полезен для тестирования алгоритма. 

G = create_tree([1, 3, 1, 2, 1, 3, 1])
# G = create_tree([2, 4, 2, 3, 2, 4, 2, 1, 1, 1, 1, 1, 2, 1, 1])


# Отрисуем изначальный граф
nx.draw_networkx(G)
plt.show()


# Создадим копию графа, чтобы не портить основной
H = G.copy()

# Этой командой можно удалить вершину
H.remove_node(1)


# Этой командой можно добавить ребро
H.add_edge(0,2)


# Печатаем соседей вершины 2 и ее степень
print(f"Степень вершины 2 равна {H.degree(2)}, а ее соседи, это {list(H[2])}")



# В этом блоке нужно реализовать стягивание ветвей дерева

def construct_branch_tree(G):
    # Создаем копию списка вершин, она может пригодиться
    node_list = list(G.nodes()).copy()
    # Реализуйте здесь стягивание ветвей
    while 2 in dict(G.degree()).values():
        for i in G.degree():
            if i[1]==2:
                neibours=list(G[i[0]])
                # print(list(G[i[0]]) )# соседи
                G.remove_node(i[0])
                G.add_edge(neibours[0],neibours[1])
                break
            
    return G

H = construct_branch_tree(G.copy())

# Отрисуем стянутый граф
nx.draw_networkx(H)
plt.show()
