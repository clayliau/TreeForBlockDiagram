from queue import Queue
from graphviz import Graph
class Node():
    def __init__(self, value, id):
        self.id = id
        self.isRootNode = False
        self.value = value
        self.parents = list()
        self.children = list()
    def addNewChild(self, value, id):
        newNode = Node(value, id)
        newNode.parents.append(self)
        self.children.append(newNode)
    def addNewParent(self, value, id):
        newNode = Node(value, id)
        newNode.children.append(self)
        self.parents.append(newNode)
    def insertNode(self, value, id):
        newNode = Node(value, id)
        # disconnect parents from original node and connect to new insert newNode
        for parent in self.parents:
            newNode.parents.append(parent)
            i = parent.children.index(self)
            parent.children[i] = newNode
        # Connect original node as a children of newNode
        newNode.children.append(self)
        # Reset original node's parents list and assign newNode as it's parent 
        self.parents = list()
        self.parents.append(newNode)
    def addExitedChild(self, childNode):
        if childNode in self.children:
            print('The child is already in it\'s children list.')
        else:
            self.children.append(childNode)
        if self in childNode.parents:
            print('It\'s already in the child\'s parents list')
        else:
            childNode.parents.append(self)
    def addExitedParent(self, newParent):
        if newParent in self.parents:
            print('The parent is already in it\'s parents list.')
        else:
            self.parents.append(newParent)
        if self in newParent.children:
            print('It\'s already in the parent\'s children list')
        else:
            newParent.children.append(self)
    def setAsRoot(self):
        self.isRootNode = True
    def setNotRoot(self):
        self.isRootNode = False
    def getID(self):
        return self.id
    def getChildrenList(self):
        return self.children
    def getParentsList(self):
        return self.parents
    def getValue(self):
        return self.value
    

class BlockDiagram():
    def __init__(self):
        self.rootNode = None
        self.currNodePtr = None
        self.tempNodePtr = None
        self.graph = None
        self.nodeIDCount = 0
    def newBlock(self, value):
        if self.rootNode == None:
            self.rootNode = Node(value, self.nodeIDCount)
            self.nodeIDCount += 1
            self.rootNode.setAsRoot()
            self.currNodePtr = self.rootNode
            self.parentNodePtr = self.rootNode
            self.graph = Graph(name='BlockDiagram', filename='BlockDiagram.gv', engine='dot')
            self.graph.node(name = self.currNodePtr.getID(), label = self.currNodePtr.getValue())
    def addNewChildNode(self, value):
        self.nodeIDCount += 1
        self.currNodePtr.addNewChild(value, self.nodeIDCount)
        self.tempNodePtr = self.currNodePtr.getChildrenList()[-1] # get the new children and assign to tempNodePtr
        print('add new node with ID %d to node ID %d' %(self.nodeID, currNodePtr.getID()))
        self.graph.node(name = self.tempNodePtr.getID(), label = self.tempNodePtr.getValue())
        self.graph.edge(self.currNodePtr.getID(), self.tempNodePtr.getID())
    def addNewParentNode(self, value):
        self.nodeIDCount += 1
        self.currNodePtr.addNewParent(value, self.nodeIDCount)
        self.tempNodePtr = self.currNodePtr.getParentsList()[-1] # get the new children and assign to tempNodePtr
        print('add new node with ID %d to node ID %d' %(self.nodeID, currNodePtr.getID()))
        self.graph.node(name = self.tempNodePtr.getID(), label = self.tempNodePtr.getValue())
        self.graph.edge(self.tempNodePtr.getID(), self.currNodePtr.getID())
    def addExistedParentNode(self, NewParentPtr):
        self.currNodePtr.addExitedParent(NewParentPtr)
        self.tempNodePtr = self.currNodePtr.getParentsList()[-1]
        self.graph.edge(self.tempNodePtr.getID(), self.currNodePtr.getID())
    def addExistedChildNode(self, NewChildPtr):
        self.currNodePtr.addExitedChild(NewChildPtr)
        self.tempNodePtr = self.currNodePtr.getChildrenList()[-1]
        self.graph.edge(self.currNodePtr.getID(), self.tempNodePtr.getID())
    '''    
    def getChildrenPosIDValueDict(self):
        returnDict = dict()
        if self.currNodePtr.getChildrenList():
            for i, child in enumerate(self.currNodePtr.getChildrenList()):
                returnDict.get(i, [child.id,child.value])
            return returnDict
        else:
            return returnDict
    '''
    '''        
    def go2Child(self, childPos):
        if self.currNodePtr.leftChild:
            print('move node to left node')
            self.parentNodePtr = self.currNodePtr
            self.currNodePtr = self.currNodePtr.leftChild
            print('from node value %d move to %d ' %(self.parentNodePtr.value, self.currNodePtr.value))
            print('new node parent value is %d' %(self.parentNodePtr.value))
            if not(self.currNodePtr.isRootNode) and (self.currNodePtr.parent==None):
                self.currNodePtr.assignParent(self.parentNodePtr)
                print('no parent in Node.parent')
                print('current node value: %d' %self.currNodePtr.value)
                print('parent node value: %d' %self.currNodePtr.parent.value)
        else:
            print('No left child node!')
    def go2RootNode(self):
        print('move node to root node')
        oriNode = self.currNodePtr
        self.currNodePtr = self.rootNode
        self.parentNodePtr = self.rootNode
        print('from node value %d move to %d ' %(oriNode.value, self.currNodePtr.value))
    def go2ParentNode(self):
        print('move node to parent node')
        tempPtr = self.parentNodePtr.parent
        oriNode = self.currNodePtr
        self.currNodePtr = self.parentNodePtr
        self.parentNodePtr = tempPtr
        print('from node value %d move to %d ' %(oriNode.value, self.currNodePtr.value))
    def bfs(self):
        queueTree = Queue()
        queueTree.put(self.rootNode)
        while not queueTree.empty():
            currentNode = queueTree.get()
            print(currentNode.value)
            if currentNode.leftChild:
                queueTree.put(currentNode.leftChild)
            if currentNode.rightChild:
                queueTree.put(currentNode.rightChild)
'''