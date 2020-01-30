class Hilal(object):
    name = ""
    wear = []
    def __init__(self ,veri):
        self.name = veri
        self.wear = ['Gömlek','Pantolon']
        print('ben oluşturuldum')

    def bye(self):
        print("Bye {}".format(self.name))

    def talk(self):
        print("Merhaba {}".format(self.name))

sinif=Hilal('Hilal')
print(sinif.name)
sinif.talk()
sinif.bye()




