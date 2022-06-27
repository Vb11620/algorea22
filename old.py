def old(p=False):  # p est un booléen à mettre Vrai pour afficher les résultats
    file = open("entry.txt", "r")

    nombreDeTypesDeRessources = int(file.readline())
    nombreDeJours = int(file.readline())
    stock = nombreDeTypesDeRessources * [0]
    nombreDeCommandesSatisfaitesParTypeDeRessources = nombreDeTypesDeRessources * [0]
    listeDesRetardsDuPlusAncienAuPlusRecent = int(file.readline()) * [-1]

    def traitementRetards(retard_a_traiter):
        if retard_a_traiter != -1 and stock[retard_a_traiter] != 0:
            stock[retard_a_traiter] -= 1
            nombreDeCommandesSatisfaitesParTypeDeRessources[retard_a_traiter] += 1
            return -1
        return retard_a_traiter

    for i in range(nombreDeJours):
        typeDeRessource, action = file.readline().split()
        typeDeRessource = int(typeDeRessource) - 1
        if action == "2":
            stock[typeDeRessource] += 1
            typeDeRessource = -1
        listeDesRetardsDuPlusAncienAuPlusRecent.append(typeDeRessource)
        listeDesRetardsDuPlusAncienAuPlusRecent = list(map(traitementRetards, listeDesRetardsDuPlusAncienAuPlusRecent))
        del listeDesRetardsDuPlusAncienAuPlusRecent[0]

    if p:
        for i in nombreDeCommandesSatisfaitesParTypeDeRessources:
            print(i)

    file.close()

    return nombreDeCommandesSatisfaitesParTypeDeRessources
