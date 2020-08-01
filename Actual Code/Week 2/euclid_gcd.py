#To find the GCD of two numbers using the Euclidean algorithm

#Euclidean algorithm: GCD (a, b) = GCD(a%b, b)
#There is an extended version of the Euclidean algorithm which is used in cryptography such as RSA public key encryption method

# Function to return gcd of a and b 
def gcd(a, b):  
    if a == 0 : 
        return b  
      
    return gcd(b%a, a)

#Main function:
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))