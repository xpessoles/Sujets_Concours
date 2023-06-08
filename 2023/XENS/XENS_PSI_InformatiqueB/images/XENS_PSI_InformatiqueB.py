## Question 1
def textes_égaux(texte1, texte2) :
    for i in range(len(texte1)) :
        if texte1[i] != texte2[i] :
            return False
    return True

t1 = ['v', 'i', 's', 'a']
t2 = ['v', 'a', 'i', 's']
print("Question 1")
q1_1 = textes_égaux(t1,t2)
q1_2 = textes_égaux(t1,t1)
print(q1_1,q1_2)


## Question 2
def distance(texte1, texte2) :
    cpt = 0
    for i in range(len(texte1)) :
        if texte1[i] != texte2[i] :
            cpt = cpt + 1
    return cpt
print("Question 2")
t3 = ['a', 'v', 'i', 's']
q2_1 = distance(t1,t2)
q2_2 = distance(t3,t1)
print(q2_1,q2_2)

## Question 3
def aucun_caractère_commun(texte1, texte2) :
    # Création d'un dictionnaire listant les caractères
    dico = {}

    # On met dans dico l'ensemble des caractères de texte1
    for lettre in texte1 :
        if lettre not in dico :
            dico[lettre]=True

    # On vérifie que les lettres de texte2 ne sont pas dans dico
    for lettre in texte2 :
        if lettre in dico :
            return False
    return True
print("Question 3")
t4 = ['u', 'r', 'n', 'e']
q3_1 = aucun_caractère_commun(t1,t2)
q3_2 = aucun_caractère_commun(t1,t4)
print(q3_1,q3_2)


## Question 4
def différentiel(texte1, texte2) :
    diff_i = []
    diff = []
    for i in range(len(texte1)):
        if texte1[i] != texte2[i] :
            diff_i.append(i)
    debut = diff_i[0]
    for i in range(len(diff_i)-1) :
        if i == 11 :
            print(11)
        if diff_i[i+1]!=diff_i[i]+1 :
            fin = diff_i[i]+1
            print(debut)
            diff.append([debut,texte1[debut:fin],texte2[debut:fin]])
            debut = diff_i[i+1]
    # cas terminal à traiter
    return diff_i,diff


    return diff



def tranche(arg_début, arg_avant, arg_après):
    return {'début': arg_début, 'avant': arg_avant, 'après': arg_après}

def début(tr):
    return tr['début']

def après(tr):
    return tr['après']

def avant(tr):
    return tr['avant']

def fin(tr):
    return début(tr) + len(après(tr))

def applique(texte1,diff) :
    # Attention, un texte est une liste de chaînes de caractères
    texte2 = texte1[:]
    for slice in diff :
        for i in range(début(slice),fin(slice)):
            texte2[i]=texte1[i]
    return texte2

def différentiel(texte1, texte2):
    diff = []
    modif = False
    for i in range(len(texte1)):
        if texte1[i] != texte2[i] and not modif:
            modif = True
            début = i
            avant = [texte1[i]]
            après = [texte2[i]]
        elif texte1[i] != texte2[i] and modif:
            avant.append(texte1[i])
            après.append(texte2[i])
        elif texte1[i] == texte2[i] and modif:
            modif = False
            diff.append(tranche(début, avant, après))
    if modif:
        diff.append(tranche(début, avant, après))
    return diff

texte1 = "Le grand château fort."
texte1 = [lettre for lettre in texte1]
texte2 = "Le petit chien a soif."
texte2 = [lettre for lettre in texte2]
diff = différentiel(texte1,texte2)

def inverse(diff):
    inv = []
    for slice in diff :
        inv.append(tranche(début(slice),après(slice),avant(slice)))
    return inv
######
def versionne(texte):
    return {'courant' : texte, 'historique' : [] }

def courant(texte_versionné):
    return texte_versionné['courant']

def remplace_courant(texte_versionné, texte):
    texte_versionné['courant'] = texte

def historique(texte_versionné):
    return texte_versionné['historique']
######


def modifie(texte_versionné,texte):
    # On récupère les 2 textes
    texte1 = texte
    texte2 = courant(texte_versionné)
    # On détermine le diff
    diff = différentiel(texte1,texte2)

    # On remplacé le texte courant :
    remplace_courant(texte_versionné, texte)

    # On modifie l'historique
    historique(texte_versionné).append(diff)

def annule(texte_versionné):
    # On récupère le dernier diff et on l'inverse
    diff = texte_versionné[historique].pop()
    diff = inverse(diff)
    # On applique le diff
    texte2 = applique(texte_versionné['courant'],diff)
    # On remplace le texte
    remplace_courant(texte_versionné, texte2):


