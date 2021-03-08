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

# def isPalindrome(word):
#     return word==word[::-1]

# string syntax == string[start:end:step]

# print(isPalindrome("tacocat"))


# Some recursive

# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True
        
# def someRecursive(arr, cb):
#     return 

# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     return True
 
# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True




# print(someRecursive([8,2,6],isOdd))

# Flatten 

# def flatten(arr):
#     return 





# flatten([1,2,3,[4,5]])





# for element in l:
#     if type(element) is list:
#         # print(element)
#         for item in element:
#             flatten_list.append(item)
#     else:
#         flatten_list.append(element)
#         print(flatten_list)

# print(flatten_list)




# def flatten(arr):
#     flat_list=[]
#     for i in arr:
#         if type(i)==list:
#             flat_list.extend(flatten(i))
#         else:
#             flat_list.append(i)
#     return flat_list

# print(flatten([[1,2,3],5,6,[7,8,9]]))


# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 
  
# # output list 
# output = [] 
  
# # function used for removing nested  
# # lists in python.  
# def reemovNestings(l): 
#     for i in l: 
#         if type(i) == list: 
#             reemovNestings(i) 
#         else: 
#             output.append(i) 
  
# # Driver code 
# print ('The original list: ', l) 
# reemovNestings(l) 
# print ('The list after removing nesting: ', output) 




# def capitalizeFirst(arr):
#     capitalize_list=[]
#     print(capitalize_list)
#     if len(arr)==0:
#         return capitalize_list
#     else:
#         capitalize_list.append(arr[0].capitalize())
#         return capitalize_list+(capitalizeFirst(arr[1:]))
            
    



# print(capitalizeFirst(["car","taco","banana","apple"]))



# Capitalize Words

# def capitalizeWords(arr):
#     capitalize_list=[]
#     if len(arr)==0:
#         return capitalize_list
#     else:
#         capitalize_list.append(arr[0].upper())
#         return capitalize_list+(capitalizeWords(arr[1:]))

# print(capitalizeWords(["i","am","learning","recursion"]))



# nested even sum



obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


# def nestedEvenSum(obj, sum=0):
# to iterate all the values
# for value in obj1.values():
    # print(value)

# to iterate through key,value pairs
# for key,value in obj1.items():
#     print(key,":",value)

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}


# def nestedEvenSum(obj,sum=0):
#     for value in obj.values():
#         if type(value) is dict:
#             sum=sum+nestedEvenSum(value)
#             print(sum)
#         elif type(value) is int and value%2==0:
#             sum=sum+value
#             # print(sum)
#     return sum

# print(nestedEvenSum(obj1))


# stringify Numbers

# obj={"num":1,
#     "test":[],
#     "data":{
#         "val":4,
#         "info":{
#             "isRight":True,
#             "random":66
#         }
#     }
# }


# def stringifyNumbers(obj):
#     new_Dict=obj
#     for value in new_Dict.values():
#         if type(value) is int:
#             value=str(value)
            
#         if type(value) is dict:
#             value=stringifyNumbers(value)
#     return new_Dict


# print(stringifyNumbers(obj))



# def stringifyNumbers(obj):
#     newObj = obj
#     for key in newObj:
#         if type(newObj[key]) is int:
#             newObj[key] = str(newObj[key])
#         if type(newObj[key]) is dict:
#             newObj[key] = stringifyNumbers(newObj[key])
#     return newObj

# print(stringifyNumbers(obj))


# Find max number using recursion

# def maxnum(sampleArray,n):
#   if n==1:
#     return sampleArray[0]
#   return max(sampleArray[n-1],maxnum(sampleArray,n-1))

# print(maxnum([3,6,1,9],4))



# Collect string

obj={
  "stuff":"foo",
  "data":{
    "val":{
      "thing":{
        "info":"bar",
        "moreInfo":{
          "evenMoreInfo":{
            "weMadeIt":"baz"
          }
        }
      }
    }
  }
}



def collectStrings(obj):
    collect_string=[]
    for value in obj.values():
      if type(value) is str:
        collect_string.append(value)
      if type(value) is dict: 
        return collect_string+collectStrings(value)
    return collect_string

print(collectStrings(obj))














