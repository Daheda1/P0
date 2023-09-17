from kingdomino import get_terrain
import os
from collections import defaultdict
import cv2 as cv
import pandas as pd

from collections import defaultdict
import pandas as pd

def test_get_terrain(folder_path):
    confusion_matrix = defaultdict(lambda: defaultdict(int))
    unique_terrains = []
    
    total_correct = 0
    total_count = 0

    # Dictionary til at holde styr på antallet af korrekte og totale prøver for hver klasse
    correct_counts = defaultdict(int)
    total_counts = defaultdict(int)
    
    for terrain_type in os.listdir(folder_path):
        terrain_folder = os.path.join(folder_path, terrain_type)
        
        if os.path.isdir(terrain_folder):
            if terrain_type not in unique_terrains:
                unique_terrains.append(terrain_type)
            
            for tile_file in os.listdir(terrain_folder):
                tile_path = os.path.join(terrain_folder, tile_file)
                
                tile = cv.imread(tile_path)
                if tile is None:
                    print(f"Could not read the image from {tile_path}. Skipping...")
                    continue
                
                predicted_terrain = get_terrain(tile)
                
                if predicted_terrain not in unique_terrains:
                    unique_terrains.append(predicted_terrain)
                
                confusion_matrix[terrain_type][predicted_terrain] += 1
                
                total_count += 1
                total_counts[terrain_type] += 1
                
                if predicted_terrain == terrain_type:
                    total_correct += 1
                    correct_counts[terrain_type] += 1
    
    # Beregn nøjagtighed for hver klasse og total nøjagtighed
    overall_accuracy = (total_correct / total_count) * 100 if total_count > 0 else 0
    print(f"Overall accuracy: {overall_accuracy}%")
    
    for terrain_type in unique_terrains:
        accuracy = (correct_counts[terrain_type] / total_counts[terrain_type]) * 100 if total_counts[terrain_type] > 0 else 0
        print(f"Accuracy for {terrain_type}: {accuracy}%")
    
    df = pd.DataFrame(confusion_matrix, index=unique_terrains, columns=unique_terrains).fillna(0).astype(int)
    return df

# Eksempel på, hvordan du kan kalde testfunktionen og få confusion matrix
conf_matrix = test_get_terrain("/Users/dannihedegaarddahl/Documents/GitHub/P0/Categories")
print(conf_matrix)