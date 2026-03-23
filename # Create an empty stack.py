# Create an empty stack
def create():
    S = []
    top = -1
    print("Empty Stack created")
    return S, top

# Checks if the stack is empty
def isEmpty(top):
    if top <= -1:
        return 1
    else:
        return 0

def push(S,top):
    no = int(input(("Enter a number to push onto the stack")))
    top += 1
    S.insert(top, no)
    return S, top

#Delete from stack
def pop(S,top):
    if (isEmpty(top)==1):
        print("Underflow: There is no element in the Stack")
    else:
        print("The element to pop is",S[top])
        top -= 1
    return S, top

#Returns the top of the stack
def peek(S,top):
    if (isEmpty(top)==1):
        print("Stack is Empty")
    else:
        print("The top of the stack is",S[top])

#Displays the stack element
def display(S, top):
    print("Top is at index -> ", top)
    if (isEmpty(top) == 1):
        print("\nStack is Empty")
    else:
        print("The elements in the Stack are")
        for i in range(top, -1, -1):
            print(i, "->", S[i])
def menu():
    print("\n~~~ MENU ~~~")
    print("1. Push an element")
    print("2. Pop from stack")
    print("3. Peek the stack")
    print("4. Display the stack")
    print("5. Exit")
    opt = int(input("Enter a valid menu item ... "))
    return opt

# Main Program
if __name__ == "__main__":
    St, top = create()
    i = 1
    while (i > 0 and i < 5):
        i = menu()
        if i == 1:
            St, top = push(St, top)
            display(St, top)
        elif i == 2:
            St, top = pop(St, top)
            if (type(top) != str):
                display(St, top)
        elif i == 3:
            peek(St, top)
        elif i == 4:
            display(St, top)
        else:
            print("Exit")
