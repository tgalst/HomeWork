# 2․ Գրել ծրագիր, որը․
#    ա)
#    - կկարդա որևէ նկար և կպահի img_1 փոփոխականի մեջ,
#    - կտպի img_1-ի չափերը,
#    - կփոքրացնի img_1-ի չափերը 3 անգամ,
#    - img_1-ը flip կանի ձախից աջ,
#    բ)
#    - screen կանի էկրանը և կպահի img_2 փոփոխականի մեջ,
#    - կտպի img_2-ի չափերը,
#    - img_2-ը կդարձնի սև-սպիտակ,
#    - img_2-ի վրա կավելացնի img_1-ը այնպես, որ img_1-ը լինի img_2-ի ուղիղ կենտրոնում,
#    - ստացված նկարում մեջտեղի նկարը պետք է լինի գունավոր, հետևի ֆոնը սև-սպիտակ,
#    - կպահպանի ստացված նկարը համակարգչի մեջ։



from PIL import Image
from PIL import ImageGrab

img_1 = Image.open("/Users/tpoghosy/Downloads/dog.jpeg")
img_2 = ImageGrab.grab()
img_1.show()
size = img_1.size
print(size)
img_1.resize((int(size[0]/3), int(size[1]/3))).show()
img_1.transpose(Image.FLIP_LEFT_RIGHT).show()

img_2.show()
size2 = img_2.size
print(size2)
final_img = img_2.convert("L").convert("RGB")
final_img.paste(img_1, (int(size2[0]/2-size[0]/2), int(size2[1]/2 - size[1]/2)))
final_img.show()
final_img.save("/Users/tpoghosy/Downloads/python_out.jpeg")
