import sys

# Basamak sınırı hatasını aşmak için sınırı 20.000'e çıkarıyoruz
# (0 yazarsan sınırı tamamen kaldırır)
sys.set_int_max_str_digits(20000)

# 15.000 basamağa yakın bir sonuç veren Mersenne üssü
p = 49831 
mersenne_prime = 2**p - 1

# Sayıyı masaüstündeki klasörüne kaydet
with open("asal_sayi.txt", "w") as f:
    f.write(str(mersenne_prime))

print(f"Başarılı! Sayı 'asal_sayi.txt' dosyasına yazıldı.")
print(f"Toplam Basamak Sayısı: {len(str(mersenne_prime))}")