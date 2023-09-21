import cv2 as cv
import numpy as np
import os
from kingdomino import get_tiles

# Main function containing the backbone of the program
def main():
    output_folder = "/Users/dannihedegaarddahl/Documents/GitHub/P0"
    input_folder = "/Users/dannihedegaarddahl/Documents/GitHub/P0/King Domino testset"


    for filename in os.listdir(input_folder):
        image_path = input_folder +"/" +filename
        print(image_path)
        if not os.path.isfile(image_path):
            print("Image not found")
            return
        image = cv.imread(image_path)
        tiles = get_tiles(image)
        print(len(tiles))
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                save_tile(tile, output_folder, filename, x, y)


def save_tile(tile, output_folder, image_name, x, y):
    # Create a folder for 'blandet' if it doesn't exist
    if not os.path.exists(os.path.join(output_folder, "blandet")):
        os.makedirs(os.path.join(output_folder, "blandet"))

    # Generate a unique filename for the tile based on the image name and tile coordinates
    tile_filename = f"{image_name}_{x}_{y}.png"

    # Save the tile to the 'blandet' folder
    tile_path = os.path.join(output_folder, "blandet", tile_filename)
    cv.imwrite(tile_path, tile)

    print(f"Saved Tile as {tile_filename} in 'blandet' folder")


if __name__ == "__main__":
    main()