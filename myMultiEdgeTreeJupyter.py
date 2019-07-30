#%%
from MultiEdgeTreeList import *
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'
myTree = BlockDiagram()
myTree.newBlock('0')
myTree.addNewChildNode('1')
myTree.addNewChildNode('2')
myTree.addNewChildNode('3')
myTree.go2Child(0)
myTree.addNewChildNode('4')
myTree.addNewChildNode('5')
myTree.go2Parent(0)
myTree.go2Child(1)
myTree.addNewChildNode('6')
myTree.addNewChildNode('7')
myTree.addNewChildNode('8')
myTree.go2Child(1)
myTree.addExistedParentNodeByID(1)
myTree.go2NodeID(3)
myTree.addExistedChildNodeByID(8)
#myTree.showBlockDiagram()

#%%
print(myTree.showBlockDiagramDes())


#%%
myTree.showBlockDiagram()

#%%
myTree.__doc__

#%%
