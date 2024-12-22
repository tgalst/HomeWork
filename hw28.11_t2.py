# 2. Գրել ֆունկցիա, որը․
#    - կունենա մեկ արգումենտ, որը կլինի դրական ամբողջ թիվ,
#    - եթե թվի թվանշանների քանակը զույգ է, կստուգի արդյոք թվի առաջին կեսի թվանշանների գումարը հավասար է երկրորդ կեսի թվանշանների գումարին, թե ոչ,
#    - եթե թվի թվանշանների քանակը կենտ է, կստուգի նախորդ պայմանի ճշտությունը, ապա կստուգի նաև մեջտեղի թվանշանի զույգ և կենտ լինելը,
#      եթե զույգ է, կտպի True, եթե կենտ՝ False,
#    օրինակ՝ 1238 -> False, քանի որ 1+2 != 3+8
#            1845 -> True, քանի որ 1+8 = 4+5
#            18545 -> False, քանի որ 1+8 = 4+5 և 5-կենտ է,
#            48257 -> True, քանի որ 4+8 = 5+7 և 2-զույգ է։



# mer grac

def my_func(num:int):
    if num < 0:
        print('argument must be > 0')
        return
    num_to_str = str(num)
    l = len(num_to_str)
    first_half = 0
    second_half = 0
    if l % 2 == 0:
        half_len = int(l/2)
        for i in range(half_len):
            first_half = first_half + int(num_to_str[i])
            second_half = second_half + int(num_to_str[half_len + i])
    else:
        half_len = int((l - 1) / 2)
        for i in range(half_len):
            first_half = first_half + int(num_to_str[i])
            second_half = second_half + int(num_to_str[half_len + 1 + i])
        print("is middle even?", int(num_to_str[half_len]) % 2 == 0)
    print('is first half equal to second half?', first_half == second_half)

my_func(35571)