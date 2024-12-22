# 3․ Գրել հետևյալ ծրագիրը․
#    - տրված բառարանը բաղկացած է տրանսպորտային միջոցներից և դրանց քաշից՝ կիլոգրամներով,
#    օրինակ՝ dict_1={"Sedan": 1500, "SUV": 2000,
#                    "Pickup": 2500, "Minivan": 1600,
#                    "Van": 2400, "Semi": 13600,
#                    "Bicycle": 12, "Motorcycle": 110},
#    - մեկ տողով կառուցեք 2 տոննայից ցածր և հավասար քաշ ունեցող մեքենաների անունների
#      ցուցակը որպես list՝ բոլորի անունները մեծատառ դարձնելով,
#    - տվյալ օրինակի դեպքում կտպի`
#      ['SEDAN', 'SUV', 'MINIVAN', 'BICYCLE', 'MOTORCYCLE']։

dict_1 = {"Sedan": 1500, "SUV": 2000,
          "Pickup": 2500, "Minivan": 1600,
          "Van": 2400, "Semi": 13600,
          "Bicycle": 12, "Motorcycle": 110}
lst = []
for key in dict_1:
    val = dict_1[key]
    if val <= 2000:
        lst.append(key.upper())
print(lst)