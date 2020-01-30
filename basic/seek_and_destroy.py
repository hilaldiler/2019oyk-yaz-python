def read_file(file_name, howmanybtes, seekposition):
    with open(file_name) as file:

        #İstedigimiz kadar bizi ileriye atar.
        file.seek(seekposition)
    return  file.read(howmanybtes)

#5 byte ileri sararak okur.5.byte dan baslar ve 1029 a kadar okur.
print(read_file("data.txt", 1024, 5))

#0.byte dan itibarek okur yani 5 byte  geri sarmıs oldu.
print(read_file("data.txt", 1024, 0))