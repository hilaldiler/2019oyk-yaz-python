import random
from time import sleep
import os
isimler = ["Alper","Melda","Ferdi",
          "Sinem","Oguzhan","Zehra","Emre","Ugurcan",
          "Dogukan","Hilal","Diren","Mehmet","Mertcan","Ali",
          "Ferhat","Cem","Gokhan","Sezer","Nur","Busra","Pelin",
          "Kadir","Muhammet","Ture","Burcu","Damla"
          ]


for i in range(random.randint(10,30)):
    os.system('clear')
    print(random.choice(isimler))
    sleep(0.05*i)
