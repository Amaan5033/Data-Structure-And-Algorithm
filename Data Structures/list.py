# update elements in the list 


mylist=['a','b','c','d','e','f','g','h','e']

# Update first two elements of the list 
print(mylist)
mylist[0:2]=["x","y"]
print(mylist)

# Delete methods in list
# pop(index) with time complexity of O(n) because element shifted 
# mylist.pop(1)

# delete() method slicing also works O(n) time complexity

# del mylist[1]


# remove method when you know the element O(n) time complexity 
# mylist.remove("e")



# Searching in the list 

# in operator O(n)

# if "f" in mylist:
#     print(mylist.index("f"))
# else:
#     print("The value is not present in the list")

# def searchlist(list,value):
#     count=0
#     for i in list:
#         if i==value:
#             count=count+1
#             print("The value is present on the list at the index"+" "+str(list.index(value)))
#     return "The occurance of the element in the list is"+" "+str(count)

# print(searchlist(mylist,"e"))





# Finding max number in a list 

l1=[2,5,8,2,4,6,4,9,10,3,17,3,7,1,0]

# def findMaxNum(list):
#     initial=0
#     for i in list:
#         if i>initial:
#             initial=i

#     return initial

# print(findMaxNum(l1))
        
# One liner to find max

# print(max(l1))




# Finding Average of list by taking input from user 


# l2=[]
# c=True
# while c:
#     a=input("Enter the numbers to find the average or type done to exit: ")
#     if a=="done":
#         print("The average of your inputs is",sum(l2)/len(l2))
#         c=False
#     else:
#         l2.append(int(a))


# a="My-name-is-amaan"
# b=a.split("-")
# print(b)
# print("".join(b))

    

# Drawbacks of list
# print(l1.sort())
# print(l1)

# l2=[[1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]]

# for i in range(0,4):
#     print(l2[i].pop())



# fl1=["Apple","Berry","Cherry","Papaya"]
# fl2=fl1
# fl3=fl1[:]

# fl2[0]="Guava"
# fl3[1]="Kiwi"

# sum=0
# for ls in (fl1,fl2,fl3):
#     # print(ls)
#     if ls[0]=="Guava":
#         sum=sum+1
#     if ls[1]=="Kiwi":
#         sum=sum+20

# print(sum)



# data = [[[1,2],[3,4]],[[5,6],[7,8]]]
# def fun(m):
#     v=m[0][0]
#     for row in m:
#         for element in row:
#             if v<element: v=element
#     return v

# print(fun(data[0]))


# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     return values

# f(1)
# f(2)
# f(3)


def f(value,values):
    v=1
    values[0]=44
t=3
v=[1,2,3]
f(t,v)
print(t,v[0])




