import create
import new
import old
import time

prec = 500

print("----------NEW----------")
tNew = 0
for i in range(prec):
    t2 = time.monotonic()
    repNew = new.new()
    tNew += time.monotonic()-t2
tNew /= prec

print("----------OLD----------")
tOld = 0
for i in range(prec):
    t1 = time.monotonic()
    repOld = old.old()
    tOld += time.monotonic()-t1
tOld /= prec
print("---------EQUAL---------")
print(repOld == repNew)
print("Old Time : ", tOld)
print("New Time : ", tNew)
