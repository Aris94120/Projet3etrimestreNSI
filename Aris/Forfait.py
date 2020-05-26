def Forfait():
    print("Veuillez choisir un forfait:")
    print("Forfait 1 : forfait v-libre pour les utilisateurs occasionnels")
    print("Forfait 2 : forfait v-plus pour les utilisateurs qui font plus de 4 trajets par mois")
    print("Forfait 3 : forfait v-max, le tout inclus de Vélib', mécanique et électrique")
    f = int(input())
    print("Pour plus de détails sur les forfaits et le prix, veuillez consulter https://www.velib-metropole.fr/offers")
    print("-----------------------------------")

    if f == 1:
        p = int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
        if p == 1:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 30:
                print("Vous allez payer 2 euros pour ", t, "minutes.")
            else:
                prix = (t // 30) * 2
                print("Vous allez payer", prix, "euros pour", t, "minutes.")

        elif p == 2:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 30:
                print("Vous allez payer 1 euros pour ", t, "minutes.")
            else:
                prix = t // 30
                print("Vous allez payer", prix, "euros pour", t, "minutes.")




    elif f == 2:
        p = int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
        if p == 1:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 30:
                print("Vous allez payer 1 euros pour ", t, "minutes.")
            else:
                prix = (t // 30 * 2) - 1
                print("Vous allez payer", prix, "euros pour", t, "minutes.")

        elif p == 2:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 30:
                print("Vous allez payer 0 euros pour ", t, "minutes.")
            else:
                prix = (t // 30) - 1
                print("Vous allez payer", prix, "euros pour", t, "minutes.")

    elif f == 3:
        p = int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
        if p == 1:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 30:
                print("Vous allez payer 0 euros pour ", t, "minutes.")
            else:
                prix = (t // 30) - 1
                print("Vous allez payer", prix, "euros pour", t, "minutes.")

        elif p == 2:
            t = int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
            if t <= 60:
                print("Vous allez payer 0 euros pour ", t, "minutes.")
            else:
                prix = (t // 30) - 2
                print("Vous allez payer", prix, "euros pour", t, "minutes.")

#Forfait()
