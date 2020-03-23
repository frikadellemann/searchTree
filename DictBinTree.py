import BinNode:

class DictBinTree:
<<<<<<< Updated upstream
    def DictBinTree():
        T = BinNode(None)
# here we defince 
=======

    def __init__(self, N):
        self = N
        self.value = N.val
        print(self.value)

>>>>>>> Stashed changes
    def search(T,k):
        if T == None or T == k:
            return T
        if k < T.k:
            return T.left.search(k)
        else:
            return T.right.search(k)

    def orderedTraversal(T):
        A = []
        if T != None:
            T.left._orderedTraversal(A)
            A.append(T)
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
        while x != None:
            y = x
            if k < x.val:
                x = x.left
            else:
                x = x.right
        if y == None:
            T = BinNode(k)
        elif k < y.val:
            y.left = BinNode(k)
        else:
            y.right = BinNode(k)
N = BinNode(10)
T = DictBinTree(N)
T.insert(10)

N.left = BinNode(20)

print(N.left.val)
