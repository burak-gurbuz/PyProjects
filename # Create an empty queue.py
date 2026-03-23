# Create an empty queue
def create():
    Q = []
    front = 0
    rear = -1
    print("Empty Queue created")
    return Q, rear, front
def isEmpty(front, rear):
    if (front > rear or rear == -1):
        front = 0
        rear = -1
        return 1
    else:
        return 0
def enqueue(Q, rear):
    no = int(input("Enter a number to push onto the Queue: "))
    rear += 1
    Q.insert(rear, no)
    return Q, rear
def dequeue(Q, front, rear):
    if (isEmpty(front, rear) == 1):
        front = 0
        rear = -1
        print("Underflow: There is no element in the Queue")
        return Q, front, rear
    else:
        print("The element to dequeue is ", Q[front])
        return Q, front + 1, rear
def display(Q, front, rear):
    print("Front is at index -> ", front)
    print("Rear is at index -> ", rear)
    if (isEmpty(front, rear) == 1):
        print("\nQueue is Empty")
    else:
        print("The elements in the Queue are")
        for i in range(front, rear + 1):
            print(i, "->", Q[i])
def menu():
    print("\n~~~ MENU ~~~")
    print("1. Insert to Queue")
    print("2. Delete from Queue")
    print("3. Display the Queue")
    print("4. Exit")
    opt = int(input("Enter a valid menu item ... "))
    return opt

# Main Program
if __name__ == "__main__":
    Q, rear, front = create()
    i = 1
    while (i > 0 and i <= 3):
        i = menu()
        if i == 1:
            Q, rear = enqueue(Q, rear)
            display(Q, front, rear)
        elif i == 2:
            Q, front, rear = dequeue(Q, front, rear)
            if (front > rear):
                front = 0
                rear = -1
            if (type(front) != str):
                display(Q, front, rear)
        elif i == 3:
            display(Q, front, rear)
        else:
            print("Exit")


