#1. Գրել ֆունկցիա (Ցելսիուսից Ֆարենհայթ կամ Ֆարենհայթից Ցելսիուս), որը․
#    - կստանա որպես արգումենտ 3 արժեք,
#      -- առաջինը՝ աստիճանը, կլինի positional-only արգումենտ,
#      -- երկրորդը՝ "c" կամ "f", այն տեսակն է, որը պետք է փոխվի, կլինի keyword-only արգումենտ,
#         default արժեքը կլինի "c",
#      -- երրորդը՝ "c" կամ "f", այն տեսակն է, որը պետք է վերածվի, կլինի keyword-only արգումենտ,
#         default արժեքը կլինի "f",
#    - կդարձնի ցելսիուսը ֆարենհայթ կամ ֆարենհայթը ցելսիուս և կվերադարձնի արժեքը։


def convert_temperature(t,/, *, current_unit = 'c', convert_unit = 'f'):
    if current_unit == 'c' and convert_unit == 'f':
        convert_temp = t * 9 / 5 + 32
    elif current_unit == 'f' and convert_unit == 'c':
        convert_temp = (t -32) * 5 / 9
    elif current_unit == convert_unit == 'c' or current_unit == convert_unit == 'f':
        convert_temp = t
    else:
        return "wrong unit"
    return convert_temp, convert_unit

temperature = float(input("temperature = "))
from_unit = input("current unit (c or f) = ")
to_unit = input("convert unit (c or f) = ")
print(convert_temperature(temperature, convert_unit = to_unit, current_unit = from_unit))