#To find the minimum number of coins required 
#Given coins: 10, 5, 1

#Safe move: Use maximum number of largest domination

total = int(input()) #Total amount
coins = [10, 5, 1] #Given domination
noc = 0 #Number of coins

for n in coins:
    noc = noc + (total // n) #No. of coins of current domination
    total = total % n
    if (total == 0): #Terminate if total becomes 0
        break

print(noc) #Printing total number of coins