#Umrechnung
def kg_in_gramm(kg: float) -> float:
    return kg * 1000

def cm_in_zoll(cm: float) -> float:
    return cm / 2.54

def kW_in_W(kW: float) -> float:
    return kW * 1000

#Wenn die Eingabe für die umzurechnende Einheit kein float ist, wird dieser hier abgefangen und auf eine gültige Eingabe gewartet.
def is_valid_float(str) -> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False

#Bediener Auswahl
def Umrechner(): 
    while True:
        print("\n Wählen Sie eine Umrechnungsmöglichkeit:")
        print("\n 1. kg zu gr \
               \n 2. cm zu Zoll \
               \n 3. kW zu W \
               \n 4. Beenden")
            
               

#Auswahlaufforderung
        choice = input("\nGeben Sie die Nummer Ihrer Wahl ein: ")

#variable Berechnung
        if choice == '1':
            kg: str = input("Geben Sie die kg ein: ")
            kg = kg.replace(",", ".")
            kg = float(kg)
            if is_valid_float(kg):
                kg_float: float = float(kg)
                g: float = kg_in_gramm(kg_float)
                print(f"\n {kg_float} Kilogramm sind {g} Gramm.\n")
            else:
                print("\n Ungültige Eingabe. Bitte geben Sie eine gültige Zahl ein.\n")
        
        elif choice == '2':
            cm: str = input("Geben Sie die cm ein: ")
            cm = cm.replace(",", ".")
            cm = float(cm)
            if is_valid_float(cm):
                cm_float: float = float(cm)
                zoll: float = cm_in_zoll(cm_float)
                print (f"\n {cm_float} cm sind {zoll} Zoll. \n")
            else:
                print("\n Ungültige Eingabe. Bite geben Sie eine gültige Zahl ein. \n")
            
        elif choice == '3':
            kW: str = input("Geben Sie die kW ein: ")
            kW = kW.replace(",", ".")
            kW = float(kW)
            if is_valid_float(kW):
                kW_float: float = float(kW)
                W: float = kW_in_W(kW_float)
                print (f"\n {kW_float} kw sind {W} W.")
            else:
                print("\n Ungültige Eingabe. Bite geben Sie eine gültige Zahl ein. \n")

        elif choice == '4':
            print("\n Programm beendet")
            break
              
        else:
            print("\nUngültige Wahl. Bitte wählen Sie eine gültige Option.\n")

#Menüauswahl
Umrechner()