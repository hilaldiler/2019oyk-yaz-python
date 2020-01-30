from math import ceil
import os


def read_file(file):
    data = []
    with open("data.txt") as file:
        opened_data = ""

        #ceil bir mat kütüphanesidir. Float degeri bir üst int degere yuvarlar.
        for bytes in range(ceil(os.path.getsize(file)/1024)):

            opened_data += file.read(1024)

            #find, ilk karakterin pozisyonunu döner. Bu kosulda ilk karakterin -1 den büyük yani 0 olması kontrol edilir.
            if opened_data.find("//") > -1:
                for i in opened_data.split("\\")[:-1]:
                    yield i
                    opened_data = opened_data.split("\\")[-1]

                #Hepsini bir kere de okuyup yazmak yerine okudukca verir.
                yield i
            file.read(1024)