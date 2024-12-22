# 1․ Գրել ծրագիր, որը․
#    - կունենա անուններից կազմված list,
#    - հերթով կտպի այն անունները, որոնց երկարությունը 5-ից մեծ չէ,
#    - ամեն անունը տպելուց հետո հաջորդ անունը կտպի 2 վայրկյան հետո։

import time
names = ["Anna", "Babken", "Gegham", "Valod", "Hripsime", "Tatev"]

for name in names:
    if len(name) <= 5:
        print(name)
        time.sleep(2)