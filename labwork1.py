class Tree:
    def __init__(self, score):
        self.score = score
        self.l = self.r = None
        
#minimum element 
def minimum(tree):
    
    if tree.l == None:
        return tree.score
    return minimum(tree.l)
    
#maximum element
def maximum(tree):
    
    if tree.r == None:
        return tree.score
    return maximum(tree.r)

#adding student
def insert(tree, new):
    while True:
        if new.score > tree.score:
            if tree.r:
                tree = tree.r
            else:
                tree.r = new
                break
        else:
            if tree.l:
                tree = tree.l
            else:
                tree.l = new
                break

#searching for student
def search(tree, n):
    if tree == None or n == tree.score:
        return tree
    if n < tree.score:
        return search(tree.l, n)
    else:
        return search(tree.r, n)

#deleting tree
def delete(tree):
    if tree == None:
        return
    delete(tree.l)
    delete(tree.r)
    tree.l = tree.r = None
    __delete_root__(tree)

# printing
def print_all(tree, space):   
    if (tree == None) : 
        return   
    space += 10
    print_all(tree.r, space)   
 
    for i in range(10, space): 
        print(end = " ")  
    print(tree.score)  
   
    print_all(tree.l, space)     
def __delete_root__(tree):
    del tree

t = Tree(6)
insert(t, Tree(7))
insert(t, Tree(5))
insert(t, Tree(5.5))
insert(t, Tree(6.5))
insert(t, Tree(4))
insert(t, Tree(8))
print_all(t, 0)