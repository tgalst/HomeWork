# 3․ Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված text փոփոխականը (input֊ի միջոցով),
#    - կստուգի արդյոք text-ը սկսվում է մեծատառով,
#    - կստուգի արդյոք text-ը սկսվում է փոքրատառով,
#    - կստուգի արդյոք text-ի երկարությունը զույգ է, թե կենտ, և կտպի արդյունքը,
#    - կստուգի թե քանի անգամ է ՛a՛ տառը կրկնվում text-ի մեջ և կտպի այդ թիվը,
#    - կստուգի արդյոք text-ի բոլոր սիմվոլները տառեր են,
#    - կդարձնի text-ի բոլոր տառերը փոքրատառ,
#    - կդարձնի text-ի առաջին տառը մեծատառ,
#    - կգտնի ՛a՛ տառի ինդեկսը text-ի մեջ,
#    - կփոխարինի text-ի մեջ հանդիպած առաջին ՛a՛ տառը ՛b՛ տառով,
#    - կավելացնի 5 զրոներ text-ի և աջ, և ձախ կողմերից։

text = input("inout text: ")
print("is title:", text.istitle())
print("is not title:", not text.istitle())
if len(text) % 2 == 1:
    print("the count of letters is odd")
else:
    print("the count of letters is even")
print("count of 'a' letters:", text.count("a"))
print("are all symbols  letter:", text.isalpha())
print("replace to lowercase:", text.lower())
print("replace first letter to capital:",text.capitalize())
print("index of 'a' letter:", text.find("a"))
print("replace 'a' to 'b':", text.replace('a','b'))
print("add 5 zeros from left and right:", text.center(len(text) + 10,'0'))
#print("00000" + text + "00000")


