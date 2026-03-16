class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

class CLinkedList:
    def __init__(self):
        self.start = Node(None)  # Başlangıç düğümü (boş)
        self.end = Node(None)    # Bitiş düğümü (boş)
        self.start.next = self.end
        self.end.next = self.start

    def listprint(self):
        print("The Elements in the Linked List are : ", end="")
        if self.start.data is None:  # Liste boşsa
            print("There is no data..")
            return
        temp = self.start
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.start:
                break
        print()

    def insert_At_Begining(self, newdata):
        NewNode = Node(newdata)
        if self.start.data is None:  # Liste boşsa
            self.start = NewNode
            self.end = NewNode
            self.end.next = self.start
        else:
            NewNode.next = self.start
            self.start = NewNode
            self.end.next = self.start

    def insert_At_End(self, newdata):
        NewNode = Node(newdata)
        if self.start.data is None:  # Liste boşsa
            self.insert_At_Begining(newdata)
            return
        NewNode.next = self.start
        self.end.next = NewNode
        self.end = NewNode

    def insert_After(self, data, newdata):
        temp = self.start
        while temp.data != data and temp.next != self.start:
            temp = temp.next
        if temp.data != data and temp.next == self.start:
            print(data, " Not Found")
        elif temp.data == data and temp.next == self.start:
            self.insert_At_End(newdata)
        else:
            NewNode = Node(newdata)
            NewNode.next = temp.next
            temp.next = NewNode

    def insert_Before(self, data, newdata):
        temp = self.start
        if temp.data == data:
            self.insert_At_Begining(newdata)
        else:
            while temp.next.data != data and temp.next != self.start:
                temp = temp.next
            if temp.next.data != data and temp.next == self.start:
                print(data, " Not Found")
            else:
                NewNode = Node(newdata)
                NewNode.next = temp.next
                temp.next = NewNode

    def del_first(self):
        if self.start == self.end:  # Tek düğüm varsa
            self.start = Node(None)
            self.end = Node(None)
            self.end.next = self.start
            return
        temp = self.start
        self.start = temp.next
        self.end.next = self.start
        del temp

    def del_last(self):
        if self.start == self.end:  # Tek düğüm varsa
            self.del_first()
            return
        temp = self.start
        while temp.next.next != self.start:
            temp = temp.next
        temp1 = temp.next
        temp.next = self.start
        self.end = temp
        del temp1

    def del_node(self, data):
        temp = self.start
        if temp.data == data:
            self.del_first()
            return
        while temp.next.data != data and temp.next.next != self.start:
            temp = temp.next
        if temp.next.data != data and temp.next.next == self.start:
            print(data, " Not Found")
        elif temp.next.data == data and temp.next.next == self.start:
            self.del_last()
        else:
            temp1 = temp.next
            temp.next = temp1.next
            del temp1

    def del_after(self, data):
        temp = self.start
        if temp.data == data and self.start == self.end:
            print("There is only one element in the list...")
            print("Next element cannot be deleted..")
            return
        while temp.data != data and temp.next != self.start:
            temp = temp.next
        if temp.data != data and temp.next == self.start:
            print(data, " data Not found")
        elif temp.data == data and temp.next == self.start:
            print(data, " is the Last node.. the next node is First node")
            ch = input("Do you want to delete the first node (y | Y) : ")
            if ch.lower() == 'y':
                self.del_first()
                return
        else:
            temp1 = temp.next
            temp.next = temp1.next
            del temp1

    def del_before(self, data):
        temp = self.start
        if (temp.data == data and self.start == self.end) or temp.next.data == data:
            self.del_first()
            return
        elif temp.data == data and temp == self.start:
            self.del_last()
            return
        else:
            while temp.data != data and temp.next != self.start:
                temp = temp.next
            if temp.data != data and temp.next == self.start:
                print(data, " data Not found")
            else:
                temp1 = self.start
                while temp1.next != temp:
                    temp1 = temp1.next
                temp2 = temp1.next
                temp1.next = temp
                del temp2

def menu():
    print("\n~~~ MENU ~~~")
    print("1. Create a Single Linked List")
    print("2. Insert at the Beginning")
    print("3. Insert at the End")
    print("4. Insert After a given Data")
    print("5. Insert before a given Data")
    print("6. Delete the First node")
    print("7. Delete the Last node")
    print("8. Delete a given node")
    print("9. Delete After a given Data")
    print("10. Delete before a given Data")
    print("11. Exit")
    while True:
        try:
            opt = int(input("Enter a valid menu item ... "))
            if 1 <= opt <= 11:
                return opt
            else:
                print("Please enter a number between 1 and 11.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    list1 = CLinkedList()
    while True:
        i = menu()

        if i == 1:
            x = input("Enter data to create the first node: ")
            list1.start = Node(x)
            list1.end = list1.start
            list1.end.next = list1.start
            list1.listprint()
        elif i == 2:
            x = input("Enter data to insert at the beginning: ")
            list1.insert_At_Begining(x)
            list1.listprint()
        elif i == 3:
            x = input("Enter data to insert at the end: ")
            list1.insert_At_End(x)
            list1.listprint()
        elif i == 4:
            x = input("Enter data to create the node: ")
            y = input("Node to be created after data: ")
            list1.insert_After(y, x)
            list1.listprint()
        elif i == 5:
            x = input("Enter data to create the node: ")
            y = input("Node to be created before data: ")
            list1.insert_Before(y, x)
            list1.listprint()
        elif i == 6:
            list1.del_first()
            list1.listprint()
        elif i == 7:
            list1.del_last()
            list1.listprint()
        elif i == 8:
            x = input("Node to be deleted: ")
            list1.del_node(x)
            list1.listprint()
        elif i == 9:
            x = input("Node to be deleted after data: ")
            list1.del_after(x)
            list1.listprint()
        elif i == 10:
            x = input("Node to be deleted before data: ")
            list1.del_before(x)
            list1.listprint()
        else:
            print("Exiting the program...")
            break
