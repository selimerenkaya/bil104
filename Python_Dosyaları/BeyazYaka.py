import Calisan


class BeyazYaka(Calisan.Calisan):
    # Nesne oluşturulduğunda değişken ataması yapan metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)
        self.__tesvik_primi = tesvik_primi

    # Calisan Class'ından alınan kalıtsal Get/Set metotları
    # BeyazYaka Class'ı için de geçerli olduğundan
    # o metotları tanımlamaya gerek yoktur

    # Private değişkenlerin Get/Set metotları
    # 1 - tesvik_primi değişkeni için Get/Set metotları
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # Çalışanın zam hakkını hesaplayan metot
    def zam_hakki(self):
        try:
            zam_onerisi = 0
            if float(self.get_tecrube_ay()) / 12 < 2:
                zam_onerisi = self.__tesvik_primi
            elif 2 <= float(self.get_tecrube_ay()) / 12 < 4 and self.get_maas() < 15000:
                zam_onerisi = ((self.get_maas() % self.get_tecrube_ay()) * 5) + self.__tesvik_primi
            elif float(self.get_tecrube_ay()) / 12 >= 4 and self.get_maas() < 25000:
                zam_onerisi = ((self.get_maas() % self.get_tecrube_ay()) * 4) + self.__tesvik_primi

            # zam hakkını hesaplayan kısım
            hakedilen_zam = zam_onerisi
            self.set_hakedilen_zam(hakedilen_zam)

            # yeni maaşı hesaplayan kısım
            yeni_maas = self.get_maas() + self.get_hakedilen_zam()
            self.set_yeni_maas(yeni_maas)

            # Yeni maaş, eski maaş ile aynıysa eski maaşın, yeni maaşa atandığı kısım
            if self.get_yeni_maas() == self.get_maas():
                self.set_yeni_maas(self.get_maas())

        except Exception as exception:
            print(f"HATA! Hata sebebi: {exception}")

    # Kullanıcı bilgilerini döndüren metot
    def __str__(self):
        self.zam_hakki()
        return f"Ad = {self.get_ad()}" \
               f"\nSoyad = {self.get_soyad()}" \
               f"\nTecrübe = {self.get_tecrube_ay()} Ay" \
               f"\nYeni Maaş = {self.get_yeni_maas():.2f}"
