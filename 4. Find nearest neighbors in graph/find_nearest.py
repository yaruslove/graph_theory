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


# В этом блоке требуется реализовать метод числа общих соседей. 
# Функция в ячейке i списка common_neigh должна сохранить число общих соседей query и i. 
# Но есть одна тонкость: ячейку с номером query и с номерами ее соседей правильно обнулить, 
# а то нам будут рекомендовать соединить query с query или ее соседями
# Это можно сделать с помощью функции exclude_obvious_answers

def common_neighbours(graph, query):
    common_neigh = [0] * len(graph)
    ### BEGIN SOLUTION
    for versh in graph:
        # print(versh)
        if versh==query or query in graph[versh]:
            common_neigh[versh]=0
        else:
            common_neigh[versh]=len(set(graph[versh]) & set(graph[query]))
    ### END SOLUTION
    return common_neigh


# Тестирование
query = 422
samp = [35561, 98891, 157171, 3060, 198304, 28054, 226896, 20673, 110999, 125875, 125877, 20342, 208996, 205186, 829, 189415, 212872, 164896, 104718, 78418]
graph = generate_dict(query, samp)

test_query = 377
test_samp = [202525, 196341, 169969, 29141, 159961, 38249, 101144, 1157, 40361, 99572, 64355, 127194, 109845, 217286, 125972, 77367, 6658, 26295, 47705, 200935]
test_graph = generate_dict(test_query, test_samp)


ans = common_neighbours(graph, query)
ind_sort = index_sorted(ans, reverse=True)[:len(samp)]
chck_ans = check_answer(ans, samp, reverse=True)
print("Ваши ответы:")
print("ТОП по числу соседей:", ind_sort)
print("Число совпадений с удалёнными рёбрами:", chck_ans)
print("Если получилось 5, возможно, вы забыли исключить query и соседей")
print("Если получилось 0, возможно, вы неправильно использовали exclude_obvious_answers")

print("Результаты тестов:")
assert chck_ans == 8
assert ind_sort == [829, 3060, 20673, 13141, 21150, 35561, 36377, 103988, 110999, 172699, 4863, 8961, 10572, 16003, 20342, 28054, 53201, 70084, 70323, 104718]
print("ОК")