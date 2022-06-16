class linkedlistnode:
    def __init__(self,value, nextnode = None):
        self.value = value
        self.nextnode = nextnode

class linkedlist:
    def __init__(self,head = None):
        self.head = head

    def insert(self, value):
        node = linkedlistnode(value)
        if self.head is None:
            self.head = node
            return
        currentnode = self.head
        while True:
            if currentnode.nextnode is None:
                currentnode.nextnode = node
                break
            currentnode = currentnode.nextnode
    def print(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.value, "->")
            currentnode = currentnode.nextnode
        print("none")
    def merge(self,ll2):
        currentnode = self.head
        while currentnode is not None:
            currentnode = currentnode.nextnode
            if (currentnode.nextnode is None):
                currentnode.nextnode =   ll2.head


ll = linkedlist()
# ll.print()
ll.insert(4)
ll.insert(11)
ll.print()
ll2 = linkedlist()
ll2.insert(2)
ll2.print() 
ll.merge(ll2)
ll.print()
