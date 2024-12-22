# 2. Գրել, ծրագիր որը․
#    - կունենա սահմանված list որի մեջ կլինեն միայն int արժեքներ,
#      օրինակ` num_list = [13, 65, 77, 52, 10, 11, 98, 8, 6, 42, 52],
#    - կտպի մի տողում զույգ թվերը, հաջորդ տողում կենտ թվերը,
#      օրինակ` Even Numbers: [52, 10, 98, 8, 6, 42, 52],
#              Odd Numbers: [13, 65, 77, 11]:


num_list = [13, 65, 77, 52, 10, 11, 98, 8, 6, 42, 52]
evens = []
odds = []
for i in num_list:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print("even numbers", evens)
print("odds numbers", odds)
#test1

