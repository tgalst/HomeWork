# Գրել ծրագիր որը․
#    - կգտնի մուտքագրված թվից մեծ ամենափոքր այն թիվը, որը հանդիսանում է բնական թվի քառակուսի,
#    օրինակ՝
#    num = 5     # result is 9,
#    num = 50    # result is 64,
#    num = 122   # result is 144։

n = int(input("n = "))
tiv = round(n ** 0.5)
if (tiv ** 2 > n):
    print(tiv ** 2)
else:
    print((tiv + 1) ** 2)

