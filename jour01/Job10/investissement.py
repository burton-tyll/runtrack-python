montant_initial = 10000

taux_rendement_annuel = 1.03

# Ajout du séparateur de milliers

import locale

locale.setlocale(locale.LC_ALL, '')

montant = montant_initial * taux_rendement_annuel

montant_milliers = locale.format_string("%d", montant, grouping=True)

# Affichage du rendement au cours de la première année

print("Le retour sur investissement de la 1ère année est de "+montant_milliers+"€")

# Deuxième Année

taux_rendement_annuel = 1.05

montant = montant + 5000

montant = montant * taux_rendement_annuel

montant_milliers = locale.format_string("%d", montant, grouping=True)

print("Le retour sur investissement de la 2ème année est de "+montant_milliers+"€")

# 3eme année

montant = montant - montant*0.1

taux_rendement_annuel= taux_rendement_annuel - taux_rendement_annuel * 0.01

montant = montant * taux_rendement_annuel

montant_milliers = locale.format_string("%d", montant, grouping=True)

print("Le retour sur investissement total est de "+montant_milliers+"€")

