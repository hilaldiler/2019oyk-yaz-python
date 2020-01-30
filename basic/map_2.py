
list1 = [1, 2, 3, 4, 5, 444]
list2 = [5, 4, 3, 2, 1, 4]
list3 = [5, 4, 3, 2, 1, 4]

def test(test):

    return " Merhaba {}".format(test)


def test2(test,test2):
    return test + test2

def test3(test,test2,test3):
    return test + test2 + test3

print(list(map(test, list1)))
print(list(map(test2, list1, list2)))
print(list(map(test3, list1, list2, list3)))
print(list(map(lambda x,y:x+y, list1, list3)))

list1 = ["1", "2"]
list2 = [1, 2]
print(list(map(lambda x,y:int(x)+int(y), list1, list2)))
