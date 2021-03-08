# Update or add element to the dictionary


mydict={"name":"Amaan","age":21}

mydict["age"]=27

mydict["address"]="mumbai"
print(mydict)



# Treversing through a dictionary


def traverse(dict):
    for key in dict:
        print(key,dict[key])



traverse(mydict)


# Search for any value in dictionary 

def searchdict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value

    else:
        return "The value doesnt exists"

print(searchdict(mydict,27))



# Time complexity is O(1) in average case
# Worst case is Amortized O(n)


# Delete an element in dictionary 

# pop(key)

mydict.pop("name")

# popitem()

mydict.popitem()
# Select a random pair and delete it 

# clear 
# Delete all pairs from dictionary 


mydict.clear()


# del(key) 
mydict={"name":"Amaan","age":21}
# del mydict("age")

dict =mydict.copy()



# from keys method(sequence,value(optional))

newdict={}.fromkeys([1,2,3],0)


print(newdict)

# get(key,value)

# if key present in the dictionary it will return the
# value associated with it 

# if the key is not present on dictionary it will
# return the value provided by default 

# if you pass only key and it is not present on the
# dictionary then it will return None

print(mydict.get("city","AZ"))

# items()

# it return key value tuple pair

print(mydict.items())
for key,value in mydict.items():
    print(key,value)



# keys()
print(mydict.keys())


# setdefault(key,default_value)

# if the key is present it will return the value 

# if the key is absent than it will add the key value pair




print(mydict.setdefault("name1"))


# values()
# return the list of values

print(mydict.values())



# update(other_dictionary or keypair value generally tuple)

newdict1={"A":1,"B":2,"C":3}

mydict.update(newdict1)

print(mydict)






# Dictionary operations and functions


# in operator
# befault only check keys 
# time complexity is O(1) because of hash function 
print("name" in mydict)
# if values
print("amaan" in mydict.values())

# built in function

# all(dictionary)
# return true and false


# any(dictionary )
# it is opposite of all()

# len()
# return number of pairs




# sorted(iterable,reverse,,key)

print(sorted(mydict))

































