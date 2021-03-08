# Creating a tuple in python 


mytuple=(1,2,3,4,5,6,7)

# Creating a tuple with single element 

mytuple1=(1,)

# Empty tuple creation 

mytuple2=tuple()

# How tuple treat string of characters 

mytuple3=tuple(("abcde"))

mytuple4=(8,9,10,11,12)

# tuple constructor 


print(mytuple)
print(mytuple1)
print(mytuple2)
print(mytuple3)



# Access tuple elements 

print(mytuple[1])

# slice operator 

# syntax tuple[leftindex:rightindex]

print(mytuple[0:3])



# Traversing a tuple 

# for i in mytuple:
#     print(i)




# Search an element in tuple 

# by using in operator

print(4 in mytuple)


def searchtuple(tuple,value):
    for i in tuple:
        if i==value:
            return tuple.index(i)

    return "The element does not exists"


print(searchtuple(mytuple,4))


# Tuple operations 


# concatenation of tuples 



print(mytuple+mytuple4)


#  *operator cannot be used by tuple but int

print(mytuple*4)




# cannot add or remove element


# count method 

print(mytuple.count(1))


# index method 


print(mytuple.index(4))


a=()
print(a.__len__())


a=1,2
b=(3,4)

# [print(sum(x)) for x in [a+b]]


# for x in [a+b]:
#     print(sum(x))



c=[(0,1),(1,2),(2,3)]

# result=sum(n for _,n in c)

# print(result)

for (i,k) in c:
    print(sum(k))





















