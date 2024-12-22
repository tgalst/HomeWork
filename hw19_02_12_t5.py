# 5․ Գրել ծրագիր, որը․
#    - կունենա հետևյալ tuple-ների list-ը, որտեղ tuple-ի առաջին էլեմենտը առարկայի անունն է, երկրորդը՝ գնահատականը,
#    օրինակ՝ user_list = [('Python', 97), ('English', 88), ('Maths', 94), ('Russian', 89)],
#    - կսորտավորի list-ի էլեմենտները ըստ գնահատականի փոքրից մեծ՝ sorted և lambda ֆունկցիաների միջոցով,
#    պետք է տպի՝ [('English', 88), ('Russian', 89), ('Maths', 94), ('Python', 97)]:

user_list = [('Python', 97), ('English', 88), ('Maths', 94), ('Russian', 89)]
user_list.sort(key=lambda x: x[1])
print(user_list)