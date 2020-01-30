names= ["Alper", "Melda", "Ferdi",
          "Sinem","Oguzhan","Zehra","Emre","Ugurcan",
          "Dogukan","Hilal","Diren","Mehmet","Mertcan","Ali",
          "Ferhat","Cem","Gokhan","Sezer","Nur","Busra","Pelin",
          "Kadir","Muhammet","Ture","Burcu","Damla"
        ]
#isimler.remove("Alper")
#print(isimler.count("Alper"))
print(names.pop(2))
print(names)
#isimler.append(2)
print(names.index("Kadir", 0, 25))
names2=names.copy()
new = ['Tonny', 'İsmail']
#isimler2.append(yenigelenler)
#print(isimler2)
#print(isimler2)
#isimler2.extend(yenigelenler)
#print(isimler)
#isimler2.clear()
#print(isimler2)
#isimler2.append("asd")

#tersten yazdırır.
names2.reverse()
print(names2)
names2.insert(5, "Diren")
print(names2)

student={"name": "Hilal", "surname": "Diler"}
print(student.get("name"))
print(student["name"])

print(student.get("age", 0))
#print(ogrenci["yas"])
student.update({"age": "22"})
print(student)
student["age"]=23
print(student)
print(student.items())
for key,value in student.items():
    print(key,value)


student={"number":206, "notes":[
    {"lesson":"math","not":100},
    {"lesson":"science","not":0}
    ]
         }
print(student.keys())
print(student.fromkeys(["notes"]))
#ogrenci=dict.fromkeys(["notlar","numara","isim"],"girilmemis")
print(student)

for value in student.values():
    print(value)

student.pop("notes")
print(student)
