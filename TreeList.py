from queue import Queue
LEFTNODE = 'leftnode'
RIGHTNODE = 'rightnode'
class Node():
    def __init__(self, value):
        self.id = None
        self.isRootNode = False
        self.value = value
        self.parent = None
        self.leftChild = None
        self.rightChild = None
    def insertLeftNode(self, value):
        if self.leftChild == None:
            self.leftChild = Node(value)
        else:
            newNode = Node(value)
            newNode.leftChild = self.leftChild
            self.node.leftChild = newNode
    def insertRightNode(self, value):
        if self.rightChild == None:
            self.rightChild = Node(value)
        else:
            newNode = Node(value)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode
    def assignParent(self, parentNode):
        self.parent = parentNode

class BinaryTree():
    def __init__(self):
        self.rootNode = None
        self.currNodePtr = None
        self.parentNodePtr = None
    def newTree(self, value):
        '''
        Create new tree. 
        Assign rootNode, currNodePtr, parentNodePtr and Node.value
        
        Parameters
        ------------------------------------------------
        value:
            - type: str, int 
        '''
        if self.rootNode == None:
            self.rootNode = Node(value)
            self.rootNode.isRootNode = True
            self.rootNode.parent = self.rootNode
            self.currNodePtr = self.rootNode
            self.parentNodePtr = self.rootNode
    def insertNode(self, value, nodePosition = LEFTNODE):
        '''
        Inserting new node for current node (currentNodePtr)
        Assign LEFTNODE or RIGHTNODE by user. Default is LEFTNODE

        Parameters
        ------------------------------------------------
        value:
            - type: str, int
        nodePosition:
            - type: str. Predefine LEFTNODE or RIGHTNODE in global variables
        '''
        if nodePosition == LEFTNODE:
            self.currNodePtr.insertLeftNode(value)
        elif nodePosition == RIGHTNODE:
            self.currNodePtr.insertRightNode(value)
        else:
            print('Fail to add new node')
    def go2LeftNode(self):
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
    def go2RightNode(self):
        if self.currNodePtr.rightChild:
            print('move node to right node')
            self.parentNodePtr = self.currNodePtr
            self.currNodePtr = self.currNodePtr.rightChild
            print('from node value %d move to %d ' %(self.parentNodePtr.value, self.currNodePtr.value))
            print('new node parent value is %d' %(self.parentNodePtr.value))
            if not(self.currNodePtr.isRootNode) and (self.currNodePtr.parent==None):
               self.currNodePtr.assignParent(self.parentNodePtr)
               print('no parent in Node.parent')
               print('current node value: %d' %self.currNodePtr.value)
               print('parent node value: %d' %self.currNodePtr.parent.value)
        else:
             print('No right child node!')
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



