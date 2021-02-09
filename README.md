### Projet d'introduction à Github (chiffre de César)

### 1. Le chiffre de César
Le chiffre de César est une méthode de chiffrement très simple utilisée par Jules César dans ses correspondances secrètes. Pour obtenir le etxte chiffré, on remplace simplement chaque lettre du texte en clair par la lettre qui se trouve trois places plus loin dans l'alphabet "modulo 26". Ainsi, A est remplacé par D, B par E, W par Z, X par A etc. On utilise parfois un décalage autre que 3

### 2. Implémentation
Dans ce ojet on écrira :
-une fonction '''chiffrement(message)''' qui permet de chiffrer une chaine de caractères (écrits en capitales) ;
-une fonction '''dechiffrement(message_chiffre)''' qui peremt de déchiffrer une chaine de caractères (écrits en capitales) ;
-une fonction principale qui demande a l'utilisateur à choisir entre déchiffrement et chiffrement, avant de lui demander le texte(à chiffrer ou déchiffrer).

### 3. Fichiers
Il faudra donc créer trois fichiers : un fichier '''chiffrement.py''', un fichier '''déchiffrement.py''' et un fichier '''main.py'''