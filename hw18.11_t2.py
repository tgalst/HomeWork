# 2․ Գրել ֆունկցիա, որը․
#    - կընդունի որպես արգումենտ անսահման քանակի թվեր և կվերադարձնի այդ թվերի
#      միջին թվաբանականը, մեդիանը, գումարը, արտադրյալը։
#
from itertools import product


def f1(*args):
    import math
    count = len(args)
    avg = sum(args)/len(args)
    med = sorted(args)[int(count/2)]
    summa = sum(args)
    prod = math.prod(args)
    lst = [avg, med, summa, prod]
    return lst

print(f1(1, 2, 3, 4))