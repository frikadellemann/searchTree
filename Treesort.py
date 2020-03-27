#/ Emil Blarke eblar19
#/ Mads Frederik Larsen madla15
import DictBinTree
import sys

T = DictBinTree.DictBinTree(None)
for line in sys.stdin:
    T.insert(int(line))

for i in T.orderedTraversal():
    print(i)
