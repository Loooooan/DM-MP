import math
import matplotlib.pyplot as plt
import numpy as np

def fic_data(fichier):
    f = open(fichier, 'r')
    data = f.readlines()
    fic = np.zeros((len(data), 3))
    for i in range(len(data)):
        data[i].strip("\n")
        L = data[i].split(";")
        for j in range(3):
            fic[i, j] = L[j]
    f.close()
    return fic

def calc_dist(ptA, ptB):
    return math.sqrt((ptA[0]-ptB[0])**2 + (ptA[1]-ptB[1])**2)

def algoknn(data, pt_search, k):
    tab_dist = np.zeros((len(data), 2))
    cpt = []
    for i in range(len(data)):
        pt_iris1 = [data[i, 0], data[i, 1]] #Liste [longueur, largeur]
        tab_dist[i] = [calc_dist(pt_iris1, pt_search), data[i, 2]] #Liste [distance euclidienne, variété]
    tri_insertion(tab_dist) #Cette fonction est défini dans le sujet
    for i in range(k):
        cpt.append(tab_dist[i, 1])
    prediction1 = cpt.count(0)
    prediction2 = cpt.count(1)
    prediction3 = cpt.count(2)
    if prediction1 >= prediction2 and prediction1 >= prediction3:
        return 0
    elif prediction2 >= prediction1 and prediction2 >= prediction3:
        return 1
    else:
        return 2

data = fic_data("fichier.txt")
liste_longueur = [5] #longueur de l'iris cherché
liste_largeur = [1.7] #largeur de l'iris cherché
liste_type = [algoknn(data, [5, 1.7], 5)] #supposition de la variété de l'iris cherché

for i in range(len(data)):
    liste_longueur.append(data[i, 0])
    liste_largeur.append(data[i, 1])
    liste_type.append(data[i, 2])

if liste_type[0] == 0:
    plt.scatter(liste_longueur[i], liste_largeur[i], marker="v", c="black", label="iris setosa", linewidths=8)
if liste_type[0] == 1:
    plt.scatter(liste_longueur[i], liste_largeur[i], marker=".", c="black", label="iris versicolor", linewidths=8)
if liste_type[0] == 2:
    plt.scatter(liste_longueur[i], liste_largeur[i], marker="+", c="black", label="iris virginica", linewidths=8)

for i in range(1, len(data)):
    if liste_type[i] == 0:
        plt.scatter(liste_longueur[i], liste_largeur[i], marker="v", c="blue", label="iris setosa")
    if liste_type[i] == 1:
        plt.scatter(liste_longueur[i], liste_largeur[i], marker=".", c="red", label="iris versicolor")
    if liste_type[i] == 2:
        plt.scatter(liste_longueur[i], liste_largeur[i], marker="+", c="green", label="iris virginica")

plt.xlabel("longueur des pétales")
plt.ylabel("largeur des pétales")

plt.show()
