from math import sqrt

def euclidean_distance(row1,row2):
    distance=0.0
    for i in range(len(row-1)-1):
        distance+=(row1[i]-row[i])**2
        return sqrt(distance)
def get_neighbors(train, test_row, num_neighbours):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((trian_row,dist))
        distances.sort(key=lambda tup:tup[1])
        neighbors= list()
        for i in range (num_neighbors):
            neighbors.append(distances[i][0])
            return neighbors
dataset = [[8.4,7.3,0],
           [8,6.8,0],
           [7.4,7.2,0],
           [6.2,4.7,0]
           [6,4.6,0],
           [5.8,4.3,0],
           [5.9,4.3,0],
           [5.8,4,0],
           [7.1,7.8,0],
           [7.4,7,0],
           [6.9,7.3,0],
           [9,9.4,0],
           [9.2,9.2,0],
           [9.6,9.2,0],
           [7.5,9.2,0],
           [7.4,7.4,0],
           [7.6,7.9,0],
           [7.2,10.3,0],
           [7.3,10.5,0],
           [7.2,9.2,0],
           [7.3,10.2,0],
           [5.8,8.7,0]]
neighbors = get_neighbors(dataset,dataset[0],3)
for neighbor in neighbors:
    print(neighbor)
