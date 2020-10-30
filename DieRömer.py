
'''
Aufgabe: Schreiben Sie ein Python-Programm, das eine beliebige römische Zahl in eine
         „gewöhnliche” Dezimalzahl umrechnet.
'''

roemische_zahlen = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} # Erstelle ein Dictionary, "übersetze" römische Zahlen in Dezimalzahlen
dezimal_zahlen = 0                                                                   # Instanziiere eine Variable mit dem Namen "dezimal_zahlen"
input_roemisch = input("Römische Zahl eingeben: ")                                   # User Input wird in input_roemisch "gespeichert"

vorherige_zahl = 0                                                                   # Instanziiere eine Variable mit dem Namen "vorherige_zahl"
for char in input_roemisch:                                                          # In Python ist es möglich, über einen String zu iterieren... Iteriere mit einer for-Schleife
    if roemische_zahlen[char] > vorherige_zahl:                                      # Wenn die nachfolgende Ziffer/Zahl größer ist als die vorherige Ziffer/Zahl...
        dezimal_zahlen -= vorherige_zahl                                             # Subtrahiere die vorherige Zahl von der nachfolgenden Zahl
    else:                                                                            # Wenn die nachfolgende Ziffer/Zahl kleiner oder gleich groß ist wie die vorherige Ziffer/Zahl...
        dezimal_zahlen += vorherige_zahl                                             # Addiere die vorherige Zahl mit der nachfolgenden Zahl
    vorherige_zahl = roemische_zahlen[char]                                          # Übersetze die vorherige römische Zahl in eine Dezimalzahl
    #print(roemische_zahlen[char])
    #print(dezimal_zahlen)
dezimal_zahlen += vorherige_zahl                                                     # Sobald die For-Schleife beendet wurde(wenn kein character mehr im Input zu finden ist), wird die letzte Ziffer zur Dezimalsumme addiert

print("Als Dezimalzahl: " + str(dezimal_zahlen))                                     # Ausgabe der Dezimalzahl
