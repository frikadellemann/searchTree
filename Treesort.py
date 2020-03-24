import DictBinTree

import sys
T = DictBinTree.DictBinTree()

for line in sys.stdin:
    if line == "\n":
        break
    T.insert(int(line))

for i in T.orderedTraversal():
    print(i)
