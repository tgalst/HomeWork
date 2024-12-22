# 4․ Գրել ծրագիր, որը․
#    - կստանա 3 արգումենտ՝ տարի, ամիս, օր,
#    - կտպի թե նշված օրն շաբաթվա որ օրն է։

import time
def f_date(y, m, d):
    str_date = f'{y}/{m}/{d}'
    t = time.strptime(str_date, "%Y/%m/%d")
    return time.strftime("%A", t)

print(f_date(2024, 11, 29))