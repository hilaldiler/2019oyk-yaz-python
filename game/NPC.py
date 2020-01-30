#Non Playable Character
from Actor import Actor



class Satici(Actor):
    def etkilesim(self, secenek):
        urunler = [{"isim": "Ekmek", "Fiyat":1, "deger":0},
                    {"isim": "Ekmek", "Fiyat": 1, "deger": 0},
                    {"isim": "Balık", "Fiyat": 1, "deger": 0},
                    {"isim": "Et", "Fiyat": 1, "deger": 0},
                    {"isim":"Süt", "Fiyat": 1, "deger": 0},
                    {"isim": "Kahve", "Fiyat": 1, "deger": 0}
                  ]
        if secenek == 0:
            urun_listesi = []
            urunid = 0
            for urun in self.urunler:
                urunid += 1
            print("{} ({} Altın) ".format(
                urun.get("isim"), urun.get("fiyat")
            ))
        else:
            pass


class Demirci(Satici):
    urunler = [{"isim": "Balta", "Fiyat": 1, "deger": 0},
        {"isim": "Ekmek", "Fiyat": 1, "deger": 0},
        {"isim": "Balık", "Fiyat": 1, "deger": 0},
        {"isim": "Et", "Fiyat": 1, "deger": 0},
        {"isim": "Süt", "Fiyat": 1, "deger": 0},
        {"isim": "Kahve", "Fiyat": 1, "deger": 0},
    ]