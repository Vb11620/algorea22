from random import *
nbJours = 500000
nbTypes = 100
joursRetard = 50000
f = open("entry.txt", "w")
f.write(str(nbTypes)+"\n")
f.write(str(nbJours)+"\n")
f.write(str(joursRetard)+"\n")
for i in range(nbJours):
    ressource = randint(1, nbTypes)
    action = randint(1, 2)
    f.write(""+str(ressource)+" "+str(action)+"\n")
f.close()
