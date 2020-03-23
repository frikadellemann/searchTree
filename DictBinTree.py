import sys
import array as arr

class BinNode:
    def __init__(self, k):
        self.val = k
        self.left = None
        self.right = None
    def val(self):
        return self.val

    def _orderedTraversal(T,A):
        if T.left != None:
            T.left._orderedTraversal(A)
        A.append(T.val)
        if T.right != None:
            T.right._orderedTraversal(A)
        return A

class DictBinTree:

    def __init__(self):
        self.val = None
        self.left = BinNode(None)
        self.right = BinNode(None)
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
        A.append(T.val)
        if T.right != None:
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
BinNode(10)
R = DictBinTree()
print(R.val)
for line in sys.stdin:
    if line == "\n":
        break
    R.insert(int(line.strip()))
print(R.orderedTraversal())
print(R.val)
print(R.left.val)
print(R.right.val)
print(R.right.right.val)
