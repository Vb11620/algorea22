import create
import V3papa
import old
import old2
import V2papa
import time

prec = 50

print("----------NEW----------")  # papa v3
tNew = 0
for i in range(prec):
    t2 = time.monotonic()
    repV3 = V3papa.new()
    tNew += time.monotonic() - t2
tNew /= prec
"""
print("----------OLD----------")
tOld = 0
for i in range(1):
    t1 = time.monotonic()
    repOld = old.old()
    tOld += time.monotonic() - t1
tOld /= 1
"""
"""
print("----------OLD2---------")  # papa v1
tOld2 = 0
for i in range(3):
    t12 = time.monotonic()
    repOld2 = old2.old()
    tOld2 += time.monotonic() - t12
tOld2 /= 3
"""
print("----------OLD3---------")  # papa v2
tOld3 = 0
for i in range(prec):
    t13 = time.monotonic()
    repV2 = V2papa.old()
    tOld3 += time.monotonic() - t13
tOld3 /= prec

print("---------EQUAL---------")
# print(repNew == repOld)
# print(repOld3 == repOld)
print(repV3 == repV2)
# print("Old Time : ", tOld)
# print("V1 papa Time : ", tOld2)
print("V2 papa Time : ", tOld3)
print("V3 papa Time : ", tNew)
