import Insan


class Issiz(Insan.Insan):
    # Nesne oluşturulduğunda değişken ataması yapan metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, mavi_yaka_yil, beyaz_yaka_yil, yonetici_yil):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__mavi_yaka_yil = mavi_yaka_yil
        self.__beyaz_yaka_yil = beyaz_yaka_yil
        self.__yonetici_yil = yonetici_yil
        self.__uygun_statu = "Belirlenmedi"
        self.__statu_dictionary = {"mavi_yaka": self.__mavi_yaka_yil,
                                   "beyaz_yaka": self.__beyaz_yaka_yil,
                                   "yonetici": self.__yonetici_yil}

    # Insan Class'ından alınan kalıtsal Get/Set metotları
    # Issiz Class'ı için de geçerli olduğundan
    # o metotları tanımlamaya gerek yoktur

    # Private değişkenlerin Get/Set metotları
    # 1 - mavi_yaka_yil değişkeni için Get/Set metotları
    def get_mavi_yaka_yil(self):
        return self.__mavi_yaka_yil

    def set_mavi_yaka_yil(self, mavi_yaka_yil):
        self.__mavi_yaka_yil = mavi_yaka_yil
        # mavi_yaka_yil değişkeninin değeri değiştiği için
        # statu_dictionary dictionarysi içindeki değeri de değiştirilmelidir
        self.__statu_dictionary["mavi_yaka"] = mavi_yaka_yil

    # 2 - beyaz_yaka_yil değişkeni için Get/Set metotları
    def get_beyaz_yaka_yil(self):
        return self.__beyaz_yaka_yil

    def set_beyaz_yaka_yil(self, beyaz_yaka_yil):
        self.__beyaz_yaka_yil = beyaz_yaka_yil
        # beyaz_yaka_yil değişkeninin değeri değiştiği için
        # statu_dictionary dictionarysi içindeki değeri de değiştirilmelidir
        self.__statu_dictionary["beyaz_yaka"] = beyaz_yaka_yil

    # 3 - yonetici_yil değişkeni için Get/Set metotları
    def get_yonetici_yil(self):
        return self.__yonetici_yil

    def set_yonetici_yil(self, yonetici_yil):
        self.__yonetici_yil = yonetici_yil
        # yonetici_yil değişkeninin değeri değiştiği için
        # statu_dictionary dictionarysi içindeki değeri de değiştirilmelidir
        self.__statu_dictionary["yonetici"] = yonetici_yil

    # 4 - uygun_statu değişkeni için Get metotu
    def get_uygun_statu(self):
        return self.__uygun_statu

    # En uygun statünün bulunmasını sağlayan metot
    def statu_bul(self):
        try:
            mavi_yaka_deger = float(self.__statu_dictionary["mavi_yaka"] * 20) / 100
            beyaz_yaka_deger = float(self.__statu_dictionary["beyaz_yaka"] * 35) / 100
            yonetici_deger = float(self.__statu_dictionary["yonetici"] * 45) / 100
            if mavi_yaka_deger > beyaz_yaka_deger and mavi_yaka_deger > yonetici_deger:
                self.__uygun_statu = "Mavi Yaka"
            elif beyaz_yaka_deger > mavi_yaka_deger and beyaz_yaka_deger > yonetici_deger:
                self.__uygun_statu = "Beyaz Yaka"
            elif yonetici_deger > mavi_yaka_deger and yonetici_deger > beyaz_yaka_deger:
                self.__uygun_statu = "Yönetici"
        except Exception as exception:
            print(f"HATA! Hata sebebi: {exception}")

    # Kullanıcı bilgilerini döndüren metot
    def __str__(self):
        self.statu_bul()
        return f"Ad = {self.get_ad()}" \
               f"\nSoyad = {self.get_soyad()}" \
               f"\nEn Uygun Statü = {self.get_uygun_statu()}"


nesne = Issiz(10013168314, "Selim Eren", "Kaya", 18, "Erkek", "Türk", 15, 7, 5)
print(nesne)
