class BinNode(object):
    def __init__(self, k):
        self.val = k
        self.left = None
        self.right = None
    

    def _orderedTraversal(T,A):
        if T.left != None and T.left.val != None:
            T.left._orderedTraversal(A)
        A.append(T.val)
        if T.right != None and T.right.val != None:
            T.right._orderedTraversal(A)
        return A
    def _search(T,k):

        if T.val == k:
            return True
        if k < T.val and T.left != None:
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)
        return False
