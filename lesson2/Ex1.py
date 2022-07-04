points: list = [(2, 5), (5, 2), (6, 6), (8, 3)]
start_point = (0, 2)
distance = 0
point_neighbour = 0

def find_length(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

current_point = start_point

while True:
    min_lengh = 0
    for i in points:
        if min_lengh == 0: 
            min_lengh, point_neighbour = find_length(current_point, i), i
        if find_length(current_point, i) < min_lengh:
            min_lengh, point_neighbour = find_length(current_point, i), i
    
    distance += min_lengh

    if points != []:
        print("{} --> {}{}".format(
        current_point, 
        point_neighbour,
        distance
        ))
        points.remove(point_neighbour)
    else:
        point_neighbour = start_point
        points.append(start_point)
        continue

    if point_neighbour == start_point:
        print('Кратчайший путь = ' + str(distance))
        break
    
    current_point = point_neighbour