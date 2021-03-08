# Common operations on Trie

# -Creation of Trie
# -Insertion in Trie 
# -Search for a string in Trie
# -Deletion from Trie


class TrieNode:
    def __init__(self):
        self.children={}
        self.endofString=False 

class Trie:
    def __init__(self):
        self.root=TrieNode()





# insertion

# -Case1: A trie is Blank
# -Case2: New strings prefix is common to another strings prefix
# -Case3: New strings prefix is already present as complete string
# -Case4: String to be inserted is already present in Trie

    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endofString=True
        # print("Successfully inserted")

# O(m),O(m) where m is the length of the word



# Search
# -Case 1: String doesnt exists in Trie
# -Case 2: String exists in Trie
# -Case 3: String is a prefix of another string, but it doesnt exists in a trie

    def searchString(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node==None:
                return False
            currentNode=node
        if currentNode.endofString==True:
            return True
        else:
            return False
# O(m),O(1)


# Deletion 
# -Case 1: Some other prefix of string is same as the one 
# that we want to delete

# -Case 2: The string is a prefix of another string(API,APIS)

# -Case 3: Other string is a prefix of this string(APIS,AP)

# -Case 4: Not any node depends on this string
    
def deleteString(root,word,index):
    ch=word[index]
    currentNode=root.children.get(ch)
    canThisNodeBeDeleted =False

    if len(currentNode.children)>1:
        deleteString(currentNode,word,index+1)
        return False
    if index==len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.endofString=False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endofString==True:
        deleteString(current,word,index+1)
        return False

    canThisNodeBeDeleted=deleteString(currentNode,word,index+1)
    if canThisNodeBeDeleted==True:
        root.children.pop(ch)
        return True
    else:
        return False






newTrie=Trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
newTrie.insertString("BAR")
newTrie.insertString("CAT")
newTrie.insertString("DOG")
deleteString(newTrie.root,"BAR",0)
print(newTrie.searchString("BAR"))

