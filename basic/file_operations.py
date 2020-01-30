my_file = open('file.txt', 'w')
my_file.write('Hello Python')
my_file.close()

new_my_file = open("file.txt", "a")
new_my_file.write("Bye Python")
new_my_file.close()

read_file  = open("file.txt")
print(read_file.read())
read_file.close()


#Dosya var ise ac ve oku. With blogunun icinden cıkarken dosya otomatik kapanır, close() kullanmamıza gerek yoktur.
with open("new.txt") as file:
    print(file.read())


