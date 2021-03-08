# Finding Missing Number 

# by using the formula for the sum of n series 
# 1+2+3+4+.....+n=n(n+1)/2


# from array import *
# arr=array("i",[1,5,7,9,10])

# Number of element should be in array =10 so n=10
# Sum of the element in the array is 10(10+1)/2=55
# And all the values should be unique 


# rangeOfNumbers=int(input("Enter the last number to find the missing in between: "))
# if rangeOfNumbers!=arr[-1]:
#     arr.append(rangeOfNumbers)
# print(arr)

# li=[]
# a=0
# for i in range(1,rangeOfNumbers+1):
#     if (i*(i+1))/2!=(arr[a]*(arr[a]+1))/2:
#         li.append(i)
#     else:
#         a=a+1

# print(li)

# Time complexity of O(n)





# Problem statement 2

# Given an array of integers nums and an integer target
# such that they add upto target
# You may assume that each input would hav exactly one solution 
# And you may not use the same element twice
# You can return the answer in any order



# def FindingPairs(nums,target):
#     li=[]
#     a=0
#     for i in range(0,len(nums)-1):
#         if len(nums)<=2:
#             return []
#         if nums[a]==nums[i+1]:
#             continue
#         elif nums[a]+nums[i+1]==target:
#             li.append([nums[a],nums[i+1]])
#             print(nums[a],nums[i+1])
        
            

#     return li+FindingPairs(nums[1:],target)
            
# a=FindingPairs([2,4,6,2,3,1,5,7,8,1],8)
# # print(a)
# # [[2, 6], [6, 2], [3, 5], [1, 7], [7, 1]]

# b=0
# # li1=a
# for i in range(len(a)-1):
#     if a[b][:]==a[b+1][::-1]:
#         print(a[b],a[b+1])
#     b=b+1




# Problem statement 
# 3-Finding a number in an array 

# import numpy as np

# arr=np.array([2,3,4,5])

# def FindingElement(array,num):
#     for i in array:
#         if i==num:
#             return "The number present in the array at index: ",np.where(array==num)
    
#     return "The number is not present of the array"

# print(FindingElement(arr,3))
# li=[]
# a=int(input("Write the number you want to find: "))
# for i in range(len(arr)):
#     if arr[i]==a:
#         li.append(i)
# if len(li)==0:
#     print("The number is not present on the array")
# else:
#     print("The number present at these indexes in an array: ",li)

# def FindNumber(array,num):
#     for i in range(len(array)):
#         if array[i]==num:
#             print(i)
# FindNumber(arr,3)






# Problem statement 4
# How to find maximum product of two integers in the 
# array where all elements are positive
# arr=np.array([1,2,3,4,5,3,7,8,3,10])
# arr=np.array([2,3,4,5])
# global max
# def FindMaxProduct(array):
#     a=0
#     for i in range(len(array)-2):
#         if len(array)<=2:
#             return array[a]*array[a+1]
#         b=array[a]*array[i+1]
#         if b<(array[a]*array[i+2]):
#             max=(array[a]*array[i+2])
#             if max>global max:
#                 global max=max
#         continue
#     return max,FindMaxProduct(array[1:len(array)])

# print(FindMaxProduct(arr))


# def findmaxproduct(array):
#     maxproduct=0
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i]*array[j]>maxproduct:
#                 maxproduct=array[i]*array[j]
#                 pairs=str(array[i])+","+str(array[j])

#     print(pairs)
#     print(maxproduct)

# findmaxproduct(arr)


# problem Number 5
# Is Unique Implement an algorithm to determine if a 
# list has all the unique characters, using python list

# My code with quadratic complexity
# print("Is the provided list have all unique elements? ")
# mylist=[1,2,3,4,1,5,7,8,10,8]
# li=[]
# for i in range(len(mylist)):
#     for j in range(i+1,len(mylist)):
#         if mylist[i]==mylist[j]:
#             # print(f"{mylist[i]} is present multiple time in the list")
#             li.append(mylist[i])
# if len(li)==0:
#     print(True,",List have all unique characters")
# else:
#     print(False,",These values are repeated in the list: ",li)
     


# option 2 


# def isUnique(list):
#     a=[]
#     for i in list:
#         if i in a:
#             print(i)
#             return False
#         else:
#             a.append(i)
#     return True

# print(isUnique(mylist))



# problem Statement 6

# Permutation
# l1=[1,2,3,4]
# l2=[3,4,1]
# #  We need to find wether these list have same elements 

# for i in l1:
#     if i in l2:
#         continue
#     else:
#         print("The list doesnt have same elements")



# Problem statement 7
# rotate matrix/image

import numpy as np 

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])





def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

# matrix = [[1,2], [3,4]]
print(matrix)
print(rotate_matrix(matrix))




















