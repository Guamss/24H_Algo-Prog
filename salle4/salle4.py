import math

def triangulaires(n):
    return [i*(i+1)/2 for i in range(1,n+1)]

def is_triangulaire(n):
    r=int(math.sqrt(2*n))
    if n==r*(r+1)//2 or n==(r+1)*(r+2)//2:
        return True
    else:
        return False
def v(x):
    ALPH = "abcdefghijklmnopqrstuvwxyz"
    return ALPH.find(x)+1
def p(x):
    r=int(math.sqrt(2*x))
    if not is_triangulaire(x):
        return 0
    else:
        return r*(r*(r+1)//2) 

content = ""
with open("JKRowling.txt") as file:
    contents_file = file.readlines()
for string in contents_file:
    content += string.replace("\n", " ")
mots = content.split()

liste_valeur_mot = []

for mot in mots:
    c = 0
    for lettre in mot:
        lettre = lettre.lower()
        c += v(lettre)
    liste_valeur_mot.append(c)
    
poid=0
for val in liste_valeur_mot:
    poid+=p(val)
print(mots)
print(poid)
