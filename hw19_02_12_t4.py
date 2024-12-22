# 4. Գրել ծրագիր, որը․
#    - կբազմապատկի տրված list-ի բոլոր էլեմենտները միմյանց հետ reduce և lambda ֆունկցիաների միջոցով,
#    օրինակ՝ nums = [1, 2, -4, 8, -15, 3, 0.5, 0.75, -0.2, -2, 0.0625],
#    - կտպի ստացված արժեքը,
#    տվյալ օրինակում պետք է տպի՝ 27.0։

from functools import reduce

nums = [1, 2, -4, 8, -15, 3, 0.5, 0.75, -0.2, -2, 0.0625]
r = reduce(lambda x, y : x * y, nums)
print(r)