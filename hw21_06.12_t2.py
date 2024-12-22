# 2․ Գրել ռեկուրսիվ ֆունկցիա, որը․
#    - կգտնի հետևյալ list-ի բոլոր էլեմենտների գումարը ռեկուրսիայի միջոցով առանց sum ֆունկցիա օգտագործելու,
#    օրինակ՝ [[1], 2, [3, 4], [5, [6, 7]]]

def list_sum(lst):
    s = 0
    for i in lst:
        if type(i) == list:
            s = s + list_sum(i)
        else:
            s = s + i
    return s

lst = [[1], 2, [3, 4], [5, [6, 7]]]
print(list_sum(lst))