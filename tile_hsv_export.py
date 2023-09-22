import cv2 as cv
import numpy as np
import os
import csv
# Definerer "main" funktionen
def main():
# tiles_folder er en variabel, der indeholder en filsti til mappen med vores tiles.
    tiles_folder = "/Users/dannihedegaarddahl/Documents/GitHub/P0/Categories/Field"
# csv_document er en variabel, der indeholder en filsti til en CSV-dokumentfil, som gemmer på gennemsnittet af vores grænseværdier.
    csv_document = "/Users/dannihedegaarddahl/Documents/GitHub/P0/forest.csv"

# images er en variabel, der gemmer på billederne fra funktionen load_images_from_folder, hvis input er en parameter bestående af tiles_folder.
    images = load_images_from_folder(tiles_folder)
# "File" er en variabel, der bruger open funktionen, som åbner en fil i skrivetilstand, der er gemt i variablen csv_document
    file = open(csv_document, "w")
# Variablen writer gør det muligt at skrive data til filen i CSV-format
    writer = csv.writer(file)
#  for loop, som kører hver enkelt tile igennem i listen images.
    for tile in images:
# Variablen hsv_tile omdanner hver enkel tile fra BGR-farvekode til HSV-farvekode
        hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
# Biblioteket numpy beregner gennemsnittet af værdierne, fra hele billedet
        hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
# Print udskriver værdierne af variablerne hue, saturation og value
        print( hue, saturation, value)
# Her kaldes funktionen write_to_csv, som skriver værdierne af hue, saturation og value til en CSV-fil.
        write_to_csv(hue, saturation, value, writer)

    file.close

# Her defineres funktionen "load_images_from_folder" med en enkel parameter "folder", som er en sti.
def load_images_from_folder(folder):
# Der oprettes her en tom liste ved navn images.
    images = []
# for loop, som kører hvert enkelt element igennem i filename i mappen folder vha. os.listdir
    for filename in os.listdir(folder):
# Biblioteket cv bruger metoden cv.imread til at indlæse et billede i "filename" i mappen "f"older"
        img = cv.imread(os.path.join(folder, filename))
# if statement, som tjekker, om cv.imread returnerer et gyldigt billede.
        if img:
# Listen images bliver forlænget med det gyldige billede ved brug af metoden append.
            images.append(img)
# Når loopet er færdigt, returneres billederne fra images
    return images

# Her defineres en funktion ved navn write_to_csv med fire parametre som input.
# De tre første er værdierne på hue, saturation og value. Parameteret writer er en csv-skriver, som gør det muligt at skrive data til en CSV-fil
def write_to_csv(hue, saturation, value, writer):
# I funktionen bruger writer metoden writerow til at skrive en enkel række af data bestående af hue, saturation og value i en liste til CSV-filen.
    writer.writerow([hue, saturation, value])

main()

