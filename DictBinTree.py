import BinNode
class DictBinTree:
    def DictBinTree():
        T = BinNode(None)

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
            T = k
        elif k < y.val:
            y.left = k
        else:
            y.right = k
DictBinTree().insert(10)

