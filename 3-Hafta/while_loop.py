#!/usr/bin/env python3

i  = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("'break' olmadı ?!")
