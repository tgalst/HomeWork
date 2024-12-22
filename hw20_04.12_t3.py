# 3․ Գրել ծրագիր, որը․
#    - կունենա dict-երից բաղկացած list,
#    օրինակ՝ user_list = [{'name': 'Arman', 'age': 23},
#                         {'name': 'Bob', 'age': 19},
#                         {'name': 'Anna'}],
#    - կսորտավորի list-ի էլեմենտները ըստ ‘age’-ի sort ֆունկցիային փոխանցելով lambda ֆունկցիա,
#    - կտպի ստացված dictionary-ների list-ը,
#    տվյալ օրինակում պետք է տպի՝ [{'name': 'Anna'},
#                                 {'name': 'Bob', 'age': 19},
#                                 {'name': 'Arman', 'age': 23}]։

user_list = [{'name': 'Arman', 'age': 23},
             {'name': 'Bob', 'age': 19},
             {'name': 'Anna'}]

user_list.sort(key=lambda x: x.get('age') if x.get('age') != None else 0)
print(user_list)