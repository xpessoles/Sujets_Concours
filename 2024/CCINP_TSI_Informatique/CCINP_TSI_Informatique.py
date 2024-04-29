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
