#Ma calculatrice

print("=== CALCULATRICE ===")

print("1 - Addition")
print("2 - Soustraction")
print("3 - Multiplication")
print("4 - Division")

choix = input("Choisissez une opération : ")

nombre1 = float(input("Premier nombre : "))
nombre2 = float(input("Deuxième nombre : "))

if choix == "1":
    resultat = nombre1 + nombre2
    print(f"Résultat : {resultat}")

elif choix == "2":
    resultat = nombre1 - nombre2
    print(f"Résultat : {resultat}")

elif choix == "3":
    resultat = nombre1 * nombre2
    print(f"Résultat : {resultat}")


elif choix == "4":
    if nombre2 == 0:
        print("Erreur : division par zéro impossible.")
    else:
        resultat = nombre1 / nombre2
        print(f"Résultat : {resultat}")

else:
    print("Opération inconnue.")
