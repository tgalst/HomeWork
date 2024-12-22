# # Գրել ծրագիր որը․
#    - կկարդա count թիվը (input- ի միջոցով),
#    - count քանակով թիվ կկարդա (input- ի միջոցով),
#    - կտպի այդ թվերի միջին թվաբանականը,
#    օրինակ՝ Type count: 4,
#            Type number: 10,
#            Type number: 25,
#            Type number: 35,
#            Type number: 30,
#            Result is 25։

count = int(input("count = "))
summa = 0
for i in range(count):
    n = float(input("n = "))
    summa += n
if (count > 0):
    print(summa / count)
else:
    print("Error")