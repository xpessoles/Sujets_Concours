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
texte1 = "Le grand château fort."
texte1 = [lettre for lettre in texte1]
texte2 = "Le petit chien a soif."
texte2 = [lettre for lettre in texte2]
di,d = différentiel(texte1,texte2)
