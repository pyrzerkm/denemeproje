def menu_goster():
    print("\n📝 Yapılacaklar Listesi")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Çıkış\n")

gorevler = []

while True:
    menu_goster()
    secim = input("Seçiminizi girin (1-3): ")

    if secim == "1":
        yeni_gorev = input("Yeni görevi girin: ")
        gorevler.append(yeni_gorev)
        print("✅ Görev eklendi!")
    elif secim == "2":
        print("\n📋 Görevler:")
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")
    elif secim == "3":
        print("👋 Programdan çıkılıyor...")
        break
    else:
        print("❌ Geçersiz seçim! Lütfen 1-3 arası bir sayı girin.")
