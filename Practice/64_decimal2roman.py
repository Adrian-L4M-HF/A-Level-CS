"""101 Python Problems - no 64"""

def dec2rom(denary: int) -> str:
    conv = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman = []
    while denary > 0:
        for value in conv:
            if value <= denary:
                denary -= value
                roman.append(conv[value])
                break
    return "".join(roman)

print(f'{dec2rom(1987)=}')
assert dec2rom(1987) == 'MCMLXXXVII'
