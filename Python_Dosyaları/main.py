import Insan
import Issiz
import Calisan
import MaviYaka
import BeyazYaka


def main():
    # Nesnelerin oluşturulduğu kısım
    # İnsan sınıfına ait nesneler
    insan_nesne_1 = Insan.Insan(10013168314, "Selim Eren", "White", 18, "Erkek", "Türk")
    insan_nesne_2 = Insan.Insan(23791307912, "Umut Şeref", "Varga", 20, "Erkek", "Türk")

    # İşsiz sınıfına ait nesneler
    issiz_nesne_1 = Issiz.Issiz(24697482015, "Yusuf", "Salamanca", 21, "Erkek", "İspanyol", 5, 3, 0)
    issiz_nesne_2 = Issiz.Issiz(48201672483, "Mehmet Igor", "Dobarov", 23, "Erkek", "Rus", 5, 0, 3)
    issiz_nesne_3 = Issiz.Issiz(28604627451, "Beyza", "Karakoç", 19, "Kadın", "Türk", 4, 1, 0)

    # Çalışan sınıfına ait nesneler
    calisan_nesne_1 = Calisan.Calisan(15928406635, "Hüseyin", "Garcia", 18, "Erkek", "Fransız", "inşaat", 29, 9000)
    calisan_nesne_2 = Calisan.Calisan(73025904169, "Sofia", "Vetra", 20, "Kadın", "İspanyol", "Diğer", 35, 12000)
    calisan_nesne_3 = Calisan.Calisan(15823947025, "Vittoria", "Morel", 24, "Kadın", "Fransız", "Teknoloji", 45, 14000)

    # Mavi Yaka sınıfına ait nesneler
    mavi_yaka_nesne_1 = MaviYaka.MaviYaka(75331020462, "Arda", "Çoban", 32, "Erkek", "Türk", "Muhasebe", 57, 23000, 0.4)
    mavi_yaka_nesne_2 = MaviYaka.MaviYaka(49177620539, "Nur", "Güler", 25, "Kadın", "Türk", "Teknoloji", 32, 17000, 0.2)
    mavi_yaka_nesne_3 = MaviYaka.MaviYaka(64153045957, "Sinem", "Ayaz", 22, "Kadın", "Türk", "Muhasebe", 27, 12000, 0.3)

    # Beyaz Yaka sınıfına ait nesneler
    beyaz_yaka_nesne_1 = BeyazYaka.BeyazYaka(38234957268, "Gus", "Fring", 40, "Erkek", "Şilili", "Diğer", 80, 24000, 3000)
    beyaz_yaka_nesne_2 = BeyazYaka.BeyazYaka(29063742415, "Michael", "Ehrmantraut", 60, "Erkek", "Amerikan", "Diğer", 56, 20000, 2000)
    beyaz_yaka_nesne_3 = BeyazYaka.BeyazYaka(52587415063, "Jessie", "Pinkman", 25, "Erkek", "Amerikan", "Muhasebe", 30, 12000, 1500)

    # Nesne bilgilerinin ekrana yazdırıldığı kısım
    # İnsan sınıfına ait nesnelerin bilgileri
    print("\n* * * İnsan Sınıfına Ait Nesne Bilgileri * * *")
    print(insan_nesne_1, end="\n\n")
    print(insan_nesne_2, end="\n\n")

    # İşsiz sınıfına ait nesnelerin bilgileri
    print("\n* * * İşsiz Sınıfına Ait Nesne Bilgileri * * *")
    print(issiz_nesne_1, end="\n\n")
    print(issiz_nesne_2, end="\n\n")
    print(issiz_nesne_3, end="\n\n")

    # Çalışan sınıfına ait nesnelerin bilgileri
    print("\n* * * Çalışan Sınıfına Ait Nesne Bilgileri * * *")
    print(calisan_nesne_1, end="\n\n")
    print(calisan_nesne_2, end="\n\n")
    print(calisan_nesne_3, end="\n\n")

    # Mavi Yaka sınıfına ait nesnelerin bilgileri
    print("\n* * * Mavi Yaka Sınıfına Ait Nesne Bilgileri * * *")
    print(mavi_yaka_nesne_1, end="\n\n")
    print(mavi_yaka_nesne_2, end="\n\n")
    print(mavi_yaka_nesne_3, end="\n\n")

    # Beyaz Yaka sınıfına ait nesnelerin bilgileri
    print("\n* * * Beyaz Yaka Sınıfına Ait Nesne Bilgileri * * *")
    print(beyaz_yaka_nesne_1, end="\n\n")
    print(beyaz_yaka_nesne_2, end="\n\n")
    print(beyaz_yaka_nesne_3, end="\n\n")


if __name__ == "__main__":
    main()