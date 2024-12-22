# 3․ Գրել պարային զույգեր կազմելու ծրագիր, որը․
#    - կունենա երկու անունների list, list-երի երկարությունները կարող են տարբեր լինել,
#    օրինակ՝ girls = ['Gohar', 'Ani', 'Tatev']
#            boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
#    - պատահականության սկզբունքով կտպի պարային զույգեր list-երից
#      փոքրագույն երկարություն ունեցողի քանակությամբ (անունները չպետք է կրկնվեն),
#    տվյալ օրինակի դեպքում կտպի՝ Gohar - Ashot
#                                Ani - Gor
#                                Tatev - Karen։

import random

girls = ['Gohar', 'Ani', 'Tatev']
boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']

random.shuffle(girls)
random.shuffle(boys)

for z in zip(girls, boys):
   print(z)