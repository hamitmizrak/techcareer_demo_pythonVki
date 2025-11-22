# _vki_console.py

# vki hesapla
def hesapla_vki(kilo,boy):
    """
    :param kilo:
    :param boy:
    :return:

    VKI: Kilo(kg) boy(metre) değerleri alır.
    VKI (Vücut Kitle İndexi)
    """
    return kilo/(boy**2)

# vki kategori
def vki_kategori(vki):
    """
    :param vki:
    :return:

    VKI değerlerine göre sınıflandırma
    """
    if vki<18.5:
        return "Zayıf"
    elif vki<25:
        return "Normal"
    elif vki<30:
        return "Fazla Kilolu"
    else:
        return "Obezsiniz"

# kullanıcıdan veriler alacağım
def kullanidan_deger_al():
    """
    Kullanıdan Kilo ve boy bilgisini alacağım.
    Dikkat: Kilo alırken virgülü unutma
    :return:
    """
    while True:
        try:
            print("\nLütfen bilgileri eksiksiz griniz:")
            kilo= float(input("Kilonuz (Kg): "))
            boy= float(input("Boyunuz (metre): örnek:1.75 "))

            if(kilo<=0 or boy <=0):
                print("🚦Dikkat: Kilo ve boy sıfır olamaz. Lütfen Tekrar giriniz. ")
                continue

            return kilo,boy
        except ValueError:
            print("🚦Lütfen sadece sayısal değerler giriniz örnek:70, 1.75")


# Sonuçları yazdır
def sonucu_yazdir(kilo, boy, vki, kategori):
    """
    :param vki:
    :param kilo:
    :param boy:
    :param kategori:
    :return:

    Hesaplanan sonuçları ekrana düzenli bir şekilde göstersin
    """

    print("\n=== Sonuçlar ===")
    print(f"Kilonuz: {kilo: .1f} Kg")
    print(f"Boyunuz: {boy:.2f} Metre")

    print(f"Vücut Kitle İndeksiniz: (VKI): {vki:.2f}")
    print(f"Durumunuz: {kategori}")

    print("\nGenel VKI Aralıkları: ")
    print(" - DURUM<=18.4 ve altı : Zayıf")
    print(" - 18.5<=DURUM<=24.9 : Normal")
    print(" - 25<=DURUM <=29.9  : Fazla Kilolu")
    print(" - DURUM>=30 ve üzeri : Obezsiniz Doktora gidiniz.")


# Kullanıcıya tekrar sormak
def kullanici_sor():
    """
    :return:
    Kulalnıcıdan yeni bir hesaplama yapmak istiyorusa tekrardan hesaplasın
    """
    cevap = input("\nYeni bir hesaplama yapmak ister misiniz ? (e/h)").strip().lower()
    return cevap =="e"


# Sonuç
def main():
    print("==================================================")
    print(" Vücut Kitle İndeksini Hesaplama (VKI)")
    print("==================================================")

    while True:
        # 1. Kullanıcıdan Kilo ve boy
        kilo,boy= kullanidan_deger_al()

        # 2. VKI hesapla
        vki= hesapla_vki(kilo,boy)

        # 3.Kategori Bul
        kategori = vki_kategori(vki)

        # 4. Sonuçları yazdır (kilo,boy,vki,kategori)
        sonucu_yazdir(kilo,boy,vki,kategori)

        # 5. Tekrar yapmak ister misiniz ?
        if not kullanici_sor():
            print("\nProgram sonlandırılıyor. Sağlıklı güzel günler dileriz.❤️🎁")
            break

# Program doğrudan çalıştırıldığında buradan başla
if __name__ == "__main__":
     main()