#Knapsack problem: to maximise the value in a bag
#Input: The first line of the input contains the number𝑛of items and the capacity𝑊of a knapsack.The next𝑛lines define the values and weights of the items. The𝑖-th line contains integers𝑣𝑖and𝑤𝑖—thevalue and the weight of𝑖-th item, respectively
#Constraints: 1≤𝑛≤103,0≤𝑊≤2·106;0≤𝑣𝑖≤2·106,0< 𝑤𝑖≤2·106for all1≤𝑖≤𝑛. All thenumbers are integers

#Safe move: Use maximum amount of items with highest value per unit

#Code starts

def valueCalcu(lst):
    perUnitVal = list()
    i = 0
    for item in lst:
        perUnitVal.append([item[0]/item[1], i])
        i = i + 1
    perUnitVal = sorted(perUnitVal, reverse = True)
    return perUnitVal

def knapsack(w, lst):
    opt_val = 0
    perUnitVal = valueCalcu(lst)
    for item in perUnitVal:
        i = item[1]
        if (w <= lst[i][1]):
            opt_val = opt_val + item[0] * w
            break
        else:
            opt_val = opt_val + lst[i][0]
            w = w - lst[i][1]
    return opt_val

if __name__ == "__main__":
    (n, w) = map(int, input().split())
    lst = list()
    for i in range(n):
        lst.append(list(map(int, input().split())))
    opt_val = knapsack(w, lst)
    print(f"{opt_val:.10f}")