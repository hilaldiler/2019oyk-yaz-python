class Actor:

    can = 100
    enerji = 100
    guc = 1
    zeka = 1
    ceviklik = 1
    kullanılabilir_yetenek_puani = 0
    deneyim = 0
    deneyim_seviyesi = 1
    canta = []
    giysiler = []
    para = 3
    yasiyormu = True

    def iyilestirme(self, kaccan):
        if self.can + kaccan >= 100:
            self.can = 100
        else:
            self.can += kaccan
    def enerji_doldur(self, kacenerji):
        if self.can + kacenerji >= 100:
            self.can = 100
        else:
            self.can += kacenerji

    def damage(self, kaccan):
        if self.can - kaccan > 0:
            self.can -= kaccan
        else:
            self.yasiyormu = False