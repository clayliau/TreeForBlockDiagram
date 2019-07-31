# Introduction
This project is for creating tree like block diagram which is not only for visualization but also creates an object for advance application.

# Prerequisite
* Python 3.7 (I use this version)
* Graphviz application. https://www.graphviz.org/

# Example
## Node Class
* Create a node from Node class:
  ```python
  myNode = Node(value, id, dataObj)
  ```
## Block Diagram Class
* Create a block diagram from BlockDiagram class:
  ```python
  myTree = BlockDiagram() # Create BlockDiagram object
  myTree.newBlock(valueForRootNode) # Create New Block Diagram with initial node which assigns Node.value = value
  ```
* Add new child node for current node:
  ```python
  myTree.addNewChildNode(valueForChildNode)
  ```
* Move BlockDiagram.currNodePtr to target node:
  1. Move to child node from BlockDiagram.currNodePtr:
  ```python
  myTree.go2Child(childNodeIndex) # BlockDiagram.currNodePtr moves to the child node base on input of Node.children lis index
  ```
  2. Move to parent node from BlockDiagram.currNodePtr:
  ```python
  myTree.go2Parent(parentNodeIndex) # BlockDiagram.currNodePtr moves to the parent node base on input of Node.parents lis index
  ```
  3. Move to arbitrary node from BlockDiagram.currNodePtr by assigning node id: 
  ```python
  myTree.go2NodeID(targetNodeID) # BlockDiagram.currNodePtr moves to the node base on input node id
  ```
 * Show block diagram by text description:
   ```python
   print(myTree.showBlockDiagramDes())
   ```
 * Show block diagram in PDF:
   ```python
   myTree.showBlockDiagram()
   ```
