# str->float
def bed_eing_1 ():
    check_bed = False
    while check_bed == False:
        bed_eing = input(" Auswahl: ")
        if bed_eing in ["1", "2"]:
            check_bed = True
        else:
            print("veruche es erneut")
    return bed_eing

# Eingabe Umrechnungswerte float
def float_auswahl():
    check_ausw = False
    while check_ausw == False:
        aus_wahl = input ("Wert: ")
        aus_wahl=aus_wahl.replace("," , ".")
        try:
            aus_wahl=float (aus_wahl)
            check_ausw = True
            return aus_wahl
        except ValueError:
            print("ungültige Eingabe")

# Bedienereingabe Menü
print("\n Wähe aus wischen: \
       \n 1: cm -> zoll \
       \n 2: cm -> m")

Menue_eingabe = bed_eing_1()

#Bediener Eingabe Umrechnen
aus_wahl_gepr = float_auswahl()

#Auswahl
match Menue_eingabe:
    case '1':
        ergebniss = aus_wahl_gepr/2.54
        ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
        print(f"{aus_wahl_gepr}cm sind {ergebniss} Zoll")
        
    
    
    
