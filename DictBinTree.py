import sys
import array as arr

class BinNode:
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
        if T.val == None:
            print(false)
            return False
        if k < T.val and T.left != None:
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)

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

        if T.val == k:
            return True
        if T.val == None:
            return False
        if T.left != None and k < T.val :
            return T.left._search(k)
        elif T.right != None:
            return T.right._search(k)
        

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
            
R = DictBinTree()
print(R.val)
for line in sys.stdin:
    if line == "\n":
        break
    R.insert(int(line.strip()))
print(R.orderedTraversal())
#print(R.val)
#print(R.left.val)
#print(R.right.val)
#print(R.right.right.val)
for line in sys.stdin:
    if line == "\n":
        break
    print(R.search(int(line.strip())))
