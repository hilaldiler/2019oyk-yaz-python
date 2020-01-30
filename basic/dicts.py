degerler = {
    'isim':'Ali',
    'yaş':36,
    "hobiler":['kamp','aff','frp'],
    "özelliker": {
        'saç':'siyah',
        'sakal':"yeşil"
    }
}
print(degerler.get('isim'))
print(degerler.get('özelliker'))
print(degerler.get('özelliker').get('sakal'))
ozellikler = degerler.get('özelliker')
print(ozellikler.get('sakal'))
print(ozellikler.get('sakallimi'))
print(ozellikler.get('sakallimi','Evet'))
print(ozellikler.get('sakal','Evet'))
print(ozellikler.get('sakallimi',{}))
print(ozellikler.get('sakallimi',{"uzunmu":"evet"}).get('uzunmu','Hayır'))
print(degerler.get('hobiler'))
print(degerler.get('hobiler')[0])
degerler.get('hobiler')[0] = 'test'
degerler.get('hobiler')[0] = 'test'
print(degerler.get('hobiler')[0])
degerler.get('hobiler').append('deneme')
print(degerler.get('hobiler'))
degerler.get('hobiler').append({'deneme':1})
print(degerler.get('hobiler'))
degerler.get('özelliker').update(
    {'sakal':"sarı", 'göz':'KAHVERENGİ'}
)
print(degerler)