# # isimler= ["Alper","Melda","Ferdi",
# #           "Sinem","Oguzhan","Zehra","Emre","Ugurcan",
# #           "Dogukan","Hilal","Diren","Mehmet","Mertcan","Ali",
# #           "Ferhat","Cem","Gokhan","Sezer","Nur","Busra","Pelin",
# #           "Kadir","Muhammet","Ture","Burcu","Damla"
# #           ]
# # #isimler.remove("Alper")
# # #print(isimler.count("Alper"))
# # print(isimler.pop(2))
# # print(isimler)
# # #isimler.append(2)
# # print(isimler)
# # print(isimler.index("Kadir",0,25))
# # isimler2=isimler.copy()
# # yenigelenler = ['Tonny','İsmail']
# # #isimler2.append(yenigelenler)
# # #print(isimler2)
# # #print(isimler2)
# # #isimler2.extend(yenigelenler)
# # #print(isimler)
# # #isimler2.clear()
# # #print(isimler2)
# # #isimler2.append("asd")
# # isimler2.reverse()
# # print(isimler2)
# # isimler2.insert(5,"Mustafa")
# # print(isimler2)
# #
# # ogrenci={"isim":"Tolga","soyisim":"ozeren"}
# # print(ogrenci.get("isim"))
# # print(ogrenci["isim"])
# #
# # print(ogrenci.get("yas",0))
# # #print(ogrenci["yas"])
# # ogrenci.update({"yas":"22"})
# # print(ogrenci)
# # ogrenci["yas"]=23
# # print(ogrenci)
# # print(ogrenci.items())
# # for key,value in ogrenci.items():
# #     print(key,value)
# #
# # # for item in ogrenci.items():
# # #     print(item[0],item[1])
# # #
# #
# # makine = {"name": "m80",
# #           "device_status": {
# #               "device_response_status": "run",
# #               "calculated": {
# #                   "device_maintance": 5, "device_error": 0
# #               }
# #           }
# #           }
# # print(makine.get("device_status").get("device_response_status"))
# # print(type(makine.get("device_status")))
#
#
# ogrenci={"numara":206,"notlar":[
#     {"ders_adi":"matematik","not":100},
#     {"ders_adi":"edebiyat","not":0}
#     ]
#     }
# print(ogrenci.keys())
# print(ogrenci.fromkeys(["notlar"]))
# #ogrenci=dict.fromkeys(["notlar","numara","isim"],"girilmemis")
# print(ogrenci)
#
# for value in ogrenci.values():
#     print(value)
#
# ogrenci.pop("notlar")
# print(ogrenci)
