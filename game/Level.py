from game.NPC import Demirci, Satici


class Level:
    oyuncular = []
    yancilar_npc = []
    kotuler = []
    gun = 0
    max_gun = 10

    """
        yon = 0 yukari
        yon = 1 sol
        yon = 2 = sag
        yon = 3 =asagi
    """
    ana_karakter_kare = [0, 0]
    harita_boyutu = [40,40]
    merkez = [0, 0]

    def __init__(self):
        demirci = Demirci()
        demirci.isim = "Haydar"

        satici = Satici()
        satici.isim = "Erşen Küneri"
        self.yancilar_npc = [
            {"x": 1, "y": 0, "kim": demirci},
            {"x": 1, "y": 1, "kim": demirci}
        ]

    def ilerle(self, kackere = 1, yon = 0):
        ""

    def vurma(self, kim, kime):
        ""

    def etkilesim(self, secim):
        ""



