class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def mergeSort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left_part = arr[:mid]
    right_part = arr[mid:]

    left = mergeSort(left_part, key)
    right = mergeSort(right_part, key)

    if key == "X":
        return mergeX(left, right)
    elif key == "Y":
        return mergeY(left, right)

def mergeX(left, right):
    sort_arr = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].get_x() <= right[j].get_x():
            sort_arr.append(left[i])
            i += 1
        else:
            sort_arr.append(right[j])
            j += 1

    for k in range(i, len(left)):
        sort_arr.append(left[k])

    for k in range(j, len(right)):
        sort_arr.append(right[k])

    return sort_arr

def mergeY(left, right):
    sort_arr = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].get_y() <= right[j].get_y():
            sort_arr.append(left[i])
            i += 1
        else:
            sort_arr.append(right[j])
            j += 1

    for k in range(i, len(left)):
        sort_arr.append(left[k])

    for k in range(j, len(right)):
        sort_arr.append(right[k])

    return sort_arr


def distance(point1, point2):
    return (((point1.x - point2.x)**2) + ((point1.y - point2.y)**2))**0.5


def closest_pair(arrX, arrY):
    lengthArr = len(arrX)

    if lengthArr <= 3:
        dist = float('inf')
        index1 = -1
        index2 = -1

        for i in range(lengthArr):
            for j in range(i + 1, lengthArr):
                dis = distance(arrX[i], arrX[j])

                if dis < dist:
                    dist = dis
                    index1 = arrX[i].index
                    index2 = arrX[j].index

        return dist, index1, index2

    mid = lengthArr // 2
    point_in_middle = arrX[mid].x

    leftX = arrX[:mid]
    rightX = arrX[mid:]

    leftY = []
    rightY = []

    for i in arrY:
        if i.x <= point_in_middle:
            leftY.append(i)

    for j in arrY:
        if j.x > point_in_middle:
            rightY.append(j)

    dist1, i1, j1 = closest_pair(leftX, leftY)
    dist2, i2, j2 = closest_pair(rightX, rightY)

    if dist1 < dist2:
        dis = dist1
        index1 = i1
        index2 = j1
    else:
        dis = dist2
        index1 = i2
        index2 = j2


    arr = []

    for p in arrY:
        if abs(p.x - point_in_middle) < dis:
            arr.append(p)

    for i in range(len(arr)):
        for j in range(i + 1, min(i + 7, len(arr))):
            dist = distance(arr[i], arr[j])
            if dist < dis:
                dis = dist
                index1 = arr[i].index
                index2 = arr[j].index

    return dis, index1, index2


def main(times):
    points = []
    for i in range(times):
        x, y = list(map(int, input().split()))
        point = Point(x, y, i + 1)
        points.append(point)

    arrX = mergeSort(points, "X")
    arrY = mergeSort(points, "Y")

    distance, index1, index2 = closest_pair(arrX, arrY)
    print(f"{index1} {index2} {round(distance, 6)}")

n = int(input())
main(n)