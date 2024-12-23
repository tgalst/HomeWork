# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
#    - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
#      (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։

import math
class Triangle:
    def __init__(self,a, b, c):
        if a + b <= c or b + c <= a or a + c <= b:
            print("Error: this is not a triangle")
            exit()
        self.a = a
        self.b = b
        self.c = c
    def get_sides(self):
        return self.a, self.b, self.c
    def get_perimeter(self):
        return self.a + self.b + self.c
    def get_area(self):
        #s = (a + b + c)/2
        #A = √[s(s - a)(s - b)(s - c)]
        s = self.get_perimeter()/2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    def get_type(self):
        if self.a == self.b == self.c:
            #հավասարակողմ
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.c == self.b:
            #հավասարասրուն
            return "Isosceles"
        else:
            #անկանոն
            return "Scalene"
    def is_right_triangle(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or self.c ** 2 + self.b ** 2 == self.a ** 2:
            return True
        return False
    def get_angels(self):
        angle_a = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)))
        angle_b = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        angle_c = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.b * self.c)))
        return angle_a, angle_b, angle_c
    def get_more(self):
        #ներգծած
        inscribed = 2 * self.get_area() / self.get_perimeter()
        #արտագծած
        circumscribed = self.a * self.b * self.c / (4 * self.get_area())
        return inscribed, circumscribed
    def print_all(self):
        print("Sides:", self.get_sides())
        print("Perimeter:", self.get_perimeter())
        print("Area:", self.get_area())
        print("Triangle type:", self.get_type())
        print("Is right triangle:", self.is_right_triangle())
        print("Angles (A, B, C):", self.get_angels())
        print("Radii of inscribed and circumscribed circles", self.get_more())

t = Triangle(5, 12, 13)
t.print_all()
