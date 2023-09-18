import cv2 as cv
import numpy as np
import os

# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"/Users/jens-jakobskotingerslev/Documents/GitHub/P0/King Domino dataset (1)/1.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile))
            print("=====")

# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
    
    if 25.5795 <= hue <= 52.6424 and 162.9737 <= saturation <= 243.9017 and 65.3475 <= value <= 171.2089:
        return "Grassland"

    if 26.9323 <= hue <= 66.0016 and 79.1927 <= saturation <= 210.5411 and 28.2416 <= value <= 95.3995:
        return "Forest"

    if 69.1898 <= hue <= 114.243 and 183.0165 <= saturation <= 262.1414 and 98.1857 <= value <= 201.9277:
        return "Lake"

    if 17.8937 <= hue <= 53.1161 and 161.9424 <= saturation <= 262.4836 and 109.3991 <= value <= 210.6415:
        return "Field"

    if 15.1137 <= hue <= 43.3629 and 40.2824 <= saturation <= 179.5934 and 62.2139 <= value <= 145.195:
        return "Swamp"

    if 12.8941 <= hue <= 65.3644 and 44.1873 <= saturation <= 155.6897 and 39.7103 <= value <= 158.3814:
        return "Home"

    if 21.5861 <= hue <= 57.3009 and 56.1645 <= saturation <= 145.6585 and 36.7319 <= value <= 101.2622:
        return "Mine"

    if 15.6347 <= hue <= 26.5975 and 154.7204 <= saturation <= 222.5555 and 101.0583 <= value <= 167.7649:
        return "None"

    return "Unknown"

if __name__ == "__main__":
    main()



