def create():
    Q = []
    front = 0
    rear = -1
    size = int(input("Enter the size of the Queue: "))
    print("Empty Queue is created")
    return Q, rear, front, size

def isFull(rear, front, size):
    if (rear >= size - 1):
        return True
    else:
        return False

def isEmpty(front, rear):
    if (front > rear or rear == -1):
        front = 0
        rear = -1
        return True
    else:
        return False

def enqueue(Q, rear, front, size):
    if (isFull(rear, front, size) == 1):
        print("Overflow: Queue is full")
        return Q, rear
    no = int(input("Enter the number to push onto the Queue: "))
    rear += 1
    Q.insert(rear, no)
    return Q, rear

def dequeue(Q, front, rear):
    if (isEmpty(front, rear) == 1):
        front = 0
        rear = -1
        print("Underflow: there is no element in the Queue")
        return Q, front, rear
    else:
        print("The element to dequeue is ", Q[0])
        return Q, front + 1, rear

def display(Q, front, rear, size):
    print("Front is at index -> ", front)
    print("Rear is at index -> ", rear)
    if (isEmpty(front, rear) == 1):
        print("\nQueue is empty")
    elif (isFull(rear, front, size) == 1):
        print("The elements in the Queue are:")
        for i in range(front, rear + 1):
            print(i, "->", Q[i])
        print("Queue is full")
    else:
        print("The elements in the Queue are:")
        for i in range(front, rear + 1):
            print(i, "->", Q[i])
def menu():
    print("\n~~~ MENU ~~~")
    print("1. Insert to Queue")
    print("2. Delete from Queue")
    print("3. Display the Queue")
    print("4. Exit")
    opt = int(input("Enter a valid menu item: "))
    return opt

if __name__ == "__main__":
    Q, rear, front, size = create()
    i = 1
    while (i > 0 and i <= 3):
        i = menu()
        if i == 1:
            Q, rear = enqueue(Q, rear, front, size)
            display(Q, front, rear, size)
        elif i == 2:
            Q, front, rear = dequeue(Q, front, rear)
            if (front > rear):
                front = 0
                rear = -1
            if (type(front) != str):
                display(Q, front, rear, size)
        elif i == 3:
            display(Q, front, rear, size)
        else:
            print("Exit")
