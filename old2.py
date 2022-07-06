def old():
    file = open("entry.txt", "r")

    nbTypes = int(file.readline())
    nbJours = int(file.readline())
    joursRetard = int(file.readline())

    stockParType = [0] * (nbTypes + 1)
    actionsRetardeesParType = [[]] * (nbTypes + 1)
    nbsCommandesSatisfaites = [0] * (nbTypes + 1)

    for i in range(1, nbJours + 1):  # i correspond à la date
        r, a = file.readline().split()
        r = int(r)

        # enlève les commandes trop vieille
        datedepassee = i - joursRetard - 1
        for j in range(nbTypes + 1):
            if len(actionsRetardeesParType[j]) != 0:
                if actionsRetardeesParType[j][0] == datedepassee:
                    del (actionsRetardeesParType[j][0])

        if a == "1":  # commande
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] - 1
                nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1
                if len(actionsRetardeesParType[r]) != 0:
                    del (actionsRetardeesParType[r][0])
                    actionsRetardeesParType[r].append(i)
            else:
                actionsRetardeesParType[r].append(i)  # ajout de la date de la commande


        else:  # action[i] == 2    livraison
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] + 1
            else:  # vérifie les retards de commande
                stockParType[r] = stockParType[r] + 1
                if len(actionsRetardeesParType[r]) != 0:
                    del (actionsRetardeesParType[r][0])
                    stockParType[r] = stockParType[r] - 1
                    nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1

    return nbsCommandesSatisfaites
