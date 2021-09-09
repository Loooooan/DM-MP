def moyenne(liste_niveaux):
    somme = 0
    for elt in liste_niveaux:
        somme += elt
    return somme/len(liste_niveaux)

def integrale_precise(liste_niveaux):
    valeure_integrale = 0
    #Durée totale: 20 minutes = 1200s
    #Durée entre chaque valeur: 0.5s (Fréquence de 2Hz => t=1/2s)
    #2400 valeurs attendues (1200/0.5)
    liste_temps = []
    temps = 0
    #Création d'une liste à 2400 valeurs
    for i in range(2400):
        liste_temps.append(temps)
        temps += 0.5
    #Pour simplifier, on considère que la fonction commence à 0s et que l'étude se termine à t=1200s
    debut = 0
    fin = 1200
    #Le pas de chaque subdivision est de 0.5, on pose alors n=2400
    n = 2400
    h = (fin-debut)/n #=0.5
    for i in range(n):
        valeure_integrale += (h/2)*(liste_niveaux[liste_temps.index(debut+i*h)] + liste_niveaux[liste_temps.index(debut+(i+1)*h)])
    return valeure_integrale

def moyenne_precise(liste_niveaux):
    #m = (1/(fin-debut))*integrale de debut à fin de nu
    debut = 0
    fin = 1200
    return (1/(fin-debut))*integrale_precise(liste_niveaux)
