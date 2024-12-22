# 2. Գրել ծրագիր, որը․
#    - կտպի tuple-ներից բաղկացած list-ի բոլոր էլեմենտների գումարը,
#    օրինակ՝ list_1 = [(1, 2, 6), (2, 3, -6), [3, 4], (2, -6, 2, 8), 6, 2.7],
#            արդյունքը պետք է լինի՝
#            29.7:

list_1 = [(1, 2, 6), (2, 3, -6), [3, 4], (2, -6, 2, 8), 6, 2.7]
total_sum = 0
for item in list_1:
    if (type(item) == int or type(item) == float):
        total_sum += item
    elif (type(item) == tuple or type(item) == list):
        total_sum += sum(item)
print(total_sum)
