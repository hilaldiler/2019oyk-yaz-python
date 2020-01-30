import os
from math import ceil

def reader(file_name):
    data = []
    with open(file_name) as file:
        opened_data = ""
        #ceil fonk. int bir sayı verir. Sayidan küçük olmayan en küçük tamsayıyı döndürür
        for bytes in range(ceil(os.path.getsize(file_name)/1024)):

            opened_data += file.read(1024)
            if opened_data.find("\\") > -1:
                for i in opened_data.split("\\")[:-1]: #sonuncu index'e kadar getirir.
                    yield i
                opened_data = opened_data.split("\\")[-1]

for i in reader('data.txt'):
    print(i)
