points = [(2, 5), (5, 2), (6, 6), (8, 3), (9, 1), (2, 3), (4, 4), (5, 5),
          (6, 6)]  # координаты - список кортежей, через запятую, указывается вручную
start_point = (0, 2)  # стартовая точка - кортеж, указывается вручную
distance = 0
point_neighbour = 0


def find_length(point_1, point_2):  # вычисление расстояния
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


current_point = start_point

while True:  # поиск пути через "Алгоритм ближайшего соседа"
    min_length = 0
    for i in points:  # поиск ближайшей точки
        if find_length(current_point, i) < min_length or min_length == 0:
            min_length, point_neighbour = find_length(current_point, i), i

    distance += min_length

    if points:
        print("{} --> {}{}".format(
            current_point,
            point_neighbour,
            distance
        ))
        points.remove(point_neighbour)
    else:  # если список пуст, значит мы прошли все пункты. следующий пункт - стартовая точка
        point_neighbour = start_point
        points.append(start_point)
        continue

    if point_neighbour == start_point:  # завершение программы, если конечная точка = начальной точке. мы вернулись
        # обратно
        print('Кратчайший путь = ' + str(distance))
        break

    current_point = point_neighbour
