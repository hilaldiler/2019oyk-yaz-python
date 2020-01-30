from functools import reduce
from math import radians

sub = lambda x, y: y - x
print(sub(4, 9))


def sonucbul(number):
    return number + 13


numbers = [1, 3, 4, 5, 9, 1, 12]

#tupple elemanlarının uzunluk sayısını bulur.
result = map(sonucbul, numbers)
#okunabilirlik için haritayı bir listeye dönüştürün.
print(list(result))

result = map(lambda x: x + 13, numbers)
print(list(result))

data = []
for i in numbers:
    sum = lambda x: x + 13
    data.append(sum(i))
numbers = [1, 3, 4, 5, 9, 1, 12]

#(((1 + 2) + 3) + 4) => 10
def reducenedir(sonuc, deger):
    print(sonuc, deger)
    data_result = sonuc + deger
    print(data_result)
    print("----------")
    return data_result
print(reduce(reducenedir, numbers))


print(list(filter(lambda x:x%2==0, numbers)))

def filtreleme(deger):
    if deger == 12:
        return True
    else:
        return False

print(list(filter(filtreleme, numbers)))