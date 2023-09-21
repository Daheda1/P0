import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Indlæs den kombinerede CSV-fil
csv_path = "CSV/combined.csv"  # Ændr denne sti til din egen fil
combined_df = pd.read_csv(csv_path)

# Sæt farvepaletten op
palette = sns.color_palette("hsv", len(combined_df['category'].unique()))

# Opret en farvemapping for hver kategori
color_mapping = {category: palette[i] for i, category in enumerate(combined_df['category'].unique())}

# Initialiser 3D-plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot hver kategori med forskellige farver
for category, color in color_mapping.items():
    subset_df = combined_df[combined_df['category'] == category]
    ax.scatter(subset_df['Hue'], subset_df['Saturation'], subset_df['Value'], label=category, c=[color]*len(subset_df), s=30)

# Tilføj etiketter og legende
ax.set_xlabel('Hue')
ax.set_ylabel('Saturation')
ax.set_zlabel('Value')
ax.legend(title='Category')

plt.title('3D Plot of Hue, Saturation, and Value by Category')
plt.show()
