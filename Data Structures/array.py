# from array import *
import numpy as np
# # arr1=array("i",[1,2,3,4])
# # print(type(arr1))


# # Insert elements in array
# # arr1.insert(3,5)

# # print(arr1)


# # Finding element in array

# # def searchInArray(array,value):
# #     for i in array:
# #         if i==value:
# #             return array.index(value)
# #     return "The element is not present in array"

# # print(searchInArray(arr1,7))


# # Remove element from array

# # arr1.remove(1)
# # print(arr1)

# # Create and array and traverse

# my_array= array("i",[1,2,3,4,5,6,7,8])
# # for i in my_array:
#     # print(i)


# # Access individual elements through index

# # print(my_array[3])


# # Append any value to the array using append() method 

# my_array.append(9)
# print(my_array)


# # Insert value in an array using insert() method

# my_array.insert(len(my_array),10)
# print(my_array)

# # Extend python array by using extend() method

# my_array1=array("i",[11,12,13])

# my_array.extend(my_array1)
# print(my_array)


# # Add item from list into array using fromlist() method

# my_list=[14,14,15,16,16]
# my_array.fromlist(my_list)
# print(my_array)


# # Remove any element form array using remove() method

# my_array.remove(15)
# print(my_array)

# # Remove last element by using pop method

# my_array.pop()
# print(my_array)

# # Fetch any element by using index() method

# print(my_array.index(14))


# # Reverse a python array using reverse() method 

# my_array.reverse() #the change is in place and id is same so we use print to get the reverse array
# print(my_array)


# # Get a buffer information through buffer_info() method

# print(my_array.buffer_info())

# # Check for number of occurance of an element using count() method

# print(my_array.count(14))

# # Convert array to string using tostring() method

# # strTemp=my_array.tostring()
# # print(strTemp)
# # for i in strTemp:
# #     print(type(i))
# # ints=array("i")
# # ints.fromstring(strTemp)
# # print(type(ints))
# # for i in ints:
#     # print(type(i))

# # Convert array to a python list with same elements using tolist() method 

# # print(type(my_array.tolist()))


# # Append a string to char array using fromstring() method 


# # Slice Elements from an array 

# # print(my_array[1:5])



# Two Dimensional Array 

twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(twoDarray)

# Insert rows or columns to two dimensional array 

# newTwoDarray=np.insert(twoDarray,1,[[8,7,6,5]],axis=0)

# print(newTwoDarray)


# Access element in two dimensional array 
# a[i][j] where i is row index and j is column index


# print(twoDarray[1][3]) #it will return 8


# def accessElement(array,rowindex,columnindex):
#     if rowindex>=len(array[1]) or columnindex>=len(array[0]):
#         print("Incorrect index")
#     else:
#         print(array[rowindex][columnindex])

# accessElement(twoDarray,4,4)



# Traversing of all elements in 2D array 

# for i in twoDarray:
#     for j in i:
#         print(j,end=" ")
#     print()



# Searching of element in the array 

# def searchingElement(array,value):
#     for i in array:
#         for j in i:
#             if j==value:
#                 # print("Value found",np.where(array==value))
#                 return "The value is loacted at index"+str(np.where(array==value))
#     return "The element is not found"
# print(searchingElement(twoDarray,7))




# Deletion of rows and columns in an array 

newTDArray=np.delete(twoDarray,0,axis=1)
print(newTDArray)




































