import csv

import requests

url = "https://www.hesapkurdu.com/kredi-faiz-oranlari"
request = requests.get(url)
html = request.content.decode('utf-8').split('<tr class="data-table__row">')

line = ["banka", "ihitiyac_kredisi", "konut_kredisi", "tasit_kredisi"]

with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(line)

while True:
    print("İşlem Seciniz:")
    print("1- Faiz Oranlarını Göster: ")
    print("2- Döviz Kuru Hesapla: ")

    selected = input("Select:")
    if selected == "1":
        with open("data.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for i in html[1:]:
                banka = i.split('<td')[1].split('>')[1].split('<')[0]
                ihtiyac = i.split('<td')[2].split('>')[1].split('<')[0]
                konut = i.split('<td')[3].split('>')[1].split('<')[0]
                tasit = i.split('<td')[4].split('>')[1].split('<')[0]

                api_data = [banka, ihtiyac, konut, tasit]
                writer.writerow(api_data)

        with open("data.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                print(row)

    elif selected == "2":
        liste = []
        data = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml').content.decode("utf-8")
        for i in data.split('<Currency ')[1:]:
            ad = i.split('<Isim')[1].split('>')[1].split("<")[0]
            alis = i.split('<BanknoteBuying')[1].split('>')[1].split("<")[0]
            satis = i.split('<BanknoteSelling')[1].split('>')[1].split("<")[0]
            # print(ad,alis,satis)
            liste.append({"ad": ad, "alis": alis, "satis": satis})
            # print("-"*10)

        with open("doviz.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['ad', 'alis', 'satis'])
            writer.writerows(liste)

        with open("doviz.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['ad', 'alis', 'satis'])
            liste = list(reader)


        def doviz_kuru_hesaplama():
            if secim == 1:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[0].get("alis"))
                    print(miktar / deger)
                if secim2 == "b":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[0].get("satis"))
                    sonuc = miktar * deger
                    print(sonuc)
            if secim == 2:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[3].get("alis"))
                    print(miktar / deger)
                if secim2 == "b":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[3].get("satis"))
                    print(miktar * deger)
            if secim == 3:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[4].get("alis"))
                    print(miktar / deger)
                if secim2 == "b":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[4].get("satis"))
                    print(miktar * deger)
            if secim == 4:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[1].get("alis"))
                    print(miktar / deger)
                if secim2 == "b":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[1].get("satis"))
                    print(miktar * deger)

            if secim == 5:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[2].get("alis"))
                    print(miktar / deger)

                if secim2 == "b":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[2].get("satis"))
                    print(miktar * deger)

            if secim == 6:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[5].get("alis"))
                    print(miktar / deger)
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[5].get("satis"))
                    print(miktar * deger)

            if secim == 7:
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[7].get("alis"))
                    print(miktar / deger)
                if secim2 == "a":
                    miktar = float(input("çevirmek istediğiniz miktarı giriniz"))
                    deger = float(liste[7].get("satis"))
                    print(miktar * deger)


        print("hoşgeldiniz ")
        secim = input(
            "hangi döviz kuruna bakmak istiyorsunuz 1/dolar 2/euro 3/ingiliz sterlini 4/avustralya doları 5/danimarka kronu 6/isviçre frangı 7/kanada doları")
        secim = int(secim)
        secim2 = input("a-alış b-satış")

        doviz_kuru_hesaplama()

    else:
        print("Yanlış Seçim !!!")