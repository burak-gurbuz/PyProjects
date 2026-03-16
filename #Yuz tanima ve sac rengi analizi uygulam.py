#Yuz tanima ve sac rengi analizi uygulamasi
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Haar Cascade siniflandiricilari
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Kamera baslatma
vid = cv2.VideoCapture(0)

# Yas tahmini icin ortalama hesaplama
age_history = []
AGE_HISTORY_SIZE = 10  # Son 10 tahmini sakla

def detect_mask(face_roi_gray, face_w, face_h):
    # Burun bolgesini tanimla: yuzun ortasinda (x + w/2, y + 3*h/5)
    nose_x = face_w // 2 - (face_w // 4) // 2
    nose_y = int(3 * face_h / 5) - (face_h // 5) // 2
    nose_w = face_w // 4
    nose_h = face_h // 5

    # Burun bolgesini cikar
    nose_region = face_roi_gray[nose_y:nose_y + nose_h, nose_x:nose_x + nose_w]

    # Ortalama parlakligi hesapla
    average_brightness = cv2.mean(nose_region)[0]

    # Maske tespiti icin esik degeri (ayarlanabilir)
    threshold = 80

    if average_brightness < threshold:
        return True
    else:
        return False

def calculate_average_age(estimated_age):
    # Yas tahmini gecmisini guncelle
    age_history.append(estimated_age)
    if len(age_history) > AGE_HISTORY_SIZE:
        age_history.pop(0)

    # Ortalama yasi hesapla
    if len(age_history) > 0:
        return int(np.mean(age_history))
    else:
        return estimated_age

def detect_eye_color(eye_roi):
    # Goz bolgesini HSV renk uzayina cevir
    eye_hsv = cv2.cvtColor(eye_roi, cv2.COLOR_BGR2HSV)

    # Renk araliklarini tanimla
    blue_mask = cv2.inRange(eye_hsv, (100, 50, 50), (130, 255, 255))  # Mavi
    green_mask = cv2.inRange(eye_hsv, (40, 50, 50), (80, 255, 255))  # Yesil
    brown_mask = cv2.inRange(eye_hsv, (10, 50, 50), (20, 255, 200))  # Kahverengi
    gray_mask = cv2.inRange(eye_hsv, (0, 0, 50), (180, 50, 200))  # Gri

    # Renk oranlarini hesapla
    total_pixels = eye_roi.shape[0] * eye_roi.shape[1]
    blue_ratio = np.sum(blue_mask) / total_pixels
    green_ratio = np.sum(green_mask) / total_pixels
    brown_ratio = np.sum(brown_mask) / total_pixels
    gray_ratio = np.sum(gray_mask) / total_pixels

    # Goz rengini belirle
    if blue_ratio > 0.5:
        return "Mavi"
    elif green_ratio > 0.5:
        return "Yesil"
    elif brown_ratio > 0.5:
        return "Kahverengi"
    elif gray_ratio > 0.5:
        return "Gri"
    else:
        return "Bilinmiyor"

def update_frame():
    ret, frame = vid.read()
    if ret:
        # Goruntuyu Y ekseninde aynala
        mirrored_frame = cv2.flip(frame, 1)

        # Gri tonlamaya cevir
        gray = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2GRAY)

        # Yuzleri tespit et
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Yuz cevresine dikdortgen ciz
            cv2.rectangle(mirrored_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Yuzun alt kismini incele (gulumseme icin)
            face_roi_gray = gray[y + int(h * 0.6):y + h, x:x + w]
            face_roi_color = mirrored_frame[y + int(h * 0.6):y + h, x:x + w]

            # Gulumsemeleri tespit et
            smiles = smile_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(30, 30))

            # En buyuk gulumseme alanini bul
            max_smile_area = 0
            smile_level = 0

            for (sx, sy, sw, sh) in smiles:
                # Gulumseme cevresine dikdortgen ciz
                cv2.rectangle(face_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
                # Gulumseme alanini hesapla
                smile_area = sw * sh
                if smile_area > max_smile_area:
                    max_smile_area = smile_area

            # Gulumseme yogunlugunu hesapla
            face_area = w * h
            if face_area != 0:
                smile_intensity = max_smile_area / face_area
            else:
                smile_intensity = 0.0

            # Gulumseme seviyesini belirle
            if 0.0 < smile_intensity <= 0.05:
                smile_level = 1
            elif 0.05 < smile_intensity <= 0.1:
                smile_level = 2
            elif smile_intensity > 0.1:
                smile_level = 3
            else:
                smile_level = 0

            # Sac bolgesini tanimla (yuzun ust kismi)
            hair_region = mirrored_frame[max(0, y - int(h * 0.3)):y, x:x + w]

            if hair_region.size > 0:
                hair_hsv = cv2.cvtColor(hair_region, cv2.COLOR_BGR2HSV)

                # Renk araliklarini tanimla
                black_mask = cv2.inRange(hair_hsv, (0, 0, 0), (180, 255, 50))  # Siyah sac
                brown_mask = cv2.inRange(hair_hsv, (10, 50, 50), (20, 255, 200))  # Kahverengi sac
                yellow_mask = cv2.inRange(hair_hsv, (20, 50, 50), (30, 255, 255))  # Sari sac

                total_pixels = hair_region.shape[0] * hair_region.shape[1]
                black_ratio = np.sum(black_mask) / total_pixels
                brown_ratio = np.sum(brown_mask) / total_pixels
                yellow_ratio = np.sum(yellow_mask) / total_pixels

                # Sac rengini belirle
                if black_ratio > 0.5:
                    hair_color = "Siyah"
                    base_age = 20
                elif brown_ratio > 0.5:
                    hair_color = "Kahverengi"
                    base_age = 25
                elif yellow_ratio > 0.5:
                    hair_color = "Sari"
                    base_age = 15
                else:
                    hair_color = "Cakma_Sari"
                    base_age = 30

                # Yas tahmini (gulumseme seviyesi etkilemesin)
                estimated_age = base_age
                estimated_age = max(10, estimated_age)  # Yasin 10'dan kucuk olmamasini sagla

                # Yasi 10 ile 22 arasinda bir degere eslestir
                if 10 <= estimated_age <= 22:
                    estimated_age = estimated_age  # Yasi oldugu gibi kullan
                else:
                    estimated_age = 30  # Varsayilan yas

                # Ortalama yasi hesapla
                average_age = calculate_average_age(estimated_age)

                # Bilgileri ekrana yazdir
                cv2.putText(mirrored_frame, f"Sac Renk: {hair_color}", (x, y - 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(mirrored_frame, f"Yas: {average_age}", (x, y - 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
                if smile_level > 0:
                    cv2.putText(mirrored_frame, f"Gulumseme: Seviye {smile_level}", (x, y - 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    cv2.putText(mirrored_frame, "Gulumseme: Yok", (x, y - 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

                # Maske tespiti
                mask_detected = detect_mask(gray[y:y + h, x:x + w], w, h)
                if mask_detected:
                    cv2.putText(mirrored_frame, "Maske Tespit Edildi", (x, y + h + 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                cv2.putText(mirrored_frame, "Sac Bolgesi Tespit Edilemedi", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

            # Gozleri tespit et
            eyes = eye_cascade.detectMultiScale(gray[y:y + int(h * 0.5), x:x + w])
            eye_colors = {"Sol Goz": "Bilinmiyor", "Sag Goz": "Bilinmiyor"}

            for (ex, ey, ew, eh) in eyes:
                # Gozun merkezini bul
                eye_center = x + ex + ew // 2

                # Sol goz mu sag goz mu?
                if eye_center < x + w // 2:
                    eye_side = "Sol Goz"
                else:
                    eye_side = "Sag Goz"

                # Goz bolgesini cikar
                eye_roi = mirrored_frame[y + ey:y + ey + eh, x + ex:x + ex + ew]

                # Goz rengini tespit et
                eye_color = detect_eye_color(eye_roi)
                eye_colors[eye_side] = eye_color

                # Goz cevresine dikdortgen ciz
                cv2.rectangle(mirrored_frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 255), 2)

            # Goz renklerini ekrana yazdir
            cv2.putText(mirrored_frame, f"Sol Goz: {eye_colors['Sol Goz']}", (x, y - 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(mirrored_frame, f"Sag Goz: {eye_colors['Sag Goz']}", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)

        # Goruntuyu Tkinter'a uygun formata cevir
        img = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)

        # Görüntüyü güncelle
        panel.img = img
        panel.config(image=img)

    # Her 10 ms'de bir güncelle
    panel.after(10, update_frame)

# Tkinter arayüzünü oluştur
root = tk.Tk()
root.title("Yuz ve Sac Analizi")

# Görüntü paneli
panel = tk.Label(root)
panel.pack()

# Görüntüyü güncelle
update_frame()

# Arayüzü başlat
root.mainloop()

# Kamerayi serbest birak ve pencereleri kapat
vid.release()
cv2.destroyAllWindows()
