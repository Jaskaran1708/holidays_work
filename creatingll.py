class linkedlist:
    def __init__(self,value,nextnode = None):
        self.value= value
        self.nextnode= nextnode

node1 = linkedlist(1)
node2 = linkedlist(2)
node3 = linkedlist(4)
node1.nextnode= node2
node2.nextnode = node3
node3.nextnode = None
currentnode= node1
while True:
    print(currentnode.value, "->")
    if currentnode.nextnode is None:
        print("None")
        break
    else:
        currentnode = currentnode.nextnode