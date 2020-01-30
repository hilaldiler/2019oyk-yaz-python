class Human:
    name = ''
    surname = ''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
    def __int__(self):
        return 5
    def __setattr__(self, key, value):
        self.__dict__.update({key:value})
        print(key,value)

    def __getattr__(self, item):
        if self.__dict__.get(item) is None:
            return 'Böyle bir şey yok '
        return self.__dict__.get(item)
hilal = Human('Hilal', 'Diler')
print(type(hilal))
test = str(hilal)
print("{} class bunu dondu".format(hilal))
print(hilal.name)
print(int(hilal))

hilal.deneme = 'value'
hilal.pony = 'value'
print(hilal.deneme)

print(hilal.__dict__)
print(hilal.tango)