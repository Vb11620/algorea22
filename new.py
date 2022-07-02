def new(p=False):  # p est un booléen à mettre Vrai pour afficher les résultats
    file = open("entry.txt", "r")

    nbTypes = int(file.readline())
    nbJours = int(file.readline())
    joursRetard = int(file.readline())

    datePremierEnfile = [-1] * nbTypes
    dateDernierEnfile = [-1] * nbTypes

    stockParType = [0] * nbTypes
    nbActionsRetardeesParType = [0] * nbTypes
    nbsCommandesSatisfaites = [0] * nbTypes
    dic = {}

    for i in range(nbJours):  # i correspond à la date (qui part du jour 0 jusqu'à nbjours-1)
        r, a = file.readline().split()
        r = int(r)-1

        # enlève les commandes trop vieilles pour la ressource r
        datelimite = i - joursRetard
        if nbActionsRetardeesParType[r] != 0:
            while datePremierEnfile[r] < datelimite and nbActionsRetardeesParType[r] != 0:
                # pop la liste = enlève le premier élément
                nomListePrem = str(r) + "f" + str(datePremierEnfile[r])
                datePremierEnfile[r] = dic[nomListePrem][1]
                del dic[nomListePrem]  # pas obligé sauf si pb de mémoire !!!
                nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] - 1
        if a == "1":  # commande
            if stockParType[r] != 0:  # la ressource attend des commandes
                stockParType[r] = stockParType[r] - 1
                nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1
                if nbActionsRetardeesParType[r] != 0:
                    # Si pas d'action en attente, l'action directement utilisée n'est pas stockée
                    # pop la liste = enlève le premier élément
                    nomListePrem = str(r) + "f" + str(datePremierEnfile[r])
                    datePremierEnfile[r] = dic[nomListePrem][1]
                    del dic[nomListePrem]  # pas obligé sauf si pb de mémoire !!!
                    nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] - 1
                    # ajout de la date de la commande
                    nomliste = str(r) + "f" + str(i)  # clé contenant la ressource et la date
                    if nbActionsRetardeesParType[r] == 0:
                        dic[nomliste] = [i, -1]  # date de la commande en attente et celle suivante
                        datePremierEnfile[r] = i
                        dateDernierEnfile[r] = i
                    else:
                        dic[nomliste] = [i, -1]
                        nomListePrec = str(r) + "f" + str(dateDernierEnfile[r])
                        dic[nomListePrec] = [dateDernierEnfile[r], i]
                        dateDernierEnfile[r] = i
                    nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] + 1
            else:  # la ressouce est indisponible, on met la commande en attente
                # ajout de la date de la commande
                nomliste = str(r) + "f" + str(i)  # clé du dico contenant la ressource et la date
                if nbActionsRetardeesParType[r] == 0:
                    dic[nomliste] = [i, -1]  # date de la commande en attente et celle suivante
                    datePremierEnfile[r] = i
                    dateDernierEnfile[r] = i
                else:
                    dic[nomliste] = [i, -1]
                    nomListePrec = str(r) + "f" + str(dateDernierEnfile[r])
                    dic[nomListePrec] = [dateDernierEnfile[r], i]
                    dateDernierEnfile[r] = i
                nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] + 1

        else:  # action[i] == 2    livraison
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] + 1
            else:  # vérifie les retards de commande
                stockParType[r] = stockParType[r] + 1
                if nbActionsRetardeesParType[r] != 0:
                    # pop la liste = enlève le premier élément
                    nomListePrem = str(r) + "f" + str(datePremierEnfile[r])
                    datePremierEnfile[r] = dic[nomListePrem][1]
                    del dic[nomListePrem]  # pas obligé sauf si pb de mémoire !!!
                    nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] - 1
                    stockParType[r] = stockParType[r] - 1
                    nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1

    return nbsCommandesSatisfaites
