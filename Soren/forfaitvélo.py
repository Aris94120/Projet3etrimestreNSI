f=int(input("Veuillez choisir entre le forfait 1 (forfait v-libre pour les utilisateurs occasionnels, le forfait 2 (forfait v-plus pour les utilisateurs qui font plus de 4 trajets par mois) et enfin, le forfait 3 (forfait v-max, le tout inclus de Vélib', mécanique et électrique)."))
print("Pour plus de détails sur les forfaits et le prix, veuillez consulter https://www.velib-metropole.fr/offers")
if f==1 :
    p=int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
    if p==1 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 2 euros pour ",t, "minutes.")
        elif t>=30 and t<=60 :
            print("Vous allez payer 4 euros pour ",t, "minutes.")
        else :
            print("Vous allez payer 4 euros plus 2 euros toutes les 30 minutes")
    elif p==2 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 1 euros pour ",t, "minutes.")
        elif t>=30 and t<=60 :
            print("Vous allez payer 2 euros pour ",t, "minutes.")
        else :
            print("Vous allez payer 2 euros plus 1 euros toutes les 30 minutes")
elif f==2 :
    p=int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
    if p==1 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 1 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
        elif t>=30 and t<=60 :
            print("Vous allez payer 3 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
        else :
            print("Vous allez payer 3 euros plus 2 euros toutes les 30 minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
    elif p==2 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 0 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
        elif t>=30 and t<=60 :
            print("Vous allez payer 1 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
        else :
            print("Vous allez payer 1 euros plus 1 euros toutes les 30 minutes (Obligation de prendre l'abonnement à 3.10 euros/mois pendant 12 mois).")
else :
    p=int(input("Vous voulez un vélib éléctrique (1) ou un vélib mécanique (2) ?"))
    if p==1 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 0 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")
        elif t>=30 and t<=60 :
            print("Vous allez payer 1 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")
        else :
            print("Vous allez payer 1 euros plus 1 euros toutes les 30 minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")
    elif p==2 :
        t=int(input("Veuillez indiquer le nombre de minutes d'utilisation de votre vélib."))
        if t<=30 :
            print("Vous allez payer 0 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")
        elif t>=30 and t<=60 :
            print("Vous allez payer 0 euros pour ",t, "minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")
        else :
            print("Vous allez payer 0 euros plus 1 euros toutes les 30 minutes (Obligation de prendre l'abonnement à 8.30 euros/mois pendant 12 mois).")