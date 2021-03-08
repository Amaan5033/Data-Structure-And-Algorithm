# mylist=[1,2,3,4]

# In this we have time complexity of O(n)

# def middle(list):
#     li=[]
#     for i in range(len(list)):
#         if i==0:
#             continue
#         if i==(len(list)-1):
#             continue
#         else:
#             li.append(list[i])

#     return li

# print(middle(mylist))

#In this we have time complexity of O(1) 

# def middle(list):
#     li=[]
#     li.append(list[1:len(list)-1])
#     for i in li:
#         return i
# print(middle(mylist))


# Problem 2nd 
# Find the sum of diagonal elements of 2D list

# mylist2D=[[1,2,3],[4,5,6],[7,8,9]]
# def sumDiagonal(a):
#     sum=0
#     b=0
#     for i in range(len(mylist2D)):
#         sum=sum+mylist2D[i][b]
#         b=b+1
#     return sum 
        
# print(sumDiagonal(mylist2D))


# Problem 3rd 

# Write a function to get first,second best scores from the list

# mylist=[84,85,86,87,85,90,85,83,90,23,45,90,84,1,2,0]

# def firstSecond(mylist):
#     mylist.sort(reverse=True)
#     for i in range(len(mylist)-1):
#         if mylist[i]!=mylist[i+1]:
#             return (mylist[i],mylist[i+1])
#         else: 
#             continue
# print(firstSecond(mylist))



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


# def missingNumber(mylist,totalCount):
#     li=[]
#     a=0
#     if totalCount not in mylist:
#         mylist.append(totalCount)
#     for i in range(1,totalCount+1):
#         if (i*(i+1))/2!=(mylist[a]*(mylist[a]+1))/2:
#             li.append(i)
#         else:
#             a=a+1
#     return li[0]
# print(missingNumber([1,2,3,4,6],6))




# problem 5
# Remove dublicates
# There is a bug in this program
def removeDuplicates(mylist):
    li=[]
    for i in range(len(mylist)):
        if mylist[i] not in li:
            li.append(mylist[i])
    return li
    
print(removeDuplicates([1,1,2,2,3,4,5]))


# problem6
# Write a function to find all pairs of an integer
# whose sum is equal to a given number 


# def pairSum(mylist,sum):
#     a=1
#     li=[]
#     for i in range(len(mylist)):
#         for j in range(a,len(mylist)):
#             if mylist[i]+mylist[j]==sum:    
#                 li.append(str(mylist[i])+"+"+str(mylist[j]))
#             else:
#                 continue
#         a=a+1
#     return li


# print(pairSum([2,4,3,5,6,-2,4,7,8,9],7))













