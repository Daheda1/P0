from kingdomino import get_terrain
import os
import cv2 as cv
import pandas as pd

def test_get_terrain(folder_path):
    unique_terrains = set()
    total_correct = 0
    total_count = 0

    # Initialize DataFrame to store confusion matrix
    confusion_matrix = pd.DataFrame()

    # Dictionary to keep track of the correct and total counts for each class
    correct_counts = {}
    total_counts = {}
    
    for terrain_type in os.listdir(folder_path):
        terrain_folder = os.path.join(folder_path, terrain_type)
        
        if os.path.isdir(terrain_folder):
            unique_terrains.add(terrain_type)
            
            for tile_file in os.listdir(terrain_folder):
                tile_path = os.path.join(terrain_folder, tile_file)
                
                tile = cv.imread(tile_path)
                if tile is None:
                    print(f"Could not read the image from {tile_path}. Skipping...")
                    continue
                
                predicted_terrain = get_terrain(tile)
                unique_terrains.add(predicted_terrain)

                # Update confusion matrix
                confusion_matrix.at[terrain_type, predicted_terrain] = confusion_matrix.at[terrain_type, predicted_terrain] + 1 if terrain_type in confusion_matrix.index and predicted_terrain in confusion_matrix.columns else 1

                total_count += 1
                total_counts[terrain_type] = total_counts.get(terrain_type, 0) + 1
                
                if predicted_terrain == terrain_type:
                    total_correct += 1
                    correct_counts[terrain_type] = correct_counts.get(terrain_type, 0) + 1
    
    # Calculate accuracy for each class and overall accuracy
    overall_accuracy = (total_correct / total_count) * 100 if total_count > 0 else 0
    print(f"Overall accuracy: {overall_accuracy}%")
    
    for terrain_type in unique_terrains:
        accuracy = (correct_counts.get(terrain_type, 0) / total_counts.get(terrain_type, 1)) * 100
        print(f"Accuracy for {terrain_type}: {accuracy}%")

    # Fill missing values in confusion matrix with 0 and convert to integers
    confusion_matrix = confusion_matrix.fillna(0).astype(int)
    
    return confusion_matrix

# Example on how to call the test function and get the confusion matrix
conf_matrix = test_get_terrain("/Users/dannihedegaarddahl/Documents/GitHub/P0/categories testset")
print(conf_matrix)
