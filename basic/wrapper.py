
def supertoplam(func):
    def wrap(*args):
        tumu = sum(args)
        func_return = func(tumu,13)
        return func_return * 13
    return wrap

@supertoplam
def deneme_toplam(a,b):
    return a+b
print(deneme_toplam(1,1,3))