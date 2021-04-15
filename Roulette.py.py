from random import *
import time


def mise(mise):
    test = 0
    while test != 1:
        mise = input("Tapez le montant de votre mise : ")
        if mise.isdigit():
            mise = int(mise)
            if mise > 0 and mise <= balance :
                test = 1
            elif mise == 0:
                print("La mise doit être suppérieur à 0.")
            else:    
                print("La mise doit être inférieur à votre balance.")
        else:
            print("La mise doit être un entier positif.")
    return mise

def couleur_mise():
    test = 0
    while test != 1:
        couleur = str(input("Sur quelle couleur voulez vous miser ? "))
        if couleur.lower() == "vert" or couleur.lower() == "noir" or couleur.lower() == "rouge":
            test = 1
        else:
            print("Couleur invalide, merci de choisir entre vert, noir et rouge")
    couleur = couleur.lower()
    return couleur

def couleur_tombe():
    print ("La roulette tourne....")
    if randint(0,13) == 0:
        couleur_tombe = "vert"
        print("La roulette est tombée sur le", couleur_tombe)
        return couleur_tombe
    elif randint(0,13) > 0 and randint(0,13) < 8:
        couleur_tombe = "rouge"
        print("La roulette est tombée sur le", couleur_tombe)
        return couleur_tombe
    else :
        couleur_tombe = "noir"
        print("La roulette est tombée sur le", couleur_tombe)
        return couleur_tombe
    
def win_loose(balance, mise, couleur_tombe, couleur_mise):
    if couleur_mise == "rouge" and couleur_mise == couleur_tombe:
        print ("Gagné ! Vous gagnez", mise, "coins.")
        balance += mise
        print ("Votre balance est maintenant de :", balance)
    elif couleur_mise == "noir" and couleur_mise == couleur_tombe:
        print ("Gagné ! Vous gagnez", mise, "coins.")
        balance += mise
        print ("Votre balance est maintenant de :", balance)
    elif couleur_mise == "vert" and couleur_mise == couleur_tombe:
        print ("Gagné ! Vous gagnez", mise*14, "coins.")
        balance += mise*14
        print ("Votre balance est maintenant de :", balance)
    else :
        print("Aie ! Vous perdez", mise, "coins.")
        balance -= mise
        print ("Votre balance est maintenant de :", balance)
    return balance
            
def rejouer(replay):
    if balance > 0:
        test = 0
        while test != 1:
            oui_non = str(input("Voulez vous rejouer ? Entrez o ou n : "))
            if oui_non.lower() == "o" or oui_non.lower() == "n":
                if oui_non.lower() == "n":
                    replay = False
                test = 1
            else:
                print("Veuillez saisir o ou n : ")
        return replay

        
print ("Bienvenue au casino")
time.sleep(2)

balance = 10000
replay = True


while replay == True:
    print("Votre balance est de", balance)
    var_mise = mise(mise)
    var_couleur_mise = couleur_mise()
    var_couleur_tombe = couleur_tombe()
    balance = win_loose(balance, var_mise, var_couleur_mise, var_couleur_tombe)
    replay = rejouer(replay)
print("Vous quittez le casino.")