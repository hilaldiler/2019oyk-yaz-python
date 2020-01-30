class Memeli:
    sicakkanli = True
    zeka = True


class Primatlar(Memeli):
    ayakta_durma = True

class Insan(Primatlar):
    dusunebilme = True
    sorgulayabilme = True
    isim = ''
    yetenek = []
    def set_isim(self,ad):
        self.isim = ad

class Kadin(Insan):
    yetenek = ['doğurganlık']

class Erkek(Insan):
    yetenek = ['sperm üretimi']

class Anne(Kadin):
    def sen_kimsin(self):
        print('anne')

class Baba(Erkek):
    def sen_kimsin(self):
        print('baba')

class Cocuk2(Anne, Baba, Kadin):
    def sen_kimsin(self):
        super().sen_kimsin()
        print('çocuk')

class Cocuk3(Baba,Anne, Kadin):
    def sen_kimsin(self):
        super().sen_kimsin()
        print('çocuk')
class Cocuk(Anne, Baba, Kadin):
    def sen_kimsin(self):
        Anne.sen_kimsin(self)
        Baba.sen_kimsin(self)
        print('çocuk')

hilal = Cocuk()
hilal.sen_kimsin()
print("-"*10)
diren = Cocuk2()
diren.sen_kimsin()
print("-"*10)
cevher = Cocuk3()
cevher.sen_kimsin()
