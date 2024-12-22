from symbol import return_stmt
#
# 1․ Գրել ծրագիր որը․
#    - կունենա ֆունկցիա is_prime անունով, որը կստանա ամբողջ թիվ
#      և կվերադարձնի True եթե թիվը պարզ է, հակառակ դեպքում կվերադարձնի False,
#    - օգտագործելով is_prime և filter ֆունկցաները` ստանալ 2-ից մինչև 1000 միջակայքում
#      գտնվող պարզ թվերի list,
#    - տպել տվյալ list-ը։

def is_prime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

print(list(filter(is_prime, range(2, 1001))))
