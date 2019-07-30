from queue import Queue
from graphviz import Graph, Source
class Node():
    def __init__(self, value, id, dataObj=None):
        '''
        ### Parameters Description
         * value: 
          * type: str, int
           * description: text for block diagram. Identifier for user to name the node 
         * id:
          * type: int
          * description: serial number for each node
         * dataObj: 
          * type: object
          * description: store object item in node for advanced application 
        '''
        self.id = id
        self.isRootNode = False
        self.value = value
        self.dataObj = None
        self.parents = list()
        self.children = list()
    def addNewChild(self, value, id, dataObj=None):
        '''
        ### Function Description
        Add new node as new child for current node. Storing it in children list.
        ### Parameters Description
         * value: 
          * type: str, int
          * description: text for block diagram. Identifier for user to name the node 
         * id:
          * type: int
          * description: serial number for each node
         * dataObj: 
          * type: object
          * description: store object item in node for advanced application 
        '''
        newNode = Node(value, id, dataObj)
        newNode.parents.append(self)
        self.children.append(newNode)
    def addNewParent(self, value, id, dataObj=None):
        '''
        ### Function Description
        Add new node as new parent for current node. Storing it in parents list.
        ### Parameters Description
         * value: 
          * type: str, int
          * description: text for block diagram. Identifier for user to name the node 
         * id:
          * type: int
          * description: serial number for each node
         * dataObj: 
          * type: object
          * description: store object item in node for advanced application 
        '''
        newNode = Node(value, id, dataObj)
        newNode.children.append(self)
        self.parents.append(newNode)
    def insertNode(self, value, id, dataObj=None):
        '''
        ### Function Description
        Insert new node as new parent for current node. It takes all parenets node from current node 
        and also add current node as child node.
        ### Parameters Description
         * value: 
          * type: str, int
          * description: text for block diagram. Identifier for user to name the node 
         * id:
          * type: int
          * description: serial number for each node
         * dataObj: 
          * type: object
          * description: store object item in node for advanced application 
        '''
        newNode = Node(value, id, dataObj)
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
        '''
        ### Function Description
        Add an exited node to children list.
        ### Parameters Description
         * childNode: 
          * type: object
          * description: target child node object. 
        '''
        if childNode in self.children:
            print('The child is already in it\'s children list.')
        else:
            self.children.append(childNode)
        if self in childNode.parents:
            print('It\'s already in the child\'s parents list')
        else:
            childNode.parents.append(self)
    def addExitedParent(self, ParentNode):
        '''
        ### Function Description
        Add an exited node to children list.
        ### Parameters Description
         * ParentNode: 
          * type: object
          * description: target parent node object.
        '''
        if ParentNode in self.parents:
            print('The parent is already in it\'s parents list.')
        else:
            self.parents.append(ParentNode)
        if self in ParentNode.children:
            print('It\'s already in the parent\'s children list')
        else:
            ParentNode.children.append(self)
    def delNode(self):
        '''
        ### Function Description
        Remove a node. Assign all it's children to it's parents[0].
        Note: If it doesn't has a parent, the operation would fail.
        '''
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
        '''
        ### Function Description
        Object initial
        ### Parameters Description
         * rootNode: 
          * type: object pointer
          * description: a pointer that points to root node of block diagram.
         * currNodePtr:
          * type: object pointer
          * description: a pointer that points to current working position.
         * newNodePtr:
          * type: object pointer
          * description: a pointer that points to new created node.
         * graph:
          * type: Graphviz graph object
          * description: create an object to visualize block diagram by using Graphviz
         * nodeIDCount:
          * type: int
          * description: internal counter for assigning serial to node.id
         * nodeListPtr:
          * type: list
          * description: storing all node pointer in a list.
         * edgeList:
          * type: list
          * description: storing the edge connections syntax for Graphviz visualization
         * graphvizSource:
          * type: str
          * description: Graphviz source code for rendering graph visualization 
        '''
        self.rootNode = None
        self.currNodePtr = None
        self.newNodePtr = None
        self.graph = None
        self.nodeIDCount = 0
        self.nodeListPtr = list()
        self.edgeList = list()
        self.graphvizSource = ''
    def add2NodeListPtr(self, nodePtr):
        '''
        ### Function Description
        Add node into nodeListPtr
        ### Parameters Description
         * nodePtr: 
          * type: object pointer
          * description: target node pointer
        '''
        self.nodeListPtr.append(nodePtr)
    def newBlock(self, value, dataObj=None):
        '''
        ### Function Description
        Create new block diagram. This is the main function to create a new block diagram object. 
        This module use Graph for visualiztion. There's no direction edge in this method.
        ### Parameters Description
         * value: 
          * type: str, int
          * description: text for block diagram. Identifier for user to name the node 
         * id:
          * type: int
          * description: serial number for each node
         * dataObj: 
          * type: object
          * description: store object item in node for advanced application 
        '''
        if self.rootNode == None:
            self.rootNode = Node(value, self.nodeIDCount, dataObj)
            self.nodeIDCount += 1
            self.rootNode.isRootNode = True
            self.currNodePtr = self.rootNode
            self.newNodePtr = self.rootNode
            self.add2NodeListPtr(self.rootNode)
            self.graph = Graph(name='BlockDiagram', filename='BlockDiagram.gv', engine='dot')
            self.addGraphvizNode()
            print('Graph is created. The root node ID is %d' %self.currNodePtr.id)
    def addGraphvizNode(self):
        '''
        ### Function Description
        Create new node. It create new node by self.newNodePtr
        '''
        ID = str(self.newNodePtr.id)
        Value = str(self.newNodePtr.value)
        self.graph.node(name = ID, label = Value)
        print('Graphviz Node is created with Node ID %s and Value %s' %(ID, Value))
    def addGraphvizEdge(self, dir = 'new2curr'):
        '''
        ### Function Description
        Make edge connection sytax and store in self.edgeList. There are three cases:
        ### Parameters Description
         * dir:
          * type: str
          * description: default is 'new2curr'. setting to determine the edge connection method.
          * options:
           1. new2curr: Create connection from newNodePtr --> currNodePtr
           2. curr2new: Create connection from currNodePtr --> newNodePtr
           3. insert: Special case for insert node. It would delete ogriginal parents connection then reconnect to insert node
        '''
        if dir == 'new2curr':
            # Create connection from newNodePtr --> currNodePtr
            ID1 = str(self.newNodePtr.id)
            ID2 = str(self.currNodePtr.id)
            edge = ID1 + ' -- ' + ID2
            if edge in self.edgeList:
                print('Edge connection is existed')
            else:
                self.edgeList.append(edge)
                print('Graphviz edge is created between Node ID %s and ID %s' %(ID1, ID2))
        elif dir == 'curr2new':
            # Create connection from currNodePtr --> newNodePtr
            ID1 = str(self.currNodePtr.id)
            ID2 = str(self.newNodePtr.id)
            edge = ID1 + ' -- ' + ID2
            if edge in self.edgeList:
                print('Edge connection is existed')
            else:
                self.edgeList.append(edge)
                print('Graphviz edge is created between Node ID %s and ID %s' %(ID1, ID2))
        elif dir == 'insert':
            # Special case for insert node. It would delete ogriginal parents connection then reconnect to insert node
            parents = self.newNodePtr.parents
            childrenID = str(self.currNodePtr.id)
            insertID = str(self.newNodePtr.id)
            for parent in parents:
                parentID = str(parent.id)
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
    def addNewChildNode(self, value, dataObj=None):
        self.currNodePtr.addNewChild(value, self.nodeIDCount, dataObj)
        self.newNodePtr = self.currNodePtr.children[-1] # get the new children and assign to newNodePtr
        self.add2NodeListPtr(self.newNodePtr)
        print('add new child node ID %d to node ID %d' %(self.nodeIDCount, self.currNodePtr.id))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'curr2new')
        self.nodeIDCount += 1
    def addNewParentNode(self, value, dataObj=None):
        self.currNodePtr.addNewParent(value, self.nodeIDCount, dataObj)
        self.newNodePtr = self.currNodePtr.parents[-1] # get the new children and assign to tempNodePtr
        self.add2NodeListPtr(self.newNodePtr)
        print('add new parent node ID %d to node ID %d' %(self.newNodePtr.id, self.currNodePtr.id))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'new2curr')
        self.nodeIDCount += 1
    def insertNewNode(self, value, dataObj=None):
        self.currNodePtr.insertNode(value, self.nodeIDCount, dataObj)
        self.newNodePtr = self.currNodePtr.parents[-1]
        self.add2NodeListPtr(self.newNodePtr)
        for parent in self.newNodePtr.parents:
            parentID = parent.id
            print('Insert new node ID %d between node ID %d and parent ID %d' %(self.newNodePtr.id, self.currNodePtr.id, parentID))
        self.addGraphvizNode()
        self.addGraphvizEdge(dir = 'insert')
        self.nodeIDCount += 1
    def addExistedParentNode(self, NewParentPtr):
        self.currNodePtr.addExitedParent(NewParentPtr)
        self.newNodePtr = self.currNodePtr.parents[-1]
        self.addGraphvizEdge(dir = 'new2curr')
    def addExistedParentNodeByID(self, id):
        NewParentPtr = self.getNodeFromID(id)
        self.addExistedParentNode(NewParentPtr)
    def addExistedChildNode(self, NewChildPtr):
        self.currNodePtr.addExitedChild(NewChildPtr)
        self.newNodePtr = self.currNodePtr.children[-1]
        self.addGraphvizEdge(dir = 'curr2new')
    def addExistedChildNodeByID(self, id):
        NewChildPtr = self.getNodeFromID(id)
        self.addExistedChildNode(NewChildPtr)
    def go2Child(self, childPos):
        if childPos < len(self.currNodePtr.children):
            print('move to children No.%d' %childPos)
            oriID = self.currNodePtr.id
            self.currNodePtr = self.currNodePtr.children[childPos]
            print('from node ID %d move to Node ID %d ' %(oriID, self.currNodePtr.id))
        else:
            print('No No.%d child node!' %childPos)
    def go2Parent(self, parentPos):
        if parentPos < len(self.currNodePtr.parents):
            print('move to parent No.%d' %parentPos)
            oriID = self.currNodePtr.id
            self.currNodePtr = self.currNodePtr.parents[parentPos]
            print('from node ID %d move to Node ID %d ' %(oriID, self.currNodePtr.id))
        else:
            print('No No.%d child node!' %parentPos)
    def go2NodeID(self, id):
        if id < len(self.nodeListPtr):
            self.currNodePtr = self.nodeListPtr[id]
            print('Move to node ID %d' %self.currNodePtr.id)
        else:
            print('Out of Range! Node id is not in the list.')
    def getNodeFromID(self, id):
        if id < len(self.nodeListPtr):
            return self.nodeListPtr[id]
        else:
            print('Out of Range! Node id is not in the list.')
    def getCurrChildrenList(self):
        return self.currNodePtr.children
    def getCurrParentsList(self):
        return self.currNodePtr.parents
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
            nodeInfo = 'Node ID' + str(node.id) + ', Value ' + str(node.value)
            #print(nodeInfo)
            desList.append(nodeInfo)
            desList.append('    Children:')
            #print('    Children:')
            for i, child in enumerate(node.children):
                nodeInfo = '      ' + str(i) + '.' + ' Child Node ID' + str(child.id) + ', Value ' + str(child.value)
                #print(nodeInfo)
                desList.append(nodeInfo)
            desList.append('    Parents:')
            #print('    Parents:')
            for i, parent in enumerate(node.parents):
                nodeInfo = '      ' + str(i) + '.' + ' Parent Node ID' + str(parent.id) + ', Value ' + str(parent.value)
                #print(nodeInfo)
                desList.append(nodeInfo)
        return '\n'.join(desList)