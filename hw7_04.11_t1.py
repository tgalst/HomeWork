# 1․ Գրել ծրագիր որը․
#    - կունենա list, օրինակ list_1 = [1, 3, 66, 4, 6, 7, 8, 9, 33, 54, 77, 79],
#    - կտպի list_1 ի ամենամեծ զույգ թիվը (տվյալ օրինակում՝ 66)։


list1 = [1, 3, 66, 4, 6, 7, 8, 9, 33, 54, 77, 79]
    #1-st method
# evens = []
# for i in list1:
#    if i % 2 == 0:
#       evens.append(i)
# print(max(evens))
# 2-nd method
m = 0
for i in list1:
   if i % 2 == 0 and i > m:
      m = i
print(m)




