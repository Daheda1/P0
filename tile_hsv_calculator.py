import cv2 as cv
import numpy as np
import os
import csv

def main():
    tiles_folder = "/Users/dannihedegaarddahl/Documents/GitHub/P0/King Domino dataset (1)"
    csv_document = "/Users/dannihedegaarddahl/Documents/GitHub/P0/test.csv"
    images = load_images_from_folder(tiles_folder)
    file = open(csv_document, "w")
    writer = csv.writer(file)
    for tile in images:
        hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
        hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
        print( hue, saturation, value)
        write_to_csv(hue, saturation, value, writer)
    file.close


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def write_to_csv(hue, saturation, value, writer):
    writer.writerow([hue, saturation, value])


main()

