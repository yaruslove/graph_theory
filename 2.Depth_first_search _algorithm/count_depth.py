import matplotlib.pyplot as plt
import networkx as nx

# В этой строчке задается случайное дерево на 20 вершинах. При каждом перезапуске блока будет создаваться новое дерево.
tree = nx.random_tree(12)


# Заводим множество посещенных вершин
visited = set()

# Здесь приведена краткая памятка по командам, которые могут потребоваться
# Следующая команда добавляет вершину v в множество посещенных
# visited.add(v)
# Следующая команда возвращает итератор по соседям вершины v
# tree[v]

# Функция должна возвращать глубину дерева с корнем v

v_root=0 # ввершина относительно которой считается

def count_depth(v_root):
    # Добавьте здесь ваше решение
    visited.add(v_root)
    depth = 0
    for u in tree[v_root]:
        if u not in visited:
            depth = max(depth, count_depth(u)+1)
    return depth


print(f'Глубина дерева: {count_depth(0)}')

nx.draw_networkx(tree)
plt.show()