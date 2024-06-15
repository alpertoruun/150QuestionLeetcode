def intToRoman(num):  
    m = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',     
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'
    }        

    values = list(m.keys())
    chars = list(m.values())
    roman_num=""
    num_digits = len(str(num))
    i = len(values) - 1
    while num > 0:
        if num >= values[i]:
            roman_num += chars[i]
            num -= values[i]
        else:
            i -= 1
    return roman_num

        

print(intToRoman(2856))
        
