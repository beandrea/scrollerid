import random

print("Enter your password: ")
psw = input()

tot = 0
for i in range(len(psw)):
  single = ord(psw[i])
  tot += single

shift = tot % len(psw)

newStr = ""
for i in range(len(psw)):
    single = ord(psw[i])
    original = single
    negative = ~single
    key = random.randint(1, random.randint(1, 90))
    single = single >> shift
    single = single ^ original
    single = single ^ negative
    single = abs(single << shift)
    single = single ^ key
    newStr += chr(single)

print(newStr)