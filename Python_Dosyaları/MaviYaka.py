import Calisan


class MaviYaka(Calisan.Calisan):
    # Nesne oluşturulduğunda değişken ataması yapan metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube_ay, maas)
        self.__yipranma_payi = yipranma_payi

    # Calisan Class'ından alınan kalıtsal Get/Set metotları
    # MaviYaka Class'ı için de geçerli olduğundan
    # o metotları tanımlamaya gerek yoktur

    # Private değişkenlerin Get/Set metotları
    # 1 - yipranma_payi değişkeni için Get/Set metotları
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    # Çalışanın zam hakkını hesaplayan metot
    def zam_hakki(self):
        try:
            zam_orani_oneri = 0
            if float(self.get_tecrube_ay()) / 12 < 2:
                zam_orani_oneri = self.__yipranma_payi * 10
            elif 2 <= float(self.get_tecrube_ay()) / 12 < 4 and self.get_maas() < 15000:
                zam_orani_oneri = (self.get_maas() % self.get_tecrube_ay()) + (self.__yipranma_payi * 10)
            elif float(self.get_tecrube_ay()) / 12 >= 4 and self.get_maas() < 25000:
                zam_orani_oneri = (float(self.get_maas() % self.get_tecrube_ay()) / 3) + (self.__yipranma_payi * 10)
            self.set_zam_orani_oneri(zam_orani_oneri)

            # zam hakkını hesaplayan kısım
            hakedilen_zam = float(self.get_maas() * zam_orani_oneri) / 100
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
