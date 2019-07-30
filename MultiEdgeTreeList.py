from queue import Queue
from graphviz import Graph, Source
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
    def getValue(self):
        return self.value
    def getChildrenList(self):
        return self.children
    def getParentsList(self):
        return self.parents
    def getValue(self):
        return self.value
    def delNode(self):
        if len(self.parents) < 1:
            print('Can\'t delete a node with no parent')
        else:
            print('Node ID %d is deleting' %self.id)
            for child in self.children:
                self.parents[0].append(child)
                print('Connect node ID %d to node ID %d' %(child.id,self.parents[0].id))
                print('Node ID %d is node ID %d\'s new child node' %(child.id,self.parents[0].id))
            print('Node ID %d is deleted' %self.id)

class BlockDiagram():
    def __init__(self):
        self.rootNode = None
        self.currNodePtr = None
        self.newNodePtr = None
        self.parentNodePtr = None
        self.graph = None
        self.nodeIDCount = 0
        self.nodeListPtr = list()
        self.edgeList = list()
        self.graphvizSource = ''
    def add2NodeListPtr(self, nodePtr):
        self.nodeListPtr.append(nodePtr)
    def newBlock(self, value):
        if self.rootNode == None:
            self.rootNode = Node(value, self.nodeIDCount)
            self.nodeIDCount += 1
            self.rootNode.setAsRoot()
            self.currNodePtr = self.rootNode
            self.parentNodePtr = self.rootNode
            self.add2NodeListPtr(self.rootNode)
            self.graph = Graph(name='BlockDiagram', filename='BlockDiagram.gv', engine='dot')
            self.graph.node(name = str(self.currNodePtr.getID()), label = str(self.currNodePtr.getValue()))
            print('Graph is created. The root node ID is %d' %self.currNodePtr.getID())
    def addGraphvizNode(self):
        #Always Create new node from newNodePtr
        ID = str(self.newNodePtr.getID())
        Value = str(self.newNodePtr.getValue())
        self.graph.node(name = ID, label = Value)
        print('Graphviz Node is created with Node ID %s and Value %s' %(ID, Value))
    def addGraphvizEdge(self, dir = 'new2curr'):
        # Create connection from newNodePtr --> currNodePtr
        if dir == 'new2curr':
            ID1 = str(self.newNodePtr.getID())
            ID2 = str(self.currNodePtr.getID())
            edge = ID1 + ' -- ' + ID2
            if edge in self.edgeList:
                print('Edge connection is existed')
            else:
                self.edgeList.append(edge)
                print('Graphviz edge is created between Node ID %s and ID %s' %(ID1, ID2))
        elif dir == 'curr2new':
            ID1 = str(self.currNodePtr.getID())
            ID2 = str(self.newNodePtr.getID())
            edge = ID1 + ' -- ' + ID2
            if edge in self.edgeList:
                print('Edge connection is existed')
            else:
                self.edgeList.append(edge)
                print('Graphviz edge is created between Node ID %s and ID %s' %(ID1, ID2))
        elif dir == 'insert':
            parents = self.newNodePtr.getParentsList()
            childrenID = str(self.currNodePtr.getID())
            insertID = str(self.newNodePtr.getID())
            for parent in parents:
                parentID = str(parent.getID())
                oriEdgeSyntax = parentID + ' -- ' + childrenID
                newEdgeSyntax = parentID + ' -- ' + insertID
                print(self.edgeList)
                print(oriEdgeSyntax)
                if oriEdgeSyntax in self.edgeList:
                    self.edgeList.remove(oriEdgeSyntax)
                self.edgeList.append(newEdgeSyntax)
                print('Graphviz edge is created between Node ID %s and ID %s' %(parentID, insertID))
            newEdgeSyntax = insertID + ' -- ' + childrenID
            self.edgeList.append(newEdgeSyntax)
            print('Graphviz edge is created between Node ID %s and ID %s' %(insertID, childrenID))
    def addNewChildNode(self, value):
        self.currNodePtr.addNewChild(value, self.nodeIDCount)
        self.newNodePtr = self.currNodePtr.getChildrenList()[-1] # get the new children and assign to newNodePtr
        self.add2NodeListPtr(self.newNodePtr)
        print('add new child node ID %d to node ID %d' %(self.nodeIDCount, self.currNodePtr.getID()))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'curr2new')
        self.nodeIDCount += 1
    def addNewParentNode(self, value):
        self.currNodePtr.addNewParent(value, self.nodeIDCount)
        self.newNodePtr = self.currNodePtr.getParentsList()[-1] # get the new children and assign to tempNodePtr
        self.add2NodeListPtr(self.newNodePtr)
        print('add new parent node ID %d to node ID %d' %(self.newNodePtr.getID(), self.currNodePtr.getID()))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'new2curr')
        self.nodeIDCount += 1
    def insertNewNode(self, value):
        self.currNodePtr.insertNode(value, self.nodeIDCount)
        self.newNodePtr = self.currNodePtr.getParentsList()[-1]
        self.add2NodeListPtr(self.newNodePtr)
        for parent in self.newNodePtr.getParentsList():
            parentID = parent.getID()
            print('Insert new node ID %d between node ID %d and parent ID %d' %(self.newNodePtr.getID(), self.currNodePtr.getID(), parentID))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'insert')
        self.nodeIDCount += 1
    def addExistedParentNode(self, NewParentPtr):
        self.currNodePtr.addExitedParent(NewParentPtr)
        self.newNodePtr = self.currNodePtr.getParentsList()[-1]
        self.addGraphvizEdge(dir = 'new2curr')
    def addExistedParentNodeByID(self, id):
        NewParentPtr = self.getNodeFromID(id)
        self.addExistedParentNode(NewParentPtr)
    def addExistedChildNode(self, NewChildPtr):
        self.currNodePtr.addExitedChild(NewChildPtr)
        self.newNodePtr = self.currNodePtr.getChildrenList()[-1]
        self.addGraphvizEdge(dir = 'curr2new')
    def addExistedChildNodeByID(self, id):
        NewChildPtr = self.getNodeFromID(id)
        self.addExistedChildNode(NewChildPtr)
    def go2Child(self, childPos):
        if childPos < len(self.currNodePtr.children):
            print('move to children No.%d' %childPos)
            oriID = self.currNodePtr.id
            self.currNodePtr = self.currNodePtr.children[childPos]
            print('from node ID %d move to Node ID %d ' %(oriID, self.currNodePtr.getID()))
        else:
            print('No No.%d child node!' %childPos)
    def go2Parent(self, parentPos):
        if parentPos < len(self.currNodePtr.parents):
            print('move to parent No.%d' %parentPos)
            oriID = self.currNodePtr.id
            self.currNodePtr = self.currNodePtr.parents[parentPos]
            print('from node ID %d move to Node ID %d ' %(oriID, self.currNodePtr.getID()))
        else:
            print('No No.%d child node!' %parentPos)
    def go2NodeID(self, id):
        if id < len(self.nodeListPtr):
            self.currNodePtr = self.nodeListPtr[id]
            print('Move to node ID %d' %self.currNodePtr.getID())
        else:
            print('Out of Range! Node id is not in the list.')
    def getNodeFromID(self, id):
        if id < len(self.nodeListPtr):
            return self.nodeListPtr[id]
        else:
            print('Out of Range! Node id is not in the list.')
    def getCurrChildrenList(self):
        return self.currNodePtr.getChildrenList()
    def getCurrParentsList(self):
        return self.currNodePtr.getParentsList()
    def showBlockDiagram(self, method = 'pdf'):
        #self.graph.edges(self.edgeList)
        self.graphvizSource = self.graph.source
        edges = '\t' +'\n\t'.join(self.edgeList) + '\n}'
        print(edges)
        self.graphvizSource = self.graphvizSource.replace('}', edges)
        print(self.graphvizSource)
        renderGraph = Source(self.graphvizSource, filename='BlockDiagram.gv', engine='dot')
        renderGraph.view()
    def getNodeList(self):
        return self.nodeListPtr
    def showBlockDiagramDes(self):
        desList = list()
        for node in self.getNodeList():
            nodeInfo = 'Node ID' + str(node.getID()) + ', Value ' + str(node.getValue())
            #print(nodeInfo)
            desList.append(nodeInfo)
            desList.append('    Children:')
            #print('    Children:')
            for i, child in enumerate(node.getChildrenList()):
                nodeInfo = '      ' + str(i) + '.' + ' Child Node ID' + str(child.getID()) + ', Value ' + str(child.getValue())
                #print(nodeInfo)
                desList.append(nodeInfo)
            desList.append('    Parents:')
            #print('    Parents:')
            for i, parent in enumerate(node.getParentsList()):
                nodeInfo = '      ' + str(i) + '.' + ' Parent Node ID' + str(parent.getID()) + ', Value ' + str(parent.getValue())
                #print(nodeInfo)
                desList.append(nodeInfo)
        return '\n'.join(desList)