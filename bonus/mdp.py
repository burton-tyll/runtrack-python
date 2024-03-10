enter_username = "Entrez votre nom d'utilisateur : "
enter_mdp = "Entrez votre mot de passe : "
quitter = "Entrez 1 pour quitter le gestionnaire ou 2 pour continuer : "

# Initialisation des listes pour stocker les utilisateurs, les mots de passe et les identifiants
username = []
mdp = []
userid = []

# Fonction pour ajouter un utilisateur
def adduser():
    user_choice = ""
    i = 0

    while user_choice != 1:
        user = input(enter_username)
        motdepasse = input(enter_mdp)

        # Ajout des informations de l'utilisateur dans les listes
        username.append(user)
        mdp.append(motdepasse)
        userid.append(i)

        print("Utilisateurs : ", username)
        print("Mots de passe : ", mdp)
        print("Identifiants : ", userid)

        i += 1

        user_choice = input(quitter)

        # Vérification de la saisie de l'utilisateur
        if user_choice == "1" or user_choice == "2":
            user_choice = int(user_choice)
        else:
            print("Veuillez entrer 1 ou 2.")

            # Si la saisie n'est pas valide, on annule l'ajout de l'utilisateur précédent
            username.pop(-1)
            mdp.pop(-1)
            userid.pop(-1)

    print("\n________________________________________________\n")
    return username, mdp, userid

# Fonction pour afficher les informations d'un utilisateur
def show_user(user):
    if user in username:
        i = username.index(user)
        print("Nom d'utilisateur : ", username[i])
        print("Mot de passe : ", mdp[i])
        print("Identifiant : ", userid[i])
    else:
        print("Utilisateur non trouvé.")

# Appel de la fonction pour ajouter un utilisateur
adduser()

# Appel de la fonction pour afficher les informations de l'utilisateur 
show_user("burton")