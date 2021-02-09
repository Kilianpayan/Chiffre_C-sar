from chiffrement import chiffrement
from dechiffrement import dechiffrement

choix = input("Souhaitez-vous [c]hiffrer ou [d]échiffrer un message ?")
if choix == "c":
    msg = input("Entrez le message à chiffrer (en lettres capitales, sans espace ni ponctuation) :")
    msg_chiffre = chiffrement(msg)
    print(f"Le message chiffré est {msg_chiffre}.")
elif choix =="d":
    msg = input("Entrez le message à déchiffrer (en lettres capitales, sans espaces ni ponctuation) :")
    msg_clair = dechiffrement(msg)
    print(f"Le message en clair est {msg_clair}.")