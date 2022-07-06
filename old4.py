def new():  # p est un booléen à mettre Vrai pour afficher les résultats

    def enlevePremier(r):
        nomListePrem = str(r) + "f" + str(datePremierEnfile[r])
        datePremierEnfile[r] = dic[nomListePrem][1]
        del dic[nomListePrem]  # pas obligé sauf si pb de mémoire !!!
        nbActionsRetardeesParType[r] = nbActionsRetardeesParType[r] - 1

    def ajouterDernier(r):
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

    file = open("entry.txt", "r")

    nbTypes = int(file.readline())
    nbJours = int(file.readline())
    joursRetard = int(file.readline())

    global datePremierEnfile
    datePremierEnfile = [-1] * nbTypes
    global dateDernierEnfile
    dateDernierEnfile = [-1] * nbTypes

    stockParType = [0] * nbTypes
    global nbActionsRetardeesParType
    nbActionsRetardeesParType = [0] * nbTypes
    nbsCommandesSatisfaites = [0] * nbTypes
    global dic
    dic = {}

    for i in range(nbJours):  # i correspond à la date (qui part du jour 0 jusqu'à nbjours-1)
        ressource, action = file.readline().split()
        r = int(ressource) - 1

        # enlève les commandes trop vieilles pour la ressource r
        datelimite = i - joursRetard
        if nbActionsRetardeesParType[r] != 0:
            while datePremierEnfile[r] < datelimite and nbActionsRetardeesParType[r] != 0:
                # pop la liste = enlève le premier élément
                enlevePremier(r)
        if action == "1":  # commande
            if stockParType[r] != 0:  # la ressource attend des commandes
                stockParType[r] = stockParType[r] - 1
                nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1
                if nbActionsRetardeesParType[r] != 0:
                    # Si pas d'action en attente, l'action directement utilisée n'est pas stockée
                    # pop la liste = enlève le premier élément
                    enlevePremier(r)
                    # ajout de la date de la commande
                    ajouterDernier(r)
            else:  # la ressouce est indisponible, on met la commande en attente
                # ajout de la date de la commande
                ajouterDernier(r)

        else:  # action[i] == 2    livraison
            if stockParType[r] != 0:
                stockParType[r] = stockParType[r] + 1
            else:  # vérifie les retards de commande
                stockParType[r] = stockParType[r] + 1
                if nbActionsRetardeesParType[r] != 0:
                    # pop la liste = enlève le premier élément
                    enlevePremier(r)
                    stockParType[r] = stockParType[r] - 1
                    nbsCommandesSatisfaites[r] = nbsCommandesSatisfaites[r] + 1

    return nbsCommandesSatisfaites
