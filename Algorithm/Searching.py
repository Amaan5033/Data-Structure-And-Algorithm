# Searching algorithm


# Linear search 
# Good for unsorted array

def linearSearch(customList,element):
    for i in range(len(customList)):
        if customList[i]==element:
            return i
    return -1

# print(linearSearch([1,2,3,4,5,6],5))
# O(n),O(1)


# Binary search faster than linear search 
# Works only with sorted array


# def BinarySearch(array,element):
#     if len(array)<=1:
#         return
#     if element==array[int(len(array)/2)]:
#          print("The element is found",element)
#     if element<array[int(len(array)/2)]:
#         BinarySearch(array[:int(len(array)/2)],element)
        
#     else:    
#         BinarySearch(array[int(len(array)/2):],element)

# # BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12],10)

# if __name__=="__main__":
#     test_cases=[1,2,3,4,5,6,7,8,9,10,11,12]
#     for j in test_cases:
#         BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12],j)
    
def BinarySearch(array,element):
    left_pointer=0
    right_pointer=len(array)-1
    middle=int((left_pointer+right_pointer)/2)
    while array[middle]!=element and left_pointer<=len(array):
        if array[middle]>element:
            right_pointer=middle#or we can use right_pointer=middle-1
        if array[middle]<element:
            left_pointer=middle#or we can use left_pointer=middle+1
        if left_pointer!=middle:#if we follow above two steps we dont need to write this step 
            middle=int((left_pointer+right_pointer)/2)
        else:
            middle=middle+1
    if array[middle]==element:
        return f"The index of {element} is {middle}"
    else:
        return -1


# Worst Case O(logn)
#Best Case O(1)
# print(BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12],12))


if __name__=="__main__":
    test_cases=[1,2,3,4,5,6,7,8,9,10,11,12]
    for j in test_cases:
        print(BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12],j))











