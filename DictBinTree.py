import sys
import BinNode

class DictBinTree(object):

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

        
    def search(T,k):

        if T.val == k:
            return True
        if T.left != None and k < T.val :
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)
        return False
        

    def orderedTraversal(T):
        A = []
        if T.left != None and T.left.val != None:
            T.left._orderedTraversal(A)
        if T.val != None:
            A.append(T.val)
        if T.right != None and T.right.val != None:
            T.right._orderedTraversal(A)
        return A


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
            y.left = BinNode(k)
        else:
            y.right = BinNode(k)
            

