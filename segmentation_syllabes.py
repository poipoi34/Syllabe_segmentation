#plan d'action:
#faire une fonction qui sépare un mot en syllabes selon des regles de ce1
#faire une correspondance sonore pour chaque syllabe (eau = o = au, pé = pai)
#transcrire la liste de mots en liste de triplets de syllabes
#trouver le nom des 7 notes (ou 12) qui permet le plus d'accord majeur qui sont des mots

liste_voyelles = ["a","e","i","o","u","y"]

def voyelle(lettre):
    return liste_voyelles.count(lettre) == 1

def segmentate(mot):
    liste_syllabe = []
    chgt = 0 #changement -> consonne à voyelle, ou voyelle à consonne
    cur_syl = ""
    
    for i in range(len(mot)-1):
        cur_syl += mot[i]
        if ( (voyelle(mot[i]) and not voyelle(mot[i+1])) or (not voyelle(mot[i]) and voyelle(mot[i+1])) ):
            chgt += 1
            if chgt == 2:
                liste_syllabe.append(cur_syl[:])
                cur_syl = ""
                chgt = 0
    liste_syllabe.append(cur_syl + mot[-1])
    return liste_syllabe

liste_voyelles = ["a","e", "é", "è", "i", "o", "u", "an", "in", "oi", "on", "ou"]
liste_consonnes = ["b", "c", "d", "f", "g", "j", "l", "m", "n", "p", "r", "s", "t", "v", "z", "br", "cr", "dr", "fr", "gr", "pr", "tr", "vr", "bl", "cl", "fl", "gl", "pl", "ch"]

def start_voyelle(mot):
    max_voyelle = 3
    for i in range (1,max_voyelle):
        if mot[3:]

def segmentate_2(mot_p):
    liste_syllabes = []
    cur_syllabe = ""
    if start_voyelle(mot[])


liste_mots = ["bonjour", "aligator", "crocodile", "tartampion", "banane"]

for mot in liste_mots:
    print(segmentate(mot))
            