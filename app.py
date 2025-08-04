import os

def menu_goster():
    print("\n📝 Yapılacaklar Listesi")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Çıkış\n")

def gorevleri_yukle(dosya_adi="gorevler.txt"):
    if not os.path.exists(dosya_adi):
        return []
    with open(dosya_adi, "r", encoding="utf-8") as f:
        return [satir.strip() for satir in f.readlines()]

def gorevleri_kaydet(gorevler, dosya_adi="gorevler.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for gorev in gorevler:
            f.write(gorev + "\n")

# Başlangıçta görevleri dosyadan yükle
gorevler = gorevleri_yukle()

while True:
    menu_goster()
    secim = input("Seçiminizi girin (1-3): ")

    if secim == "1":
        yeni_gorev = input("Yeni görevi girin: ")
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print("✅ Görev eklendi!")
    elif secim == "2":
        print("\n📋 Görevler:")
        if not gorevler:
            print("Henüz hiç görev yok.")
        else:
            for i, gorev in enumerate(gorevler, 1):
                print(f"{i}. {gorev}")
    elif secim == "3":
        print("👋 Programdan çıkılıyor...")
        break
    else:
        print("❌ Geçersiz seçim! Lütfen 1-3 arası bir sayı girin.")
