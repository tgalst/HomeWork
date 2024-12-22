# 1․ Գրել ծրագիր, որը․
#    - միացնելուց պետք է ստուգի usernames.txt ֆայլի առկայությունը (հիշեք անցած մոդուլներից),
#    - եթե ֆայլը առկա է, պետք է կարդա ֆայլում գրաված անունները և պահի usernames լիստում,
#      եթե ֆայլը առկա չէ, պետք է ստեղծի դատարկ usernames լիստ,
#    - պետք է տպի թվանշանների նշանակության ցանկը՝
#      0 - Save to file
#      1 - Add user name
#    - անվերջ ցիկլի մեջ
#      -- կարդա input()՝ մարդու կողմից մուտքագրած թիվը,
#      -- եթե թիվը 1 է, ապա կարդա input() մարդու կողմից ավելացված անունը
#         և ավելացնի usernames լիստին,
#      -- եթե թիվը 0 է, ապա կգրի usernames լիստը usernames.txt ֆայլի մեջ։
import os

if os.path.exists("usernames.txt"):
    print("File exists, reading list from file")
    with open("usernames.txt", "r") as f:
        usernames = f.readlines()
    print(usernames)
else:
    with open("usernames.txt", "w") as f:
        usernames = []
        print("0 - Save to file", "1 - Add user name", sep='\n')
        while True:
            action = input("What to do? ")
            if action == "1":
                name = input("Name = ")
                usernames.append(name)
            elif action == "0":
                f.write('\n'.join(usernames))
                f.close()
                break



