#%%
from MultiEdgeTreeList import *
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'
myTree = BlockDiagram()
myTree.newBlock('SDR865-LBTX')
myTree.addNewChildNode('LB-LPAMID')
myTree.go2Child(0)
myTree.addNewChildNode('LPF')
myTree.go2Child(0)
myTree.addNewChildNode('2P2T')
myTree.go2Child(0)
myTree.addNewChildNode('ANT0')
myTree.addNewChildNode('ANT1')
myTree.go2NodeID(4)
myTree.insertNewNode('TPX')
myTree.showBlockDiagram()

#%%
#%%
for node in myTree.getNodeList():
    nodeInfo = 'Node ID' + str(node.getID()) + ', Value ' + str(node.value)
    print(nodeInfo)
    print('    Children:')
    for i, child in enumerate(node.getChildrenList()):
         nodeInfo = '     - No' + str(i) + ' Child Node ID' + str(child.getID()) + ', Value ' + str(child.value)
         print(nodeInfo)
    print('    Parents:')
    for i, parent in enumerate(node.getParentsList()):
         nodeInfo = '     - No' + str(i) + ' Parent Node ID' + str(parent.getID()) + ', Value ' + str(parent.value)
         print(nodeInfo)

#%%
