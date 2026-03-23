# Aisim.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# 1. Veri Setini Yükleme
# Ödev 1'de kullanılan CSV dosyası: "Aisim.csv"
data = pd.read_csv("Aisim.csv")

# 2. Kategorik verilerin sayısal hale getirilmesi
# Özellikler için eşleme: 'Düşük'->0, 'Orta'->1, 'Yüksek'->2
mapping = {"Düşük": 0, "Orta": 1, "Yüksek": 2}
data["Satış Fiyatı"]    = data["Satış Fiyatı"].map(mapping)
data["Bakım Masrafı"]   = data["Bakım Masrafı"].map(mapping)
data["Güvenlik"]       = data["Güvenlik"].map(mapping)
data["Bagaj Kapasitesi"] = data["Bagaj Kapasitesi"].map(mapping)

# Hedef değişken için eşleme: 'Yeterli'->1, 'Yeterli Değil'->0
target_mapping = {"Yeterli": 1, "Yeterli Değil": 0}
data["Arabanın Sınıfı"] = data["Arabanın Sınıfı"].map(target_mapping)

# 3. Özellikler (X) ve Hedef (y) Belirleme
X = data[["Satış Fiyatı", "Bakım Masrafı", "Güvenlik", "Bagaj Kapasitesi"]]
y = data["Arabanın Sınıfı"]

# 4. Eğitim ve Test Verilerine Bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Karar Ağacı Modelini Oluşturma ve Eğitme
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# 6. Test Verisi Üzerinde Tahmin
y_pred = clf.predict(X_test)

# 7. Model Değerlendirme: Karışıklık Matrisi ve Sınıflandırma Raporu
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Karar Ağacını Görselleştirme
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=["Yeterli Değil", "Yeterli"])
plt.savefig("Aisism.png")
plt.show()