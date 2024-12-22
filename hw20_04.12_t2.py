# 2. Գրել ծրագիր, որը․
#    - կունենա սահմանված երկու list-եր,
#      nums_1 = [1, 2, 3, 5, 7, 8, 9, 10],
#      nums_2 = [1, 2, 4, 8, 9],
#    - կստեղծի list, որը բաղկացած կլինի այն թվերից,
#      որոնք կան և nums_1 ի, և nums_2 ի մեջ օգտագործելով filter և lambda,
#    - կտպի ստացված լիստը,
#    տվյալ օրինակում պետք է տպի՝ [1, 2, 8, 9]։
from importlib.metadata import files

nums_1 = [1, 2, 3, 5, 7, 8, 9, 10]
nums_2 = [1, 2, 4, 8, 9]
#print(set(nums_1) & set(nums_2))
print(list(filter(lambda x: x in nums_2, nums_1)))