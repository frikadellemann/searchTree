#/ Emil Blarke eblar19
#/ Mads Frederik Larsen madla15
class BinNode(object):
    #Initialize a new node
    def __init__(self, k):
        self.val = k
        self.left = None
        self.right = None

    #'Helper method' which does exactly the same as search from DictBinTree but for BinNode objects
    def _search(T,k):
        if T.val == k:
            return True
        if k < T.val and T.left != None:
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)
        return False

    
    #'Helper method' which does the same as orderedTraversal from DictBinTree but for BinNode objects
    #It gets the array from orderedTraversal and builds it from the rest of the nodes
    def _orderedTraversal(T,A):
        if T.left != None and T.left.val != None:
            T.left._orderedTraversal(A)
        A.append(T.val)
        if T.right != None and T.right.val != None:
            T.right._orderedTraversal(A)
        return A
