import Insan


class Calisan(Insan.Insan):
    # Nesne oluşturulduğunda değişken ataması yapan metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        sektor_liste = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        while sektor.lower() not in sektor_liste:
            print("Geçersiz bir sektör girdiniz.")
            sektor = input("Geçerli bir sektör giriniz.\n"
                           "Seçenekler = teknoloji, muhasebe, inşaat, diğer\n"
                           "Sektör = ")
        self.__sektor = sektor
        self.__tecrube_ay = tecrube_ay
        self.__maas = maas
        self.__yeni_maas = "Belirlenmedi"
        self.__zam_orani_oneri = 0
        self.__hakedilen_zam = 0

    # Insan Class'ından alınan kalıtsal Get/Set metotları
    # Issiz Class'ı için de geçerli olduğundan
    # o metotları tanımlamaya gerek yoktur

    # Private değişkenlerin Get/Set metotları
    # 1 - sektor değişkeni için Get/Set metotları
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    # 2 - tecrube_ay değişkeni için Get/Set metotları
    def get_tecrube_ay(self):
        return self.__tecrube_ay

    def set_tecrube_ay(self, tecrube_ay):
        self.__tecrube_ay = tecrube_ay

    # 3 - maas değişkeni için Get/Set metotları
    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    # 4 - yeni_maas değişkeni için Get/Set metotları
    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    # 5 - zam_orani_oneri değişkeni için Get/Set metotları
    def get_zam_orani_oneri(self):
        return self.__zam_orani_oneri

    def set_zam_orani_oneri(self, zam_orani_oneri):
        self.__zam_orani_oneri = zam_orani_oneri

    # 6 - hakedilen_zam değişkeni için Get/Set metotları
    def get_hakedilen_zam(self):
        return self.__hakedilen_zam

    def set_hakedilen_zam(self, hakedilen_zam):
        self.__hakedilen_zam = hakedilen_zam

    # Çalışanın zam hakkını hesaplayan metot
    def zam_hakki(self):
        try:
            # zam oranı hesaplaması yapan kısım
            if float(self.__tecrube_ay) / 12 < 2:
                self.__zam_orani_oneri = 0
            elif 2 <= float(self.__tecrube_ay) / 12 < 4 and self.__maas < 15000:
                self.__zam_orani_oneri = self.__maas % self.__tecrube_ay
            elif float(self.__tecrube_ay) >= 4 and self.__maas < 25000:
                self.__zam_orani_oneri = (self.__maas % self.__tecrube_ay) / 2

            # zam hakkını hesaplayan kısım
            self.__hakedilen_zam = float(self.__maas * self.__zam_orani_oneri) / 100

            # yeni maaşı hesaplayan kısım
            self.__yeni_maas = self.__maas + self.__hakedilen_zam

            # Yeni maaş, eski maaş ile aynıysa eski maaşın, yeni maaşa atandığı kısım
            if self.__yeni_maas == self.__maas:
                self.__yeni_maas = self.__maas

        except Exception as exception:
            print(f"HATA! Hata sebebi: {exception}")

    # Kullanıcı bilgilerini döndüren metot
    def __str__(self):
        self.zam_hakki()
        return f"Ad = {self.get_ad()}" \
               f"\nSoyad = {self.get_soyad()}" \
               f"\nTecrübe = {self.__tecrube_ay} Ay" \
               f"\nYeni Maaş = {self.get_yeni_maas()}"
