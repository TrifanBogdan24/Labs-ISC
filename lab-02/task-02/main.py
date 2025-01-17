#!/usr/bin/env python3

import gmpy2

# Given values
p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163
n = 70736025239265239976315088690174594021646654881626421461009089480870633400973
e = 3
c = 28822365203577929536184039125870638440692316100772583657817939349051546473185

phi_n = (p - 1) * (q - 1)

d = gmpy2.invert(e, phi_n)
m = gmpy2.powmod(c, d, n)

message = bytearray.fromhex(hex(m)[2:]).decode()

print("Decrypted message:", message)
