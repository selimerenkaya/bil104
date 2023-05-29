import Insan
import Issiz
import Calisan
import MaviYaka
import BeyazYaka
import pandas


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
    mavi_yaka_nesne_1 = MaviYaka.MaviYaka(75331020462, "İlker", "Tunç", 32, "Erkek", "Türk", "Muhasebe", 57, 23000, 0.4)
    mavi_yaka_nesne_2 = MaviYaka.MaviYaka(49177620539, "Nur", "Güler", 25, "Kadın", "Türk", "Teknoloji", 32, 17000, 0.2)
    mavi_yaka_nesne_3 = MaviYaka.MaviYaka(64153045957, "Sinem", "Ayaz", 22, "Kadın", "Türk", "Muhasebe", 27, 12000, 0.3)

    # Beyaz Yaka sınıfına ait nesneler
    beyaz_yaka_nesne_1 = BeyazYaka.BeyazYaka(38234957268, "Gustavo", "Fring", 40, "Erkek", "Şilili", "Diğer",
                                             80, 24000, 3000)
    beyaz_yaka_nesne_2 = BeyazYaka.BeyazYaka(29063742415, "Michael", "Ehrmantraut", 60, "Erkek", "Amerikan", "Diğer",
                                             56, 20000, 2000)
    beyaz_yaka_nesne_3 = BeyazYaka.BeyazYaka(52587415063, "Jessie", "Pinkman", 25, "Erkek", "Amerikan", "Muhasebe",
                                             30, 12000, 1500)

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

    # Çalışan, Mavi Yaka ve Beyaz Yaka sınıflarına ait
    # Nesne bilgilerinin DataFrame'e atamak üzere
    # Dictionary'e atandığı kısım
    dictionary = {  # Dictionary'e nesnelerin nesne değer bilgilerini atayan kısım
                    "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan",
                                     "Mavi Yaka", "Mavi Yaka", "Mavi Yaka",
                                     "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],

                    # Dictionary'e nesnelerin TC No bilgilerini atayan kısım
                    "TC No": [calisan_nesne_1.get_tc_no(), calisan_nesne_2.get_tc_no(),
                              calisan_nesne_3.get_tc_no(), mavi_yaka_nesne_1.get_tc_no(),
                              mavi_yaka_nesne_2.get_tc_no(), mavi_yaka_nesne_3.get_tc_no(),
                              beyaz_yaka_nesne_1.get_tc_no(), beyaz_yaka_nesne_2.get_tc_no(),
                              beyaz_yaka_nesne_3.get_tc_no()],

                    # Dictionary'e nesnelerin ad bilgilerini atayan kısım
                    "Ad": [calisan_nesne_1.get_ad(), calisan_nesne_2.get_ad(),
                           calisan_nesne_3.get_ad(), mavi_yaka_nesne_1.get_ad(),
                           mavi_yaka_nesne_2.get_ad(), mavi_yaka_nesne_3.get_ad(),
                           beyaz_yaka_nesne_1.get_ad(), beyaz_yaka_nesne_2.get_ad(),
                           beyaz_yaka_nesne_3.get_ad()],

                    # Dictionary'e nesnelerin soyad bilgilerini atayan kısım
                    "Soyad": [calisan_nesne_1.get_soyad(), calisan_nesne_2.get_soyad(),
                              calisan_nesne_3.get_soyad(), mavi_yaka_nesne_1.get_soyad(),
                              mavi_yaka_nesne_2.get_soyad(), mavi_yaka_nesne_3.get_soyad(),
                              beyaz_yaka_nesne_1.get_soyad(), beyaz_yaka_nesne_2.get_soyad(),
                              beyaz_yaka_nesne_3.get_soyad()],

                    # Dictionary'e nesnelerin yaş bilgilerini atayan kısım
                    "Yaş": [calisan_nesne_1.get_yas(), calisan_nesne_2.get_yas(),
                            calisan_nesne_3.get_yas(), mavi_yaka_nesne_1.get_yas(),
                            mavi_yaka_nesne_2.get_yas(), mavi_yaka_nesne_3.get_yas(),
                            beyaz_yaka_nesne_1.get_yas(), beyaz_yaka_nesne_2.get_yas(),
                            beyaz_yaka_nesne_3.get_yas()],

                    # Dictionary'e nesnelerin cinsiyet bilgilerini atayan kısım
                    "Cinsiyet": [calisan_nesne_1.get_cinsiyet(), calisan_nesne_2.get_cinsiyet(),
                                 calisan_nesne_3.get_cinsiyet(), mavi_yaka_nesne_1.get_cinsiyet(),
                                 mavi_yaka_nesne_2.get_cinsiyet(), mavi_yaka_nesne_3.get_cinsiyet(),
                                 beyaz_yaka_nesne_1.get_cinsiyet(), beyaz_yaka_nesne_2.get_cinsiyet(),
                                 beyaz_yaka_nesne_3.get_cinsiyet()],

                    # Dictionary'e nesnelerin uyruk bilgilerini atayan kısım
                    "Uyruk": [calisan_nesne_1.get_uyruk(), calisan_nesne_2.get_uyruk(),
                              calisan_nesne_3.get_uyruk(), mavi_yaka_nesne_1.get_uyruk(),
                              mavi_yaka_nesne_2.get_uyruk(), mavi_yaka_nesne_3.get_uyruk(),
                              beyaz_yaka_nesne_1.get_uyruk(), beyaz_yaka_nesne_2.get_uyruk(),
                              beyaz_yaka_nesne_3.get_uyruk()],

                    # Dictionary'e nesnelerin sektör bilgilerini atayan kısım
                    "Sektör": [calisan_nesne_1.get_sektor(), calisan_nesne_2.get_sektor(),
                               calisan_nesne_3.get_sektor(), mavi_yaka_nesne_1.get_sektor(),
                               mavi_yaka_nesne_2.get_sektor(), mavi_yaka_nesne_3.get_sektor(),
                               beyaz_yaka_nesne_1.get_sektor(), beyaz_yaka_nesne_2.get_sektor(),
                               beyaz_yaka_nesne_3.get_sektor()],

                    # Dictionary'e nesnelerin tecrübe bilgilerini atayan kısım
                    "Tecrübe": [int(calisan_nesne_1.get_tecrube_ay()/12), int(calisan_nesne_2.get_tecrube_ay()/12),
                                int(calisan_nesne_3.get_tecrube_ay()/12), int(mavi_yaka_nesne_1.get_tecrube_ay()/12),
                                int(mavi_yaka_nesne_2.get_tecrube_ay()/12), int(mavi_yaka_nesne_3.get_tecrube_ay()/12),
                                int(beyaz_yaka_nesne_1.get_tecrube_ay()/12), int(beyaz_yaka_nesne_2.get_tecrube_ay()/12),
                                int(beyaz_yaka_nesne_3.get_tecrube_ay()/12)],

                    # Dictionary'e nesnelerin maaş bilgilerini atayan kısım
                    "Maaş": [calisan_nesne_1.get_maas(), calisan_nesne_2.get_maas(),
                             calisan_nesne_3.get_maas(), mavi_yaka_nesne_1.get_maas(),
                             mavi_yaka_nesne_2.get_maas(), mavi_yaka_nesne_3.get_maas(),
                             beyaz_yaka_nesne_1.get_maas(), beyaz_yaka_nesne_2.get_maas(),
                             beyaz_yaka_nesne_3.get_maas()],

                    # Dictionary'e nesnelerin yıpranma payı bilgilerini atayan kısım
                    "Yıpranma payı": [0, 0,
                                      0, mavi_yaka_nesne_1.get_yipranma_payi(),
                                      mavi_yaka_nesne_2.get_yipranma_payi(), mavi_yaka_nesne_3.get_yipranma_payi(),
                                      0, 0,
                                      0],

                    # Dictionary'e nesnelerin teşvik primi bilgilerini atayan kısım
                    "Teşvik primi": [0, 0,
                                     0, 0,
                                     0, 0,
                                     beyaz_yaka_nesne_1.get_tesvik_primi(), beyaz_yaka_nesne_2.get_tesvik_primi(),
                                     beyaz_yaka_nesne_3.get_tesvik_primi()],

                    # Dictionary'e nesnelerin yeni maaş bilgilerini atayan kısım
                    "Yeni Maaş": [int(calisan_nesne_1.get_yeni_maas()), int(calisan_nesne_2.get_yeni_maas()),
                                  int(calisan_nesne_3.get_yeni_maas()), int(mavi_yaka_nesne_1.get_yeni_maas()),
                                  int(mavi_yaka_nesne_2.get_yeni_maas()), int(mavi_yaka_nesne_3.get_yeni_maas()),
                                  int(beyaz_yaka_nesne_1.get_yeni_maas()), int(beyaz_yaka_nesne_2.get_yeni_maas()),
                                  int(beyaz_yaka_nesne_3.get_yeni_maas())],
                  }


if __name__ == "__main__":
    main()
