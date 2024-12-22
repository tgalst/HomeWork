# 3․ Գրել ծրագիր, որը․
#    - կունենա թվերից բաղկացած list,
#    - list-ը կբաժանի 2 list-երի այնպես,
#      որ առաջին list-ում կլինեն նախնական list-ի առաջին, երրորդ, հինգերորդ և այլն էլեմենտները,
#      իսկ երկրորդ list-ում՝ երկրորդ, չորորդ, վեցերորդ և այլն էլեմենտները,
#    - կհաշվի և tuple-ով կտպի այդ list-երի միջին թվաբանականները,
#    օրինակ՝ list_1 = [50, 60, 60, 45, 70]
#    պետք է ստացվի՝ (60, 52.5):

def divided_list(list_1 = [50, 60, 60, 45, 70]):
    list_even = []
    list_odd = []
    for i in range(len(list_1)):
        if i % 2 == 0:
            list_even.append(list_1[i])
        else:
            list_odd.append(list_1[i])

    return sum(list_even)/len(list_even), sum(list_odd)/len(list_odd)

print(divided_list())
