# #Գրել ծրագիր որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված հեռախոսահամարը,
#    - կստուգի արդյոք հեռախոսահամարը ճիշտ է մուտքագրված (օրինակ կազմված լինի թվերից և այլն),
#    - կվերադարձնի հետևյալ ֆորմատով +374yyxxxxxx։

mobile = (input("mobile number - "))
if (mobile.isdigit()) and (len(mobile) == 9) and (mobile[0] == '0'):
    print("+374" + mobile[1:])
else:
    print("wrong number")












