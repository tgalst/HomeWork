# 1. Գրել, ծրագիր որը․
#    - կհաշվի դրական թվի թվանշանների գումարը,
#    օրինակ՝ 1456 ի դեպքում 1+4+5+6 = 16։
#from encodings.punycode import digits

n = "-1234"
if n.isdigit():
    summa = 0
    for i in n:
        summa = summa + int(i)
    print(summa)
else:
    print("wrong number")