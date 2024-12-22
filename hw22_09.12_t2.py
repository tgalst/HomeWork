# 2․ Գրել ռեկուրսիվ ֆունկցիա, որը․
#    - կգտնի բնական թվի թվանշանների գումարը,
#    օրինակ՝ 285 -> 15։

def rec_func(num):
    str_num = str(num)
    if len(str_num) > 1:
        return int(str_num[0]) + rec_func(str_num[1:])
    else:
        return int(str_num)

print(rec_func(285))
