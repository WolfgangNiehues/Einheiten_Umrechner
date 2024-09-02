# str->float
def bed_eing_ausw ():
    check_bed = False
    while check_bed == False:
        bed_eing = input("\n Auswahl: ")
        if bed_eing in ["1", "2" , "3" , "4" , "5" , "6" , "7"]:
            check_bed = True
        else:
            print(" ungültige Eingabe\
                    \n bitte wählen Sie eine der vorgeschlagenen Zahlen")
    return bed_eing
    
# Eingabe Umrechnungswerte float, Komma zu Punkt und runden nach 3 Dezimalstellen
def float_auswahl_wert():
    check_ausw = False
    while check_ausw == False:
        aus_wahl_wert = input ("\n Wert: ")
        aus_wahl_wert=aus_wahl_wert.replace("," , ".")
        try:
            aus_wahl_wert_float = float (aus_wahl_wert)
            check_ausw = True
        except ValueError:
            print(" ungültige Eingabe\
                 \n Bitte geben Sie einen Wert ein, welcher umgerechnet werden kann")
    return aus_wahl_wert_float

while True:
    
# Bedienereingabe Menü
    print("	\n Wähe aus zwischen: \
            \n 1: cm -> zoll \
            \n 2: cm -> m \
            \n 3: °C -> °F \
            \n 4: °F -> °C \
            \n 5: g -> uncen\
            \n 6: uncen -> g\
            \n 7: beenden")
    
#Check korrekte Menue- Auswahl, weitergabe an case
    Menue_eingabe = bed_eing_ausw()

#Beenden
    if Menue_eingabe == '7':
        print(" auf wiedersehen")
        break
    
#Bediener Eingabe Umrechnen
    aus_wahl_gepr = float_auswahl_wert()

#Berechnung und Ausgabe
    match Menue_eingabe:
        
        #cm -> zoll
        case '1':
            ergebniss = aus_wahl_gepr/2.54
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f"\n {aus_wahl_gepr}cm sind {ergebniss} Zoll")
        
        #cm -> m
        case '2':
            ergebniss = aus_wahl_gepr/100
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f"{aus_wahl_gepr}cm sind {ergebniss} m")
        
        #°C -> °F
        case '3':
            ergebniss = (aus_wahl_gepr * 9/5) + 32
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f" {aus_wahl_gepr}°C sind {ergebniss} °F")
        
        #°F -> °C
        case '4':
            ergebniss = (aus_wahl_gepr-32)*5/9
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f" {aus_wahl_gepr}°F sind {ergebniss} °C")
        
        #g -> uncen
        case '5':
            ergebniss = aus_wahl_gepr/28.3495231
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f" {aus_wahl_gepr}g sind {ergebniss} uncen")
        
        #uncen -> g
        case '6':
            ergebniss = aus_wahl_gepr*28.3495231
            ergebniss = round (ergebniss ,3) #ergebniss wird gerundet überschrieben
            print(f" {aus_wahl_gepr}uncen sind {ergebniss} g")


 

        
  

        

        
        
    
    
    
