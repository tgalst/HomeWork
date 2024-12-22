# 1․ Գրել ֆունկցիա, որը․
#    - կընդունի երկու թիվ որպես պարամետր և կվերադարձնի list-ով այդ թվերի
#      գումարը, տարբերությունը, արտադրյալը, քանորդը։

def f1(a, b):
    lst = []
    lst.append((a + b))
    lst.append((a - b))
    lst.append((a * b))
    lst.append((a / b))
    return lst

print(f1(5, 6))
