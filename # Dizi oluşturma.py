#create a list of integer
def create(n):
    lst = []
    for i in range(n):
        no = int(input("Enter the number "))
        lst.append(no)
    return lst

def display(a):
    print("The data in the array are :")
    print(a)

# Listeden belirli bir konumdan veri erişimi
def access(a, i):
    if 0 <= i < len(a):
        print("The element at position ", i, " is ", a[i])
    else:
        print("The index is more than the size of array")

# Listeye belirli bir konumda veri ekleme
def insrt(a, i, x):
    if i < 0:
        print("Location is below the range")
        return a
    elif i > len(a):
        print("Location is out of the range")
        return a
    else:
        a.insert(i, x)
        return a
# Delete a data from the list at a given location
def delit(a, i):
    if i < 0:
        print("Location is below the range")
        return a
    elif i > len(a):
        print("Location is out of the range")
        return a
    else:
        del a[i]
        return a
# Main Program
n = int(input("Enter How many numbers in an array "))
Arr = create(n)
display(Arr)

print("\n---  Data at Location  ---")
i = int(input("Element at which position element to get "))
access(Arr, i)

print("\n---  Insert at a Location  ---")
j = int(input("Specify the Location to Insert "))
y = int(input("Specify the Data "))
Arr = insrt(Arr, j, y)
display(Arr)

print("\n---  Deletion at position  ---")
j = int(input("Specify the Location to Delete "))
Arr = delit(Arr, j)
display(Arr)
