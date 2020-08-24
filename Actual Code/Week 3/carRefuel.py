# python3
#Input: The first line contains an integer𝑑. The second line contains an integer𝑚. The third linespecifies an integer𝑛. Finally, the last line contains integersstop1,stop2, . . . ,stop
#Output: Minimum number of stops required else -1 if not possible

#Safe move: Travel the most possible distance between each stop

def compute_min_refills(distance, tank, stops):
    noOfStops = 0
    lastStop, currentStop = (0, 0)
    while (stops[currentStop] != distance):   
        if (stops[currentStop+1] - stops[lastStop] > tank):
            if (currentStop == lastStop): #To see if reaching next stop is impossible
                return -1
            noOfStops = noOfStops + 1
            lastStop = currentStop
        else:
            currentStop = currentStop + 1
    return noOfStops

if __name__ == '__main__':
    d = int(input()) #Total Distance
    m = int(input()) #Distance travelled on full tank
    n = input() #Placeholder for number of stations. Not required
    stops = [0]
    stops.extend(map(int,input().split()))
    stops.append(d)
    print(compute_min_refills(d, m, stops))