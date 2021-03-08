# def openRussiandoll(doll):
#     if doll==1:
#         print("All dolls are open")
#     else:
#         print(f"The opening number of doll is {doll}")
#         openRussiandoll(doll-1)
        
        
# doll=int(input("Enter the number of dolls"))
# openRussiandoll(doll)



# def firstmethod():
#     secondmethod()
#     print("I am the First method")

# def secondmethod():
#     thirdmethod()
#     print("I am the second method")

# def thirdmethod():
#     fourthmethod()
#     print("I am the third method")

# def fourthmethod():
#     print("I am the forth method")

# firstmethod()


# def recursivemethod(num):
#     if num<1:
#         print("num is less than 1")
#     else:
#         recursivemethod(num-1)
#         print(num)


# recursivemethod(4)

# def poweroftwo(num):
#     if num==0:
#         return 1
#     else:
#         power = poweroftwo(num-1)
#         return power*2


# print(poweroftwo(4))


# def poweroftwo(num):
#     i=0
#     power=1
#     while i< num:
#         power= power*2
#         i=i+1
#     return power

# print(poweroftwo(4))


# def factorial(num):
#     assert num>=0 and int(num)==num, "The number must be a positive integer"
#     if num in [0,1]:
#         return 1
#     else:
#         print(num)
#         return num*factorial(num-1)

# print(factorial(1.5))   



# def fibonacci(num):
#     assert num>=0 and int(num)==num,"The number must be a positive integer only!"
#     if num in [0,1]:
#         return num
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)

# print(fibonacci(9))




# def sumofnumber(num):
#     assert num>=0 and int(num)==num," Then the number must be an integer"
#     if num==0:
#         return 0
#     else:
#         return int(num%10)+sumofnumber(int(num/10))


# print(sumofnumber(float(input("Enter your number"))))



# def power(base, expo):
#     if expo==0:
#         return 1
#     else:
#         return base*power(base, expo-1)


# print(power(-1,4))




# By using Euclidean Algorithm and apply recursion
# def gcd(num,m):
#     assert int(num)==num and int(m)==m, "The number must be an integer"
#     if num<0:
#         num=-1*num
#     if m<0:
#         m=-1*m
#     if m==0:
#         return num
    
#     else:
#         return gcd(m,num%m)


# print(gcd(12.5,-30))



# Decimal to binary using recursion


# def binary(num):
#     assert int(num)==num, "The number must be an integer only"
#     if num==0:
#         return 0
#     else:
#         return num%2+10*binary(int(num/2))

# print(binary(13))


# PRoblems based on recursion

# power

# def power(base,exponent):
#     assert int(base)==base and int(exponent)== exponent,"The base and exponent must be positive integer"
#     if exponent<0:
#         exponent=-1*exponent
#     if exponent == 0:
#         return 1
#     else:
#         return base*power(base,exponent-1)

# print(power(10,-2))


# factorial


# def factorial(num):
#     assert int(num)==num and num>0,"The number must be a positive integer only"
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(6))


# product of array

# def productOfArray(arr):
    
#     return arr[i]*arr[i+1]



# productOfArray([1,2,3])

# by using iteration

# l=[1,2,3,4,5]
# result=1
# for i in l:
#     result=result*i

# print(result)

# by using recursion

# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     else:
#         return arr[0]*productOfArray(arr[1:])
# print(productOfArray([1,2,3,4]))



# recursive range


# def recursiveRange(num):
#     if num==1:
#         return 1
#     else:
#         return num+recursiveRange(num-1)

# print(recursiveRange(4))



# fibonacci sequence


# def fib(num):
#     if num==1:
#         return 1
#     if num==0:
#         return 0
#     else:    
#         return fib(num-1) + fib(num-2)
# print(fib(10))



# reverse of a string

# def reverse(strng):
#     if strng==strng[0]:
#         return strng[0]
#     else:
#         return reverse(strng[1:len(strng)])+strng[0] 

# print(reverse("python"))



# Palindrome

# def isPalindrome(strng):
#     if len(strng)<2: return True
#     if strng[0]!=strng[-1]: return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome("tacocat"))

# One line code for Palindrome

def isPalindrome(word):
    return word==word[::-1]

# string syntax == string[start:end:step]

print(isPalindrome("tacocat"))




























