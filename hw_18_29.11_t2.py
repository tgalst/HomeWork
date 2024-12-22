# 2. Գրել ֆունկցիա, որը․
#    - կհաշվի 1-ից 100_000_000 միջակայքում գտնվող 3-ի բաժանվող թվերի քանակը,
#    - կտպի այդ ֆունկցիայի կատարման ժամանակը վայրկյաններով։

import time

def div3():
    lst = []
    for i in range(3, 100_000_001, 3):
        lst.append(i)
    return len(lst)

a = time.time()
print(div3())
b = time.time()
print(b - a)