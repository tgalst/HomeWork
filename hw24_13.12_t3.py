# 3․ Գրել դեկորատոր ֆունկցիա, որը կփոփոխի հետևյալ ֆունկցիան այնպես, որ.
#    - այն կաշխատի միայն ժամը 10։00-ից 19։00 ընկած ժամանակահատվածում աշխատեցնելիս,
#    - եթե նշված ժամանակահատվածից դուրս ենք կանչում ֆունկցիան, պետք է տպի "Sorry, it's too late.",
#    - եթե ճիշտ ժամի է կանչած ֆունկցիան, պետք է տպի նաև ֆունկցիան կանչելու ժամանակը՝ տարին, ամիսը, օրը, ժամը, րոպեն,
#
# ֆունկցիան՝
# def f(a):
#     print(f'Welcome {a}!')

import datetime

def dec_f(func):
    def inner(*args, **kwargs):
        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute
        if (10 <= hour < 19 or minutes == 0 and hour == 19):
            print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))
            func(*args, **kwargs)
        else:
            print("Sorry, it's too late.")
    return inner

@dec_f
def f(a):
    print(f'Welcome {a}!')

f("Tatev")
