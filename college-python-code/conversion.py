def bin2Dec(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1

    return dec


def oct2Hex(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1
    print(dec)
    list=[]
    while dec != 0:
        list.append(dec%16)
        dec = dec // 16
    print(list)
    nl=[]
    for elem in list[::-1]:
        if elem <= 9:
            nl.append(str(elem))
        else:
            nl.append(chr(ord('A') + (elem -10)))
    hex = "".join(nl)
    
    return hex

# def oct2Hex2(val):
#     oct_to_bin = {
#         '0': '000', '1': '001', '2': '010', '3': '011',
#         '4': '100', '5': '101', '6': '110', '7': '111'
#     }

#     hex_digits = {
#         '0000': '0', '0001': '1', '0010': '2', '0011': '3',
#         '0100': '4', '0101': '5', '0110': '6', '0111': '7',
#         '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
#         '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
#     }

#     binary_val = ""
#     for digit in val:
#         binary_val += oct_to_bin[digit]

#     while len(binary_val) % 4 != 0:
#         binary_val = '0' + binary_val

#     hex_val = ""
#     i = 0
#     while i < len(binary_val):
#         hex_val += hex_digits[binary_val[i:i+4]]
#         i += 4

#     return hex_val




num = input("Enter a number: ")
print(f"decimal: {oct2Hex(num)}")
