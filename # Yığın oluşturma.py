# Yığın oluşturma
def create():
    return [], -1  # Boş bir liste ve top = -1 ile başlıyoruz

# Yığının boş olup olmadığını kontrol etme
def isEmpty(stack, top):
    return top == -1  # Eğer top -1 ise, yığın boştur

# Eleman ekleme (Push)
def push(stack, top, value):
    stack.append(value)  # Elemanı listeye ekle
    top += 1  # top değişkenini güncelle
    return stack, top

# Eleman çıkarma (Pop)
def pop(stack, top):
    if top == -1:  # Eğer yığın boşsa
        print("Stack Underflow - Yığın boş!")
        return stack, top
    print("Çıkarılan eleman:", stack[top])
    stack.pop()  # Üstteki elemanı çıkar
    top -= 1  # top değerini azalt
    return stack, top

# Üstteki elemanı gösterme (Peek)
def peek(stack, top):
    if top == -1:
        print("Stack Underflow - Yığın boş!")
        return None
    print("Yığının üst elemanı:", stack[top])
    return stack[top]

# Yığını görüntüleme
def display(stack, top):
    if top == -1:
        print("Yığın boş!")
    else:
        print("Yığın elemanları (üstten alta):", stack[::-1])  # Listeyi ters çevirerek göster
# Ana program
stack, top = create()  # Yığın oluştur
stack, top = push(stack, top, 10)  # 10 ekle
stack, top = push(stack, top, 20)  # 20 ekle
peek(stack, top)  # Yığının üst elemanını görüntüle
stack, top = pop(stack, top)  # Üst elemanı çıkar
display(stack, top)  # Yığındaki elemanları görüntüle
