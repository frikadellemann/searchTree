import sys


class BinNode:
    def __init__(self, k):
        self.val = k
        self.left = None
        self.right = None
    def val(self):
        return self.val

class DictBinTree:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
    def val(self):
        return self.val

    def val(T):
        return T.val
        
    def search(T,k):
        if T == None or T == k:
            return T
        if k < T.k:
            return T.left.search(k)
        else:
            return T.right.search(k)

    def orderedTraversal(T):
        A = []
        if T.left != None:
            T.left._orderedTraversal(A)
        A.append(T)
        if T.right != None:
            T.right._orderedTraversal(A)
        return A

    def _orderedTraversal(T,A):
        if T != None:
            T.left._orderedTraversal(A)
            A.append(T)
            T.right._orderedTraversal(A)

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
BinNode(10)
R = DictBinTree()
print(R.val)
R.insert(1)
print(R.orderedTraversal())
R.insert(2)
print(R.right.val)
