# В этом блоке мы загружаем граф из файла и приводим его в вид, удобный для работы

import networkx as nx

amazon = nx.read_edgelist("./amazon0302.txt", create_using=nx.Graph(), nodetype=int, data=False)
amazon = nx.convert_node_labels_to_integers(amazon, ordering='decreasing degree')
nodes = amazon.number_of_nodes()



#мы фиксируем вершину (в коде ниже это переменная query);
#удаляем некоторые смежные с ней ребра (в коде ниже это список samp);
#вычисляем специально определенное расстояние между нашей вершиной и всеми остальными (методы различаются как раз выбором расстояния);
#выбираем вершины с наименьшим расстоянием до выбранной, это те вершины, в которые метод предлагает провести ребра;
#сравниваем предложенные методом ребра с удаленными, чем больше совпадений, тем лучше сработал метод.


##### В данном методе расстоянием является просто число общих соседей  #####



# Эта функция получив на вход словарь упорядочивает его по значению меток
def index_sorted(a, reverse=False):
    return sorted(range(len(a)), key=lambda k: a[k], reverse=reverse)

# Эта функция позволяет выбрать ответ из посчитанных расстояний и сравнить его с целевым значением. 
# Она выбирает нужное количество вершин с минимальным расстоянием и находит число совпадений с удаленными ребрами.
# Здесь stat — это словарь с расстояниями, а samp — количество выбираемых вершин с минимальным расстоянием.
def check_answer(stat, samp, reverse=False): 
    index_dist = index_sorted(stat, reverse)
    guess = index_dist[:len(samp)]
    return len(set(samp) & set(guess))

# Эта функция генерирует тестовый пример, удаляя данные ей ребра из графа.
# Здесь samp — количество удаляемых ребер.
# Здесь мы также конвертируем граф в словарь списков
def generate_dict(query, samp):
    graph = amazon.copy()
    for i in samp:
        graph.remove_edge(query, i)
    return nx.convert.to_dict_of_lists(graph)


# В отличие от функций в блоке выше, которые уже использованы в проверках,
# эта является подсказкой к тому, что вам самим нужно сделать после работы
# каждого из алгоритмов (в блоках SOLUTION). Конечно, эту функцию можно
# менять, если вам будет нужно.

# Так самые близкие к заданой вершине это сама вершина и ближайшие соседи их исключим!

    
def exclude_obvious_answers(graph, query, answers, worst_metric):
    answers[query] = worst_metric
    for neigh in graph[query]:
        answers[neigh] = worst_metric


query = 422
samp = [35561, 98891, 157171, 3060, 198304, 28054, 226896, 20673, 110999, 125875, 125877, 20342, 208996, 205186, 829, 189415, 212872, 164896, 104718, 78418]
graph = generate_dict(query, samp)

test_query = 377
test_samp = [202525, 196341, 169969, 29141, 159961, 38249, 101144, 1157, 40361, 99572, 64355, 127194, 109845, 217286, 125972, 77367, 6658, 26295, 47705, 200935]
test_graph = generate_dict(test_query, test_samp)

# В этом блоке требуется реализовать метод случайных блужданий.
# Обратите внимание на массив used: его можно использовать для того, чтобы проверять, посещалась ли вершина в блуждании ранее
# Причем удобно не ставить там метку того, была ли посещена вершина в текущем блуждании.
# Вместо этого можно хранить номер последней итерации, на которой была посещена вершина, и сравниваем его с текущим.

import random


# РЕШЕНИЕ!
def hit_distance(adjlist, query, time=10):
    hit_dist = [0] * nodes  # искомые расстояния
    hit_times = [0] * nodes  # количество раз, когда вершина была достигнута в блуждании
    used = [0] * nodes # последняя итерация, на которой вершина была достигнута в блуждании
    samples = nodes // time  # количество блужданий
    ### BEGIN SOLUTION
    for sample in range(samples):
        v = query
        used = [0] * nodes
        for i in range(time):
            node = random.choice(adjlist[v]) # Делаем случаынй шаг из узла
            v = node
            if used[node]<=0: 
                used[node] = i
                hit_dist[node] += i
                hit_times[node] += 1
        
    updt_hit_dist=[]
    for dist, h_times in zip(hit_dist,hit_times):
        updt_hit_dist.append((dist+(samples-h_times)*time)/samples)
    worst_metric = time
    hit_dist=updt_hit_dist

    exclude_obvious_answers(adjlist, query, hit_dist, worst_metric)             
    ### END SOLUTION

    return hit_dist


hd = hit_distance(graph, query)
hd_check = check_answer(hd, samp)
print("Совпадений с удалёнными рёбрами:", hd_check)
print("Если ответ 2 -- не исключили query и соседей, если 0 -- исключили неправильно")
assert hd_check >= 8
print("OK")


test_hd = hit_distance(test_graph, test_query)
hd_check = check_answer(test_hd, test_samp)
print("Совпадений с удалёнными рёбрами:", hd_check)
assert hd_check >= 9
print("OK")