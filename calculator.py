#Umrechnung
def kg_in_gramm(kg):
    return kg * 1000

def cm_in_zoll(cm):
    return cm * 2,54

def kW_in_W(kW):
    return kW * 1000

#Wenn die Eingabe für die umzurechnende Einheit kein float ist, wird dieser hier abgefangen und auf eine gültige Eingabe gewartet.
def is_valid_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

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
            kg = input("Geben Sie die kg ein: ")
            if is_valid_float(kg):
                kg = float(kg)
                g = kg_in_gramm(kg)
                print(f"{kg} Kilogramm sind {g} Gramm.\n")
            else:
                print("\n Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.\n")
        
        elif choice == '2':
            cm = input("Geben Sie die cm ein: ")
            if is_valid_float(cm):
                cm = float(cm)
                zoll = cm_in_zoll(cm)
                print (f"{cm} cm sind {zoll} Zoll. \n")
            else:
                print("\n Ungültige Eingabe. Bite geben Sie eine gültige Zahl ein. \n")
            
        elif choice == '3':
            kW = input("Geben Sie die kW ein: ")
            if is_valid_float(kW):
                kW = float(kW)
                W = kW_in_W(kW)
                print (F"{kW} kw sind {W} W.")
            else:
                print("\n Ungültige Eingabe. Bite geben Sie eine gültige Zahl ein. \n")

        elif choice == '4':
            print("Programm beendet.")
            break
              
        else:
            print("\nUngültige Wahl. Bitte wählen Sie eine gültige Option.\n")

#Menüauswahl
Umrechner()