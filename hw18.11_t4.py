# 4. Գրել ծրագիր, որը․
#    - մեկ input-ի միջոցով օգտատիրոջից կհարցնի տարբեր մրգերի անուններ բացատով առանձնացված,
#    - մեկ input-ի միջոցով օգտատիրոջից կհարցնի տարբեր մրգերի գներ բացատով առանձնացված,
#    - այդ երկու input արած արժեքները կվերածի list-երի։
#    Գրել ֆունկցիա, որը.
#    - կստանա որպես արգումենտ 2 list-եր, կլինեն keyword-only արգումենտներ առանց default արժեքների,
#    - այդ list-երից կստանա dict, որտեղ անունները կլինեն key-երը, իսկ գները որպես float արժեք value-ները,
#    - հաշվի առեք, որ list-երը կարող են ունենալ տարբեր երկարություններ,
#      եթե ավելի երկար է անունների list-ը, ավել անունների value-ները պետք է լինեն None,
#      իսկ եթե ավելի երկար է գների list-ը, ավել արժեքները չպետք է վերցնենք։

def ret_dict_from_lists(*, fruites, prices):
    ret_dict = {}
    for i in range(len(fruites)):
        if i >= len(prices):
            val = None
        else:
            val = float(prices[i])
        ret_dict[fruites[i]] = val
    return ret_dict

str_fruites = input("fruits names? ")
str_prices = input("fruits prices? ")

lst_fruites = str_fruites.split()
lst_prices = str_prices.split()

print(ret_dict_from_lists(fruites=lst_fruites, prices=lst_prices))