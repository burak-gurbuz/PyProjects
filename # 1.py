# 1. Stack Implementation Using a List

# Creating an empty stack
def create():
    return [], -1

# Checking if the stack is empty
def isEmpty(stack, top):
    return top == -1

# Adding an element to the stack (push)
def push(stack, top, element):
    stack.append(element)
    top += 1
    return stack, top

# Removing the top element from the stack (pop)
def pop(stack, top):
    if isEmpty(stack, top):
        print("Stack underflow! Cannot pop from an empty stack.")
        return stack, top
    else:
        element = stack.pop()
        top -= 1
        print(f"Popped element: {element}")
        return stack, top

# Viewing the top element of the stack without removing it (peek)
def peek(stack, top):
    if isEmpty(stack, top):
        print("Stack underflow! No element to peek.")
        return None
    else:
        print(f"Top element: {stack[top]}")
        return stack[top]

# Displaying all elements of the stack
def display(stack):
    print("Stack elements (top to bottom):")
    for element in reversed(stack):
        print(element)

# Example usage
stack, top = create()
stack, top = push(stack, top, 10)
stack, top = push(stack, top, 20)
stack, top = push(stack, top, 30)
display(stack)
peek(stack, top)
stack, top = pop(stack, top)
display(stack)

# 2. Stack Implementation Using a Dictionary

def create_dict():
    return {}, -1

# Checking if the stack is full or empty (similar methods as above can be implemented)

# Adding, removing, peeking, and displaying logic can be adapted for dictionary-based implementation.
# For brevity, skipping repetitive parts.

# 3. Stack Implementation Using a Class

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size

    def isFull(self):
        return self.top >= self.max_size - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, element):
        if self.isFull():
            print("Stack overflow! Cannot push to a full stack.")
        else:
            self.stack.append(element)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Stack underflow! Cannot pop from an empty stack.")
        else:
            element = self.stack.pop()
            self.top -= 1
            print(f"Popped element: {element}")

    def peek(self):
        if self.isEmpty():
            print("Stack underflow! No element to peek.")
        else:
            print(f"Top element: {self.stack[self.top]}")

    def display(self):
        print("Stack elements (top to bottom):")
        for element in reversed(self.stack):
            print(element)

# Example usage
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.display()

# 4. Applications of Stack: Delimiter Matching

def delimiter_matching(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or \
               (top == '{' and char != '}') or \
               (top == '[' and char != ']'):
                return False
    return not stack

# Example usage
expression = "a[5]+(b-{c*(d-e)+(f-g)})"
print("Delimiter matching result:", delimiter_matching(expression))

# 5. Infix to Postfix Conversion

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    result = []
    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return ''.join(result)

# Example usage
infix_expr = "A/(B+C)*D"
print("Postfix expression:", infix_to_postfix(infix_expr))

# 6. Evaluation of Postfix Expression

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    return stack.pop()

# Example usage
postfix_expr = "135*+"
print("Evaluation result:", evaluate_postfix(postfix_expr))