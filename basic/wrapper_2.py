def dictecevir(fonksiyon):
    def wrapla(*args,**kwargs):

        data = fonksiyon(*args,**kwargs)
        return {
            'sonuc':True,
            'data':data
        }
    return  wrapla

@dictecevir
def toplama(a,b):
    return a+b

@dictecevir
def yaziyaz(yazi):
    return "Yazımız {}  ".format(yazi)

@dictecevir
def dictver(a,b):
    return {
        "birinc":a,
        "ikinci":b
    }

print(toplama(3,5))
print(yaziyaz("Merhaba"))
print(dictver("Merhaba",'Mustafa'))