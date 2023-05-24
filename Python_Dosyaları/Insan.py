class Insan:
    # Nesne oluşturulduğunda değişken ataması yapan metot
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    # Private değişkenlerin Get/Set metotları
    # 1 - tc_no değişkeni için Get/Set metotları
    def get_tc_no(self):
        return self.__tc_no

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    # 2 - ad değişkeni için Get/Set metotları
    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    # 3 - soyad değişkeni için Get/Set metotları
    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    # 4 - yas değişkeni için Get/Set metotları
    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    # 5 - cinsiyet değişkeni için Get/Set metotları
    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    # 6 - uyruk değişkeni için Get/Set metotları
    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    # Kullanıcı bilgilerini döndüren metot
    def __str__(self):
        return f"* * * Kullanıcı Bilgileri * * *" \
               f"\nTC No = {self.__tc_no}" \
               f"\nAd = {self.__ad}" \
               f"\nSoyad = {self.__soyad}" \
               f"\nYaş = {self.__yas}" \
               f"\nCinsiyet = {self.__cinsiyet}" \
               f"\nUyruk = {self.__uyruk}"
