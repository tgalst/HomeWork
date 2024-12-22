# 4. Գրել ֆունկցիա, որը․
#    - կհաշվի, թե տրված ամբողջ թվերի list-ից քանի քայլով կարելի է ստանալ մոնոտոն աճող թվերից բաղկացած list,
#      մեկ քայլի ընթացքում թույլատրվում է թվերից մեկը մեկով մեծացնել, թվերի տեղերը փոխել չի կարելի,
#    օրինակ՝ [-10, 0, -2, 0] -> 5,
#            [1, 1, 1] -> 3:


def monoton(lst):
    count = 0
    new_lst = lst.copy()
    for i in range(1, len(new_lst)):
        if new_lst[i - 1] >= new_lst[i]:
            count += new_lst[i - 1] + 1 - new_lst[i]
            new_lst[i] = new_lst[i - 1] + 1
    print(f'{lst} -> {new_lst} -> {count}')

lst1 = [-10, 0, -2, 0]
#
lst1 = [1, 1, 1]

monoton(lst1)