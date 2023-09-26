def bin2Dec(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1

    return dec


def oct2Hex(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1

    hex_val = hex(dec)
    hex_val = hex_val.upper()

    return hex_val[2:]


num = input("Enter a number: ")
print(f"decimal: {oct2Hex(num)}")
