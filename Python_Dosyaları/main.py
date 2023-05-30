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
    print(insan_nesne_1, end="\n------------------------\n")
    print(insan_nesne_2, end="\n------------------------\n")

    # İşsiz sınıfına ait nesnelerin bilgileri
    print("\n* * * İşsiz Sınıfına Ait Nesne Bilgileri * * *")
    print(issiz_nesne_1, end="\n------------------------\n")
    print(issiz_nesne_2, end="\n------------------------\n")
    print(issiz_nesne_3, end="\n------------------------\n")

    # Çalışan sınıfına ait nesnelerin bilgileri
    print("\n* * * Çalışan Sınıfına Ait Nesne Bilgileri * * *")
    print(calisan_nesne_1, end="\n------------------------\n")
    print(calisan_nesne_2, end="\n------------------------\n")
    print(calisan_nesne_3, end="\n------------------------\n")

    # Mavi Yaka sınıfına ait nesnelerin bilgileri
    print("\n* * * Mavi Yaka Sınıfına Ait Nesne Bilgileri * * *")
    print(mavi_yaka_nesne_1, end="\n------------------------\n")
    print(mavi_yaka_nesne_2, end="\n------------------------\n")
    print(mavi_yaka_nesne_3, end="\n------------------------\n")

    # Beyaz Yaka sınıfına ait nesnelerin bilgileri
    print("\n* * * Beyaz Yaka Sınıfına Ait Nesne Bilgileri * * *")
    print(beyaz_yaka_nesne_1, end="\n------------------------\n")
    print(beyaz_yaka_nesne_2, end="\n------------------------\n")
    print(beyaz_yaka_nesne_3, end="\n------------------------\n")

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
                    "Tecrübe(Yıl)": [int(calisan_nesne_1.get_tecrube_ay()/12),
                                     int(calisan_nesne_2.get_tecrube_ay()/12),
                                     int(calisan_nesne_3.get_tecrube_ay()/12),
                                     int(mavi_yaka_nesne_1.get_tecrube_ay()/12),
                                     int(mavi_yaka_nesne_2.get_tecrube_ay()/12),
                                     int(mavi_yaka_nesne_3.get_tecrube_ay()/12),
                                     int(beyaz_yaka_nesne_1.get_tecrube_ay()/12),
                                     int(beyaz_yaka_nesne_2.get_tecrube_ay()/12),
                                     int(beyaz_yaka_nesne_3.get_tecrube_ay()/12)],

                    # Dictionary'e nesnelerin maaş bilgilerini atayan kısım
                    "Maaş": [calisan_nesne_1.get_maas(), calisan_nesne_2.get_maas(),
                             calisan_nesne_3.get_maas(), mavi_yaka_nesne_1.get_maas(),
                             mavi_yaka_nesne_2.get_maas(), mavi_yaka_nesne_3.get_maas(),
                             beyaz_yaka_nesne_1.get_maas(), beyaz_yaka_nesne_2.get_maas(),
                             beyaz_yaka_nesne_3.get_maas()],

                    # Dictionary'e nesnelerin yıpranma payı bilgilerini atayan kısım
                    "Yıpranma Payı": [0, 0,
                                      0, mavi_yaka_nesne_1.get_yipranma_payi(),
                                      mavi_yaka_nesne_2.get_yipranma_payi(), mavi_yaka_nesne_3.get_yipranma_payi(),
                                      0, 0,
                                      0],

                    # Dictionary'e nesnelerin teşvik primi bilgilerini atayan kısım
                    "Teşvik Primi": [0, 0,
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

    # Çalışan, Mavi Yaka ve Beyaz Yaka sınıflarına ait
    # Nesne bilgilerinin Dictionary'den alınıp
    # DataFrame'e atandığı kısım
    dataframe = pandas.DataFrame(data=dictionary)

    # İSTENİLEN DATAFRAME İŞLEMLERİ KISMI
    # 1 - Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş
    # Ortalamalarını her grup için hesaplayıp yazdıran bölüm

    # Ortalamaların ve birey sayısının tutulacağı sözlüklerin oluşturulduğu kısım
    ortalama_tecrube = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}
    ortalama_yeni_maas = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}
    birey_sayisi = {"Çalışan": 0, "Mavi Yaka": 0, "Beyaz Yaka": 0}

    # Değerlerin alınıp sözlüklere atandığı kısım
    try:
        for i in range(len(dataframe)):
            # Çalışan statüsü mü diye kontrol eden kısım
            if dataframe.iloc[i, 0] == "Çalışan":
                ortalama_tecrube["Çalışan"] += dataframe.iloc[i, 8]
                ortalama_yeni_maas["Çalışan"] += dataframe.iloc[i, 12]
                birey_sayisi["Çalışan"] += 1

            # Mavi Yaka statüsü mü diye kontrol eden kısım
            elif dataframe.iloc[i, 0] == "Mavi Yaka":
                ortalama_tecrube["Mavi Yaka"] += dataframe.iloc[i, 8]
                ortalama_yeni_maas["Mavi Yaka"] += dataframe.iloc[i, 12]
                birey_sayisi["Mavi Yaka"] += 1

            # Beyaz Yaka statüsü mü diye kontrol eden kısım
            elif dataframe.iloc[i, 0] == "Beyaz Yaka":
                ortalama_tecrube["Beyaz Yaka"] += dataframe.iloc[i, 8]
                ortalama_yeni_maas["Beyaz Yaka"] += dataframe.iloc[i, 12]
                birey_sayisi["Beyaz Yaka"] += 1
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # Değerlerin ortalamasının hesaplamasının yapıldığı kısım
    # Çalışanların ortalamalarını hesaplayan kısım
    try:
        ortalama_tecrube["Çalışan"] = ortalama_tecrube["Çalışan"] / birey_sayisi["Çalışan"]
        ortalama_yeni_maas["Çalışan"] = ortalama_yeni_maas["Çalışan"] / birey_sayisi["Çalışan"]

        # Mavi Yakalıların ortalamalarını hesaplayan kısım
        ortalama_tecrube["Mavi Yaka"] = ortalama_tecrube["Mavi Yaka"] / birey_sayisi["Mavi Yaka"]
        ortalama_yeni_maas["Mavi Yaka"] = ortalama_yeni_maas["Mavi Yaka"] / birey_sayisi["Mavi Yaka"]

        # Beyaz Yakalıların ortalamalarını hesaplayan kısım
        ortalama_tecrube["Beyaz Yaka"] = ortalama_tecrube["Beyaz Yaka"] / birey_sayisi["Beyaz Yaka"]
        ortalama_yeni_maas["Beyaz Yaka"] = ortalama_yeni_maas["Beyaz Yaka"] / birey_sayisi["Beyaz Yaka"]
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # Ortalamaları ekrana yazdıran kısım
    statu_listesi = ("Çalışan", "Mavi Yaka", "Beyaz Yaka")
    print("\n\n* * * STATÜ ORTALAMALARI * * *")
    try:
        for i in statu_listesi:
            print(f"\n----{i} Statülü Bireylerin----"
                  f"\nOrtalama Tecrübesi = {ortalama_tecrube[i]:.2f} Yıl"
                  f"\nOrtalama Yeni Maaşı = {ortalama_yeni_maas[i]:.2f} TL")
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # 2 - Çalışan, mavi yaka ve beyaz yaka statülü bireylerden
    # 15000 TL üzeri maaş alanların toplam sayısını bulan ve yazdıran kısım
    on_bes_bin_uzeri_maas_alan_sayisi = 0
    try:
        for i in range(len(dataframe)):
            if dataframe.iloc[i, 9] > 15000:
                on_bes_bin_uzeri_maas_alan_sayisi += 1
        print(f"\n\nMAAŞI 15000TL ÜZERİ OLAN BİREY SAYISI = {on_bes_bin_uzeri_maas_alan_sayisi}")
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # 3 - DataFrame’in yeni maaşa göre küçükten büyüğe doğru
    # Sıralanmış halini yazdıran kısım
    try:
        sirali_dataframe = dataframe.sort_values("Yeni Maaş", ascending=True)
        print("\n\n----------DATAFRAME'İN YENİ MAAŞA GÖRE KÜÇÜKTEN BÜYÜĞE DOĞRU SIRALANMIŞ HALİ----------\n")
        print(sirali_dataframe.to_string())
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # 4 - Tecrübesi 3 seneden fazla olan Beyaz yakalıların
    # Bulunmasını ve yazdırılmasını sağlayan kısım
    uc_sene_ve_beyaz_yaka = []
    try:
        for i in range(len(dataframe)):
            if dataframe.iloc[i, 8] > 3 and dataframe.iloc[i, 0] == "Beyaz Yaka":
                uc_sene_ve_beyaz_yaka.append(i)
        print("\n\n--------TECRÜBESİ 3 SENEDEN FAZLA OLAN BEYAZ YAKALILAR--------")
        sira = 1
        for i in uc_sene_ve_beyaz_yaka:
            print(f"{sira}. "
                  f"{dataframe.loc[i][2]} "
                  f"{dataframe.loc[i][3]}")
            sira += 1
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # 5 - Yeni maaşı 10000 TL üzerinde olanlardan 2-5 satır arası olanları, tc_no ve yeni_maaş
    # Sütunlarını göstererek yazdıran kısım
    print("\n\n--------YENİ MAAŞI 10000TL ÜZERİ VE SIRASI 2-5 ARASI OLANLAR--------")
    try:
        for i in range(len(dataframe)):
            if dataframe.iloc[i, 12] > 10000 and 2 <= i <= 5:
                bilgiler = dataframe.iloc[i, 1:13:11]
                print(f"Sıra No = {i}\n"
                      f"{bilgiler.to_string()}\n")
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")

    # 6 - Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame
    # Elde edip yazdıran kısım
    print("\n\n--------SADECE AD, SOYAD, SEKTÖR VE YENİ MAAŞI İÇEREN YENİ DATAFRAME--------")
    try:
        yeni_dataframe = dataframe[["Ad", "Soyad", "Sektör", "Yeni Maaş"]].copy()
        print(yeni_dataframe.to_string())
    except Exception as exception:
        print(f"HATA! Hata sebebi: {exception}")


if __name__ == "__main__":
    main()
