def old():
    file = open("entry.txt", "r")

    nbTypes = int(file.readline())
    nbJours = int(file.readline())
    joursRetard = int(file.readline())

    stockParType = [0] * nbTypes
    actionsRetardeesParType = [[] for _ in range(nbTypes)]  # _ = i
    nbsCommandesSatisfaites = [0] * nbTypes

    for i in range(nbJours):  # i correspond à la date (qui part du jour 0 jusqu'à nbJours-1)
        r, a = file.readline().split()
        r = int(r) - 1

        # enlève les commandes trop vieilles pour la ressource r
        dateLimite = i - joursRetard
        continu = True
        while continu:
            if len(actionsRetardeesParType[r]) != 0:
                if actionsRetardeesParType[r][0] < dateLimite:
                    actionsRetardeesParType[r].pop(0)  # del() peut marcher aussi
                else:
                    continu = False
            else:
                continu = False

        if a == "1":  # commande
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] - 1
                nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1
                if len(actionsRetardeesParType[r]) != 0:
                    # Si pas d'action en attente, l'action directement utilisée n'est pas stockée
                    actionsRetardeesParType[r].pop(0)
                    actionsRetardeesParType[r].append(i)
            else:
                actionsRetardeesParType[r].append(i)  # ajout de la date de la commande

        else:  # action[i] == 2    livraison
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] + 1
            else:  # vérifie les retards de commande
                stockParType[r] = stockParType[r] + 1
                if len(actionsRetardeesParType[r]) != 0:
                    actionsRetardeesParType[r].pop(0)
                    stockParType[r] = stockParType[r] - 1
                    nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1

    return nbsCommandesSatisfaites
