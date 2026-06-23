import random

def spiel ():
    print("Willkommen beim Spiel des Zahlenratens")
    print()
    print("Ich überlege mir eine Zahl zwischen 1 bis 10.\n\n")

    # Computer wählt zufällige Zahl
    zahl = random.randint(1, 10)

    versuche = 3 #Einstellung Anzahl Versuche

    #Spielschleife
    while versuche > 0:
        try:
            eingabe = int(input("Deine Zahl zwischen (1-10) "))

        #Eingabe überprüfen
            if eingabe  < 1 or eingabe > 10:
                print ("Bitte nur Zahlen zwischen 1 bis 10 eingeben!\n\n")
                continue

        except ValueError:
            print("Das war keine Zahl, bitte erneut eingeben.\n\n")

        #Zahl richtig erraten
        if eingabe == zahl:
            print()
            print("Glückwunsch, du hast gewonnen!")
            return
        else: 
            versuche -= 1

            if eingabe < zahl:
                print ()
                print ()
                print("Zu niedrig.\n\n\n")

            else:
                print()
                print()
                print ("Zu hoch.\n\n\n")
 
            print (f"Verbleibende Versuche: {versuche}\n\n")        

    #Wenn Versuche aufgebraucht sind
    print(f"Leider verloren, die richtige Zahl war {zahl}.")

#Spiel starten
spiel()
input("\n\n\nSpiel beendet. Drücke Enter zum Schließen.")
