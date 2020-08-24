#To find the largest number that can be made using the numbers given (need not be single digit)

#Safe move: Compare the digit starting from the highest place and place it in the highest position. 
#We create a function which checks which number is greater in terms of all places

def isGreater(n, maxDigit):
    nn = n
    mm = maxDigit
    while (len(n) != 0  and len(maxDigit) != 0): #Comparision digit by digit starting from MSB
        if (n[0] > maxDigit[0]):
            return True
        elif  (n[0] < maxDigit[0]):
            return False
        else:
            n = n[1:]
            maxDigit = maxDigit[1:]

    if (len(n) == 0 and len(maxDigit) == 0):
        return False
    elif (len(n) == 0): #When n is smaller than maxDigit, e.g 12, 121
        return isGreater(nn, maxDigit) #To check if n is greter than maxDigit trailing numbers 
    else: #When n is larger than maxDigit, e.g 129, 12
        return isGreater(n, mm) ##To check if maxDigit is smaller than trailing numbers of n

def calSalary(digits):
    maxNum = ""
    while (len(digits) != 0):
        localMax = None
        for digit in digits:
            if localMax is None:
                localMax = digit
            else:
                if (isGreater(digit, localMax)):
                    localMax = digit
        maxNum = maxNum + localMax
        digits.remove(localMax)
    return maxNum

#Main function
if __name__ == "__main__":
    n = input()
    digits = list(input().split()) #Numbers are operated as strings
    maxNum = calSalary(digits)
    print(int(maxNum))
