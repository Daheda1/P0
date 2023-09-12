import cv2 as cv
import numpy as np
import os
import csv

def main():
    tiles_folder = ""
    csv_document = ""
    images = load_images_from_folder(tiles_folder)
    for tile in images:
        hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
        hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
        write_to_csv(hue, saturation, value, csv_document)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def write_to_csv(hue, saturation, value, csv_document):
    file = open(csv_document, "w")
    writer = csv.writer(file)
    writer.writerow(f"{hue}, {saturation}, {value}")
    file.close



