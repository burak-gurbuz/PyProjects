
class Node:  # Class Definition of a Node in Double Linked List
    def __init__(self, dataval=None):
        self.prev = None
        self.data = dataval
        self.next = None

class DLinkedList:  # Class Definition of a Double Linked List
    def __init__(self):
        self.start = Node(None)

    def listprint(self):  # Printing the elements of a DLL List
        print("The Elements in the Linked List are: ", end=" ")
        printval = self.start
        while printval is not None:
            print(printval.data, end=" ")
            printval = printval.next
        print("\n")

def insert_At_Begining(self, newdata):
    NewNode = Node(newdata)
    if (self.start == None):
        self.start = NewNode
    else:
        NewNode.next = self.start
        self.start.prev = NewNode
        self.start = NewNode

def insert_At_End(self, newdata):
    if (self.start == None):
        self.insert_At_Begining(newdata)
        return
    NewNode = Node(newdata)
    temp = self.start
    while(temp.next != None):
        temp = temp.next
    temp.next = NewNode
    NewNode.prev = temp

def insert_After(self, key, newdata):
    temp = self.start
    while(temp.data != key and temp.next != None):
        temp = temp.next
    if (temp.data != key and temp.next == None):
        print(key, "Not Found")
    elif (temp.data == key and temp.next == None):
        self.insert_At_End(newdata)
    else:
        NewNode = Node(newdata)
        NewNode.next = temp.next
        NewNode.prev = temp
        temp.next.prev = NewNode
        temp.next = NewNode

def insert_Before(self, key, newdata):
    temp = self.start
    if (temp.data == key):
        self.insert_At_Begining(newdata)
    else:
        while(temp.data != key and temp.next != None):
            temp = temp.next
        if (temp.next == None):
            print(key, " Not Found")
        else:
            NewNode = Node(newdata)
            NewNode.next = temp.next
            NewNode.prev = temp
            temp.next.prev = NewNode
            temp.next = NewNode

def del_first(self):
    if(self.start != None):
        temp = self.start
        self.start = self.start.next
        temp.next = None
        del temp
    if (self.start != None):
        self.start.prev = None

def del_last(self):
    temp = self.start
    if (temp.next == None):
        self.del_first()
        return
    while(temp.next.next != None):
        temp = temp.next
    temp1 = temp.next
    temp.next = None
    del temp1

def del_node(self, key):
    temp = self.start
    if (temp.data == key):
        self.del_first()
        return
    while(temp.data != key and temp.next != None):
        temp = temp.next
    if (temp.data != key and temp.next == None):
        print(data, "Not Found")
    elif(temp.data == key and temp.next == None):
        self.del_last()
    else:
        temp1 = temp.prev
        print(temp1.data)
        temp1.next = temp.next
        temp.next.prev = temp1
        del temp

def insert_After(self, key, newdata):
    temp = self.start
    while(temp.data != key and temp.next != None):
        temp = temp.next
    if (temp.data != key and temp.next == None):
        print(key, "Not Found")
    elif (temp.data == key and temp.next == None):
        self.insert_At_End(newdata)
    else:
        NewNode = Node(newdata)
        NewNode.next = temp.next
        NewNode.prev = temp
        temp.next.prev = NewNode
        temp.next = NewNode
