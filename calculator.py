#
#
#
#
#
#
#
#
#
#
# Funktion zur Umrechnung Kilogramm in Gramm
def kg_in_g (kg):
    return kg * 1000

#Nutzereingabe
kilogramm = float(input("Bitte geben Sie das Gewicht in kg ein:"))

#Umrechnung
gramm = kg_in_g(kilogramm)

#Ausgabe

print(f"{kilogramm} Kilogramm sind {gramm} Gramm.")
