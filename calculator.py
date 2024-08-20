#Umrechnung
def kg_in_gramm(kg):
    return kg * 1000

def cm_in_zoll(cm):
    return cm * 2,54

def kW_in_W(kW):
    return kW * 1000

#Bediener Auswahl
def Umrechner():
    while True:
        print("Wählen Sie eine Umrechnungsmöglichkeit:")
        print("1. kg zu gr")
        print("2. cm zu Zoll")
        print("3. kW zu W")
        print("4. Beenden")

#Auswahlaufforderung
        choice = input("Geben Sie die Nummer Ihrer Wahl ein: ")

#variable Berechnung
        if choice == '1':
            kg = float(input("Geben Sie die kg ein: "))
            g = kg_in_gramm(kg)
            print(f"{kg} Kilogramm sind {g} Gramm.\n")
        
        elif choice == '2':
            cm = float(input("Geben Sie die cm ein: "))
            zoll = cm_in_zoll(cm)
            print (f"{cm} cm sind {zoll} Zoll. \n")
            
        elif choice == '3':
            kW = float(input("Geben Sie die kW ein: "))
            W = kW_in_W(kW)
            print (F"{kW} kw sind {W} W.")

#Schleife unterbrechen
        elif choice == '4':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Wahl. Bitte wählen Sie eine gültige Option.\n")

#Menüauswahl
Umrechner()