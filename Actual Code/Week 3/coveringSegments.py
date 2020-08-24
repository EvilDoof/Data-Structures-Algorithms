#To find least number of points required to ensure each segment has one point

#Safe move: Starting from the left, go to the right and insert point at the first end point

def optimalPoints(startPoints, endPoints):
    startPoints = [x for _,x in sorted(zip(endPoints, startPoints))]
    endPoints = sorted(endPoints) 
    points = list()
    while (len(endPoints) != 0):
        points.append(endPoints[0])
        while True:
            if (len(startPoints) == 0 or startPoints[0] > points[-1]):
                break
            del startPoints[0]
            del endPoints[0]
            if (len(startPoints) == 0):
                break
    return points

#Main function
if __name__ == '__main__':
    n = int(input())
    startPoints = list()
    endPoints = list()
    for i in range(n):
        x, y = map(int, input().split())
        startPoints.append(x)
        endPoints.append(y)
    points = optimalPoints(startPoints, endPoints)
    print(len(points))
    print(*points)