# Here we are practising multiple sorting algorithms 
import math #for bucket sort

# Bubble Sort
# Average time complexity is poor
# Space complexity is good so used Inplace
# My way
def BubbleSort1(list,j):
    if j==len(list):
        print(list)
    else:

        for i in range(len(list)-j):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
            else:
                continue
        BubbleSort(list[0:len(list)],j+1)

# O(n2),O(1)

# Instructor way
def BubbleSort2(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

    print(list)

# O(n2),O(1)
# BubbleSort2([3,5,1,2,8,4,7,6,9])




# Selection sort
# When we have insufficient memory
# Avoid when time is a concern
# My way
def SelectionSort(customList):
    for i in range(len(customList)):
        min=customList[i]
        min_index=i
        for j in range(i,len(customList)):
            if min>customList[j]:
                min=customList[j]
                min_index=j
        customList[i],customList[min_index]=customList[min_index],customList[i]    
    print(customList)
        
    
# Instructor Way 

def SelectionSort2(customList):
    for i in range(len(customList)):
        min_index=i
        for j in range(i+1,len(customList)):
            if customList[min_index]>customList[j]:
                min_index=j
        customList[i],customList[min_index]=customList[min_index],customList[i]
    print(customList)

# O(n2),O(1)

# SelectionSort([1,7,2,2,1])    



# Insertion Sort
# When we have insufficient memory
# When we have continuous inflow of numbers and we want to keep them sorted
# Avoid when time is a concern
# My way



# ---------This is not a good way because i m creating an extra space for list to store values----------#
def InsertionSort(customList):
    li=[]
    li.append(customList[0])
    for i in range(len(customList)-1):
        li.append(customList[i+1])
        insertion_index=-1
        for j in range(len(li)-1):
            if li[insertion_index]<li[insertion_index-1]:
                li[insertion_index],li[insertion_index-1]=li[insertion_index-1],li[insertion_index]
                insertion_index-=1
            else:
                break
    print(li)
# --------------------------------------------------------------------------------------------------------#

# Instructor way

def InsertionSort2(customList):
    for i in range(1,len(customList)):
        key=customList[i]
        j=i-1
        while j>=0 and key<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=key
    return customList
# InsertionSort2([3,5,1,2,8,4,1,7,6,3,9])

# O(n2),O(1)
# Bucket Sort 
# When input is Uniformly Distributed over Range for eg [1,2,4,5,3,7,8] not in [1,2,3,9,93,95]
# avoid when space is a concern



def BucketSort(customList):
    NumberOfBuckets=round(math.sqrt(len(customList)))
    maxValue=max(customList)
    arr=[]
    for i in range(NumberOfBuckets):
        arr.append([])
    for j in range(len(customList)):
        appropriate_bucket=math.ceil(customList[j]*NumberOfBuckets/maxValue)
        arr[appropriate_bucket-1].append(customList[j])
    for k in arr:
        k=InsertionSort2(k)
    k=0
    for i in range(NumberOfBuckets):
        for j in range(len(arr[i])):
            customList[k]=arr[i][j]
            k+=1
    return customList
# O(n2) if we use Insertion Sort but O(nlogn) if we use Quick Sort
# O(N)
# print(BucketSort([3,5,1,2,8,4,1,7,6,3,9]))



# Merge Sort
# When you need stable sort
# When average expected time is O(nlogn)
# Avoid when space is a concern

# Python inbuild method sort use tim sort which is 
# a hybrid of merge sort and insertion sort

def merge(customList,l,m,r):
    n1=m-l+1
    n2=r-m
    Left_array=[0]*(n1)
    Right_array=[0]*(n2)

    for i in range(0,n1):
        Left_array[i]=customList[l+i]
    for j in range(0,n2):
        Right_array[j]=customList[m+1+j]
    # Now we are merging the array
    i=0 #initial index of first sub array
    j=0 #initial index of second sub array
    k=l #initial index of merged sub arrays 
    while i<n1 and j<n2:
        if Left_array[i]<=Right_array[j]:
            customList[k]=Left_array[i]
            i+=1
        else:
            customList[k]=Right_array[j]
            j+=1
        k+=1
    while i<n1:
        customList[k]=Left_array[i]
        i+=1
        k+=1
    while j<n2:
        customList[k]=Right_array[j]
        j+=1
        k+=1

def MergeSort(customList,l,r):#l=leftindex, r=rightindex
    if l<r:
        m=(l+(r-1))//2
        MergeSort(customList,l,m)#-----T(N/2)
        MergeSort(customList,m+1,r)#-----T(N/2)
        merge(customList,l,m,r)

    return customList

# O(NLogN),O(N)
# print(MergeSort([3,4,1,2],0,3))




# Lets try something else:::

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_two_sorted_arrays(left,right)

def merge_two_sorted_arrays(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)

    i=j=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

# Here we take two sorted array and merge them 
# with the help of pointers

# if __name__=="__main__":
    # a=[5,8,12,56]
    # b=[7,9,45,51]
# Now we will go for our problem we define single customlist
# and try to break it in multiple arrays 
    # arr=[3,5,1,2,8,4,1,7,6,3,9]
    # print(merge_sort(arr))



# lets optimise our solution by using less space
# For that we will be removing all the return statements
# and unneccesary variables and sorted list

def merge_sort2(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort2(left)
    merge_sort2(right)

    merge_two_sorted_array2(left,right,arr)



def merge_two_sorted_array2(a,b,arr):
    

    i=j=k=0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1
    

# if __name__=="__main__":
#     arr=[3,5,1,2,8,4,1,7,6,3,9]
#     # merge_sort2(arr)
    # print(arr)


# lets have some few more test cases

# if __name__=="__main__":
#     tests_cases=[
#         [10,3,15,7,8,23,98,29],
#         [],
#         [3],
#         [9,8,7,2],
#         [1,2,3,4,5]
#     ]

#     for arr in tests_cases:
#         merge_sort2(arr)
#         print(arr)



# Exercise to practice

# https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise.md

# Quick Sort
# When expected time is O(NlogN)
# Avoid when space is a concern
# Avoid when you need a stable sort 

def partition(customList,low,high):
    i=low-1
    pivot=customList[high]
    for j in range(low,high):
        if customList[j]<=pivot:
            i+=1
            customList[i],customList[j]=customList[j],customList[i]
    customList[i+1],customList[high]=customList[high],customList[i+1]

    return (i+1)

def QuickSort(customList,low,high):
    if low<high:
        pi=partition(customList,low,high)
        QuickSort(customList,low,pi-1)
        QuickSort(customList,pi+1,high)
    return customList
# O(Nlogn),O(N)

print(QuickSort([2,1,7,6,5,3],0,5))

    

# Heap Sort 

def heapify(customList,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and customList[l]<customList[smallest]:
        smallest=l

    if r<n and customList[r]<customList[smallest]:
        smallest=r

    if smallest!=i:
        customList[i],customList[smallest]=customList[smallest],customList[i]
        heapify(customList,n,smallest)


def heapSort(customList):
    n=len(customList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)

    for i in range(n-1,0,-1):
        customList[i],customList[0]=customList[0],customList[i]
        heapify(customList,i,0)
    customList.reverse()

# customList=[2,1,7,6,5,3]

# print(heapSort(customList))

# print(customList)


# O(NlogN), O(1)





