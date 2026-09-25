def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    # numbers = []

    # for number in range(1, n + 1):
    #     numbers.append(str(number))

    # print( " ".join(numbers))

    # OR WE CAN USE THIS!!!

    print(" ".join(str(number) for number in range(1,n+1)))

number_pattern(12)




def simple_perceptron2(input_data : list) -> float:
    if len(input_data) != 3:
        raise Exception("Invalid input data length!")
    weight1 = [[0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
        [0.7, 0.8, 0.9]]
    b1 = [[-0.4, -0.4, -0.4],
        [0.5, 0.5, 0.5],
        [-0.6, -0.6, -0.6]]
    weight2 = [0.2, 0.5, 0.3]
    b2 = [0.0, -0.3, -0.3]
    layer1_size = 3;
    layer2_size = 3;
    layer1 = [0] * layer1_size;
    for x, w_, b_, i in zip (input_data, weight1, b1, range(layer1_size)):
        layer1[i] = 1 if sum(x* w + b for w, b in zip(w_, b_)) >= 0 else 0
    result = 1 if sum(x * w + b for x, w, b in zip(layer1, weight2, b2)) >= 0 else 0
    return result



N = 7
FIO = ['Ivanova', 'Petrova', 'Sidorova', 'Kuznetsova', 'Fedorov', 'Golubev']
subject1 = [21, 95, 35, 27, 46, 78, 59]
subject2 = [81, 10, 69, 76, 45, 92, 50]
sum_value = 0.0
for s1, s2 in zip (subject1, subject2):
    sum_value = sum_value + s1 + s2
average_score = sum_value / (N * 2.0)

result = {}


for f, s1, s2 in zip (FIO, subject1, subject2):
    if (s1 + s2) / 2.0 > average_score:
        result[f] = (s1 + s2) /2.0

print(result)



def KNN (z : list) -> str:
    X = [1.0, 4.0, 7.0]
    Y = [4.0, 1.0, 4.0]
    data_class = ['A', 'B', 'A']
    k=2
    point_in_class = {'A' : 0, 'B': 0}
    minimum_distance = {'A': float("inf"), 'B' : float("inf")}

    if len(z) != 2:
        raise Exception("Invalid input data length!")

    distance_to_point = []
    for x, y in zip(X, Y):
        distance_to_point.append(( abs(x-z[0]) + abs(y-z[1])))

        distance_and_class = sorted(zip(distance_to_point, data_class))[:k]

        for distance, c in distance_and_class:
            point_in_class[c] += 1
            minimum_distance[c] = min(minimum_distance[c], distance)


    if (point_in_class['A'] > point_in_class['B']):
        return 'A'
    elif (point_in_class['A'] < point_in_class['B']):
        return 'B'
    else:
        if (minimum_distance['A'] < minimum_distance['B']):

            return 'A'
        else:
            return 'B'