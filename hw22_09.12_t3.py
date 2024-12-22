# 3․ Գրել ծրագիր, որը․
#    - կկարդա որևէ տեքստային ֆայլ,
#    - կհաշվի թե քանի անգամ է հանդիպում այդ ֆայլի մեջ Python բառը և կտպի այդ քանակը,
#    - կտպի բոլոր այն տողերի համարները, որտեղ կա Python բառը, համարակալումը՝ 1-ից,
#    - բոլոր "Python" բառերը ֆայլի մեջ կփոխարինի "Machine learning" բառակապակցությամբ,
#    - կպահպանի ֆայլը։

with open('text.txt', 'r+') as f:
    lines_lst = f.readlines()
    new_lines_lst = []
    word_count = 0
    lines_num = []
    i = 0
    for line in lines_lst:
        i += 1
        if "Python" in line:
            word_count += 1
            lines_num.append(i)
            new_line = line.replace("Python", "Machine learning")
            new_lines_lst.append(new_line)
        else:
            new_lines_lst.append(line)
    f.seek(0)
    f.write(''.join(new_lines_lst))
    print("Python count", word_count)
    print("line numbers", lines_num)