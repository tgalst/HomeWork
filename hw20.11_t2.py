# 2. Գրել զառ նետելու խաղի ծրագիր ֆունկցիայի միջոցով, որը․
#    - կպահի համակարգչի և խաղացողի հաշիվը,
#    - ցիկլի միջողոց՝
#      -- կկարդա խաղացողի կողմից մուտքագրված թիվը և կստուգի, որ այն լինի 1 - 6 սահմանում,
#      -- կգենեռացնի պատահական թիվ 1-6 սահմանում,
#      -- կորոշի, թե ով է հաղթողը և հաղթողի հաշիվը կավելացնի մեկով,
#    - խաղը ավարտվում է երբ համակարգչի կամ խաղացողիհաշիվը 5-ի է հասնում:

import random

def zar():
    user_score = 0
    comp_score = 0
    while True:
        user_ = int(input("1-6? "))
        if not (0 < user_ < 7):
            print("Try again.")
            continue
        comp_ = random.randint(1,6)
        print("Comp", comp_)
        if user_ > comp_:
            user_score += 1
        elif user_ < comp_:
            comp_score += 1
        if comp_score == 5 or user_score == 5:
            break
    if user_score > comp_score:
        print("You Win!")
    else:
        print("You Lose!")

zar()