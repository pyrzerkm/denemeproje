import os

gorevler = []

def gorevleri_yukle():
    if os.path.exists("gorevler.txt"):
        with open("gorevler.txt", "r", encoding="utf-8") as f:
            for satir in f:
                satir = satir.strip()
                if "|" in satir:
                    durum, aciklama = satir.split("|", 1)
                    gorevler.append({"aciklama": aciklama, "tamamlandi": durum == "TAMAMLANDI"})

def gorevleri_kaydet():
    with open("gorevler.txt", "w", encoding="utf-8") as f:
        for gorev in gorevler:
            durum = "TAMAMLANDI" if gorev["tamamlandi"] else "YAPILACAK"
            f.write(f"{durum}|{gorev['aciklama']}\n")

def gorev_ekle():
    aciklama = input("Görev açıklaması: ")
    gorevler.append({"aciklama": aciklama, "tamamlandi": False})

def gorevleri_listele(filtre=None):
    for i, gorev in enumerate(gorevler, 1):
        durum = "✓" if gorev["tamamlandi"] else "✗"
        if filtre == "tamamlandi" and not gorev["tamamlandi"]:
            continue
        if filtre == "yapilacak" and gorev["tamamlandi"]:
            continue
        print(f"{i}. [{durum}] {gorev['aciklama']}")

def gorev_tamamla():
    gorevleri_listele()
    try:
        no = int(input("Tamamlanan görev numarası: "))
        gorevler[no - 1]["tamamlandi"] = True
    except:
        print("Hatalı giriş!")

def gorev_sil():
    gorevleri_listele()
    try:
        no = int(input("Silinecek görev numarası: "))
        gorevler.pop(no - 1)
    except:
        print("Hatalı giriş!")

def filtrele():
    print("1. Tüm görevler")
    print("2. Sadece tamamlananlar")
    print("3. Sadece yapılacaklar")
    secim = input("Seçim: ")
    if secim == "2":
        gorevleri_listele(filtre="tamamlandi")
    elif secim == "3":
        gorevleri_listele(filtre="yapilacak")
    else:
        gorevleri_listele()

def menu():
    gorevleri_yukle()
    while True:
        print("\n1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Tamamla")
        print("4. Görev Sil")
        print("5. Görevleri Filtrele")
        print("0. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            gorev_ekle()
        elif secim == "2":
            gorevleri_listele()
        elif secim == "3":
            gorev_tamamla()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            filtrele()
        elif secim == "0":
            gorevleri_kaydet()
            print("Görevler kaydedildi. Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    menu()
