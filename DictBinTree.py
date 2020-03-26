import BinNode

class DictBinTree(object):

    #initialize root for new DictBinTree object
    # all values are set to None from start
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    #Search for k in tree T, and returns in boolean whether k is found
    #This method assumes that the tree is ordered   
    #This is a starter method, which starts in the root and continues via the _search method from BinNode
    def search(T,k):

        if T.val == k:
            return True
        if T.left != None and k < T.val :
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)
        return False
        
    #Go trough tree T and add the elements to array in rising order. returns the array
    #This is a starter method, which initializes the array and passes it to the _orderedTraversal method from BinNode
    def orderedTraversal(T):
        A = []
        if T.left != None and T.left.val != None:
            T.left._orderedTraversal(A)
        if T.val != None:
            A.append(T.val)
        if T.right != None and T.right.val != None:
            T.right._orderedTraversal(A)
        return A

    #The only non-recursive function
    #Inserts new element k in tree T according to 'ordered tree logic'
    def insert(T,k):
        y = None
        x = T
        while x != None and x.val != None:
            y = x
            if k < x.val:
                x = x.left
            else:
                x = x.right
        if y == None:
            T.val = k
        elif k < y.val:
            y.left = BinNode.BinNode(k)
        else:
            y.right = BinNode.BinNode(k)
            

