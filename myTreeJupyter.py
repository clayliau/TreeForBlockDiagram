#%%
from TreeList import *
myTree = BinaryTree()
myTree.newTree(1)
myTree.insertNode(2,LEFTNODE)
myTree.insertNode(3,RIGHTNODE)

#%%
myTree.go2LeftNode()


#%%
myTree.insertNode(4,LEFTNODE)
myTree.insertNode(5,RIGHTNODE)

#%%
myTree.go2ParentNode()


#%%
myTree.go2ParentNode()
myTree.go2RightNode()
myTree.insertNode(6,LEFTNODE)
myTree.insertNode(7,RIGHTNODE)
myTree.go2RootNode()


#%%
myTree.go2RootNode()
myTree.go2LeftNode()
print(myTree.currNodePtr.value)

#%%
myTree.currNodePtr.parent.value

#%%
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2LeftNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2LeftNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2ParentNode()
myTree.go2RightNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2RootNode()
myTree.go2RightNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2LeftNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)
myTree.go2ParentNode()
myTree.go2RightNode()
print(myTree.currNodePtr.value, myTree.currNodePtr.parent.value)


#%%
myTree.parentNodePtr.value

#%%
