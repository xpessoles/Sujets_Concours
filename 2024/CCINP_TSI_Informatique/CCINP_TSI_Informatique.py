## Question 1
Gex = [[0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0]]

## Question 2
LA = [[1,3,4,6,6],[0,2,3],[1,3],[0,1,2,4],[0,3,5,6,7],[4,6,7],[0,4,5,7],[0,4,5,6]]


## Question 5
def voisins(LA: [[int]], i:int, j:int) -> bool:
    # Version Python
    return j in LA[i]

def voisins_2(LA: [[int]], i:int, j:int) -> bool:
    # Version naïve
    vois = LA[i] # vois contient tous les voisins de i
    for k in range(len(vois)):
        if j == vois[k] :
            return True
    return False

def voisins_3(LA: [[int]], i:int, j:int) -> bool:
    vois = LA[i] # vois contient tous les voisins de i
    for v in vois:
        if j == v :
            return True
    return False

## Question 6
def coloration_valide(LA: [[int]], C:[int]) -> bool:
    for i in range(len(LA)):    # i est un sommet
        for j in LA[i] :        # j est un voisin de i
            if C[i] == C[j]:    # On vérifie la couleur des sommest
                return False
    return True


n=10
## Question 8
C = []
for i in range(n):
    C.append(-1)
# Autre solution
C = [-1 for _ in range(n)]

## Question 9
def colore_sommet(C:[int],s:int,LA:[[int]]) -> None:
    # on détermine la liste des couleurs des voisins de s déjà colorés
    coul_vois = []
    voisins = LA[s]
    for v in voisins:
        if C[v] > -1 and C[v] not in coul_vois: # Attention aux doublons de couleur
            coul_vois.append(C[v])

    # coul_vois est maintenant déterminée et on recherche la
    # plus petite couleur, notée num_coul, absente de coul_vois:
    i = 0
    flag = True
    if len(coul_vois) == 0: # Pour gérér le cas initial ou toutes les couleurs sont à -1
        maxi = -1
    else :
        maxi = max(coul_vois)
    while i <= maxi and flag : # On compte de 1 en 1 et on vérifie que i est dans coul_vois. Sinon, on sort du while.
        if i in coul_vois :
            i=i+1
        else :
            flag = False
    num_coul = i
    # la valeur num_coul trouvée devient la couleur du sommet s:
    C[s] = num_coul


## Question 10
def colorer1(LA:[[int]]) :
    C = [-1 for _ in range(len(LA))]
    for i in range(len(LA)):
        colore_sommet(C,i,LA)
    return C

# q10 = colorer1(LA)
# print(q10)

## Question 11
def colorer2(ordre:[int],LA:[[int]]) :
    C = [-1 for _ in range(len(LA))]
    for i in ordre:
        colore_sommet(C,i,LA)
    return C

# q11 = colorer2([0,2,4,6,1,3,5,7],LA)
# print(q11)

## Question 12
# q12 = colorer2([7,6,5,4,3,2,1,0],LA)
# print(q12)

## Question 13
def degre(LA:[[int]]) -> [int]:
    D = []
    for s in LA :
        D.append(len(s))
    return D

def degre_02(LA:[[int]]) -> [int]:
    return [len(s) for s in LA]

# LA = [[1,2], [0,2,3], [0,1,3], [1,2,4], [3]]
# print(degre(LA),degre_02(LA),degre(LA) == degre_02(LA))

## Question 14
def init(n:int) -> [[None]]:
    return [[] for _ in range(n)]

#print(init(3))


## Question 15
def ranger(LA:[[int]]) -> [int]:
    R = init(len(LA))
    D = degre(LA)
    for i in range(len(D)):
        R[D[i]].append(i)
    return R

# LA = [[1,2], [0,2,3], [0,1,3], [1,2,4], [3]]
# print(ranger(LA))

## Question 16
def renverse(L:[]) -> []:
    Lr = []
    for e in L :
        Lr = [e]+Lr
    return Lr

# print(renverse([1,2,3,4]))

## Question 17
def trier_sommets(LA:[[int]]) -> [int]:
    # Dans R, les sommets sont triés par nombre de de dégrés
    R = ranger(LA)
    res = []
    for L in R:
        for s in L:
            res.append(s)
    return renverse(res)
#
# LA = [[1,2], [0,2,3], [0,1,3], [1,2,4], [3]]
# print(trier_sommets(LA))

## Question 18
def colorer3(LA:[[int]]) -> [int]:
    ordre = trier_sommets(LA)
    return colorer2(ordre,LA)

# print(colorer3(LA))

## Question 21
def degre_satur(LA:[[int]],C:[int],s:[int]) -> int:
    voisins = LA[s]
    # On récupére les couleurs des voisins
    liste_coul = []
    for v in voisins:
        if C[v] != -1 and C[v] not in liste_coul :
            liste_coul.append(C[v])
    return len(liste_coul)


## Question 22

























## Question 23 -- Ligne 200
def pas_fini(C):
    if -1 in C :
        return True
    else :
        return False



## Quesion 24






























## Question 25 -- Ligne 240
def est_clique(LA,K):
    for i in K:
        for j in K:
            if j not in LA[k]:
                return False
    return True

