# str->float
def bed_eing_1 ():
    check_bed = False
    while check_bed == False:
        bed_eing = input("\n Auswahl: ")
        if bed_eing in ["1", "2" , "3" , "4" , "5"]:
            check_bed = True
        else:
            print(" veruche es erneut")
    return bed_eing
    
# Eingabe Umrechnungswerte float, Komma zu Punkt und runden nach 3 Dezimalstellen
def float_auswahl():
    check_ausw = False
    while check_ausw == False:
        aus_wahl = input ("\n Wert: ")
        aus_wahl=aus_wahl.replace("," , ".")
        try:
            aus_wahl=float (aus_wahl)
            check_ausw = True
            return aus_wahl
        except ValueError:
            print(" ungültige Eingabe")

# Bedienereingabe Menü
print("	\n Wähe aus zwischen: \
        \n 1: cm -> zoll \
        \n 2: cm -> m \
        \n 3: °C -> °F \
        \n 4: °F -> °C \
        \n 5: beenden")

#Check korrekte Menue- Auswahl, weitergabe an case
Menue_eingabe = bed_eing_1()

#Bediener Eingabe Umrechnen
aus_wahl_gepr = float_auswahl()

#Berechnung und Ausgabe
match Menue_eingabe:
    case '1':
        ergebniss = aus_wahl_gepr/2.54
        ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
        print(f"\n {aus_wahl_gepr}cm sind {ergebniss} Zoll")
        
    case '2':
        ergebniss = aus_wahl_gepr/100
        ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
        print(f"{aus_wahl_gepr}cm sind {ergebniss} m")
        
    case '3':
        ergebniss = (aus_wahl_gepr * 9/5) + 32
        ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
        print(f" {aus_wahl_gepr}°C sind {ergebniss} °F")
        
    case '4':
        ergebniss = aus_wahl_gepr* 9/5 + 32
        ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
        print(f" {aus_wahl_gepr}°F sind {ergebniss} °C")
        
  

        
  

        

        
        
    
    
    
