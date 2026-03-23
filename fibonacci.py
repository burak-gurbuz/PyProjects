def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Böl ve fethet yöntemiyle Fibonacci hesaplama
    sol = fibonacci(n - 1)
    sag = fibonacci(n - 2)
    
    return sol + sag

# Örnek kullanım
n = 10  # Kaçıncı Fibonacci sayısını hesaplamak istiyoruz?
print(f"{n}. Fibonacci sayısı: {fibonacci(n)}")