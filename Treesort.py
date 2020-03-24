import DictBinTree

import sys
T = DictBinTree.DictBinTree()

for line in sys.stdin:
    T.insert(int(line))

for i in T.orderedTraversal():
    print(i)
