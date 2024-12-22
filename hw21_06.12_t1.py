# 1․ Գրել ծրագիր, որը․
#    - կհաշվի դրական ամբողջ թվի ֆակտորիալը օգտագործելով ռեկուրսիա:

def factorial1(num):
    if num == 0:
        return 1
    return num * factorial1(num - 1)

print(factorial1(5))