# #3*. Գրել ծրագիր, որը․
#    - կկարդա օգտագործողի կողմից մուտքագրված a պարամետրը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված b պարամետրը (input-ի միջոցով),
#    - կկարդա օգտագործողի կողմից մուտքագրված c պարամետրը (input-ի միջոցով),
#    - կլուծի a*x^2 + b*x + c = 0 քառակուսային եռանդամը և կտպի x1 և x2 լուծումները
#      (D = b^2 - 4*a*c, եթե D > 0, ապա x1 = (-b + sqrt(D)) / (2 * a), x2 = (-b - sqrt(D)) / (2 * a),
#                        եթե D = 0, ապա x = - b / (2 * a),
#                        եթե D < 0, ապա իրական թվերի բազմության մեջ լուծում չունի)։


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
elif D == 0:
    x = - b / (2 * a)
    print("x = ", x)
else:
    print("no solution for real numbers")
