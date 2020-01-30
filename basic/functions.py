def write_to_screen():
    print('Merhaba')
    print('Dunya')
write_to_screen()
def say_hello(isim,soyisim=''):
    print('Merhaba {} {}, ben bir fonksiyonum'.format(isim,soyisim))

say_hello('Hilal')
say_hello(soyisim="HÜLAYİM",isim='OĞUZHAN')
say_hello('Furkan','Ahmet')
say_hello('Diren','Aydın')
say_hello('Muhammet','Kahraman')


def hello_everthing(yas,*args,**kwargs):
    print(args)
    print(kwargs)
    print(yas)

hello_everthing(yas=12,isim='Diren',soyisim='Aydin')