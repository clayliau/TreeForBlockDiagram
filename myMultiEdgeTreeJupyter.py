#%%
from MultiEdgeTreeList import *
myTree = Node(1)
myTree.addNewChild(2)
myTree.addNewChild(3)
myTree.addNewChild(4)
treePtr = myTree.children[0]
treePtr.addNewChild(5)
treePtr = myTree.children[1]
treePtr.addNewChild(6)
treePtr.addNewChild(7)
treePtr.addNewChild(8)
treePtr = treePtr.children[2]
parentPtr = myTree.children[2]
treePtr.addParent(parentPtr)
#treePtr = myTree.children[1]
#treePtr.insertNode(9)
#%%
treePtr = treePtr.parents[1]

#%%
childPtr = treePtr.children[0]
#%%
treePtr.addChild(childPtr)

#%%
for child in myTree.children[1].children[0].children:
    print(child.value)

#%%
myTree.children[1].children[0].children[2].parents[1].parents[0].children[1].value

#%%
