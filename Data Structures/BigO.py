# Finding complexities of interview questions

# Product and Sum

# def foo(array):
#     sum=0
#     product=1

#     for i in array:
#         sum=sum+i
#     for i in array:
#         product=product*i
    
#     print("Sum ="+str(sum)+", Product ="+str(product))

# foo([1,2,3,4])


# Print Pairs

# def Printpairs(array):
#     for i in array:
#         for j in array:
#             print(str(i)+","+str(j))
# Printpairs([1,2,3,4])



# Print unordered Pairs


# def PUP(array):
#     for i in range(0,len(array)):
#         for j in range(i+1,len(array)):
#             print(str(array[i])+","+str(array[j]))

# PUP([1,2,3,4])



# def reverse(array):
#     for i in range(0,int(len(array)/2)):
#         other=len(array)-i-1
#         temp=array[i]
#         array[i]=array[other]
#         array[other]=temp
#     print(array)

# reverse([1,2,3,4])



# Power of 2

# def powersof2(n):
#     if n<1:
#         return 0
#     elif n==1:
#         print(1)
#         return 1
#     else:
#         prev=powersof2(int(n/2))
#         curr=prev*2
#         print(curr)
#         return curr

# powersof2(40)

