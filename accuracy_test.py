from kingdomino import get_terrain
import os
import cv2 as cv
import pandas as pd
# Definition af funktionen test_get_terrain
def test_get_terrain(folder_path):
    # set () gør, at der ikke kan være duplicates i vores unique_terrains variabel
    unique_terrains = set()
    total_correct = 0
    total_count = 0

    # Bruger pandas dataframeframe funktion til at opbevare vores confusions_matrix i en tabel med rækker og kolonner. 
    confusion_matrix = pd.DataFrame()

    # Hvorfor bruger vi curly brackets her og ikke alm. brackets??? Men den definerer 2 lister: 
    # 1 til tælling af korrekte tællinger og 1 til totale tællinger
    correct_counts = {}
    total_counts = {}
    
    # Laver et outer loop, så den går igennem hver terrain_type mappe. 
    for terrain_type in os.listdir(folder_path):
        terrain_folder = os.path.join(folder_path, terrain_type)
        # Tilfjøjer terrain_type til unique_terrains ud fra et if-statement. 
        if os.path.isdir(terrain_folder):
            unique_terrains.add(terrain_type)
            # Laver et inner loop, der definerer tile_path
            for tile_file in os.listdir(terrain_folder):
                tile_path = os.path.join(terrain_folder, tile_file)
                
                # Vi bruger cv.imread til at indlæse tile_path og definerer det som tile.
                tile = cv.imread(tile_path)
                # Hvis tile ikke er fil/billedfil, så printer programmet en message. Herefter går den videre til næste tile.
                if tile is None:
                    print(f"Could not read the image from {tile_path}. Skipping...")
                    continue
                # Vi definerer predicted_terrain ud fra get_terrain-funktionen, der aflæser et tile. 
                predicted_terrain = get_terrain(tile)
                unique_terrains.add(predicted_terrain)

                # Definerer confunsion_matrix??? 
                confusion_matrix.at[terrain_type, predicted_terrain] = confusion_matrix.at[terrain_type, predicted_terrain] + 1 if terrain_type in confusion_matrix.index and predicted_terrain in confusion_matrix.columns else 1

                total_count += 1
                total_counts[terrain_type] = total_counts.get(terrain_type, 0) + 1
                # Tjekker om predicted_terrain er forskellig fra terrian_type. Herefter ligger den 1 til i total_correct
                # linje 49 forstår jeg ikke helt
                if predicted_terrain == terrain_type:
                    total_correct += 1
                    correct_counts[terrain_type] = correct_counts.get(terrain_type, 0) + 1
    
    # Beregner en overall accuracy i procent og printer svaret som en message. 
    overall_accuracy = (total_correct / total_count) * 100 if total_count > 0 else 0
    print(f"Overall accuracy: {overall_accuracy}%")
    
    # Beregner accuracy for en given terrain_type og printer svaret som en message. 
    for terrain_type in unique_terrains:
        accuracy = (correct_counts.get(terrain_type, 0) / total_counts.get(terrain_type, 1)) * 100
        print(f"Accuracy for {terrain_type}: {accuracy}%")

    # Fill missing values in confusion matrix with 0 and convert to integers
    confusion_matrix = confusion_matrix.fillna(0).astype(int)
    
    return confusion_matrix

# Printer confusion_matrix ud fra funktionen test_get_terrain. 
conf_matrix = test_get_terrain("/Users/dannihedegaarddahl/Documents/GitHub/P0/categories testset")
print(conf_matrix)
