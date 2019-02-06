import binascii

f = open('nonsense')
hexes = f.read()
hex_codes = hexes.split('\\x')[1:]
print(hex_codes)

for a in range(0x0, 0xff):
    f = open('un_nonsense'+str(a)+'.bin', 'w')
    for code in hex_codes:
        #b = binascii.unhexlify(code)
        b = int(code, 16)
        b = chr(b^a)
        f.write(b)

