 # Գրել ծրագիր, որը․
 #   - իր մեջ կունենա սահմանված երկու tuple,
 #     օրինակ` tuple_1 = (11, 55, 54, “abc”, 90, 102, “asdasd”, “qwerty”),
 #             tuple_2 = (“bbb”, 44, 14, 11, 99, “a”),
 #   - կտպի True, եթե գոյություն ունի առնվազն մեկ արժեք, որը առկա է
 #     և tuple_1-ի, և tuple_2-ի մեջ, հակառակ դեպքում տպի False,
 #     օրինակ՝ տվյալ դեպքում երկու tuple-ների մեջ կա 11 թիվը, այդ պատճառով պետք է տպի True:


tuple_1 = (11, 55, 54, "abc", 90, 102, "asdasd", "qwerty")
tuple_2 = ("bbb", 44, 14, 11, 99, "a")
for i in tuple_1:
    if i in tuple_2:
        print(True)
        break
else:
    print(False)