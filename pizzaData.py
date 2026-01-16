import matplotlib.pyplot as plt
import numpy as np

# Step 1: Define data (rows: pizza styles, columns: attributes; 0-10 scale)
# Example pizza data (adapt to yours; assumes 8 attributes)
data = np.array([
    [8.5, 9.0, 7.5, 8.0, 9.5, 8.0, 7.0, 9.0],   # Neapolitan
    [7.0, 8.0, 9.0, 6.5, 7.5, 9.0, 8.5, 8.0],   # Chicago Deep-Dish
    [9.5, 6.5, 8.0, 9.0, 8.5, 7.0, 9.5, 7.5]    # New York Thin-Crust
])

# Step 2: Labels and setup
categories = ['Crust Crisp', 'Sauce Quality', 'Cheese Melt', 'Topping Variety', 
              'Spice Level', 'Portion Size', 'Value for Money', 'Overall Flavor']
N = len(categories)  # 8 variables

# Angles for axes (evenly spaced around circle)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle (duplicate first for closure)

# FIXED: Append first column to close polygons (no loop needed)
data = np.column_stack([data, data[:, 0]])

# Step 3: Create the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))  # Square for symmetry

# Colors and styles
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, orange, green
pizza_names = ['Neapolitan', 'Chicago Deep-Dish', 'New York Thin-Crust']
for i, (row, color, name) in enumerate(zip(data, colors, pizza_names)):
    ax.plot(angles, row, 'o-', linewidth=2.5, markersize=8, 
            label=name, color=color)
    ax.fill(angles, row, color=color, alpha=0.25)  # Filled polygons

# Step 4: Customize axes and labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)  # Readable labels
ax.set_ylim(0, 10)  # Scale to match data (0-10)
ax.set_yticks([2, 4, 6, 8, 10])  # Grid ticks
ax.yaxis.grid(True, linestyle='--', alpha=0.3)  # Subtle grid
ax.set_title('Pizza Style Comparison: Radar Chart', fontsize=16, fontweight='bold', pad=20)

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=11)

# Step 5: High-quality export
plt.tight_layout()
plt.savefig('Pizza_Radar_Fixed.png', dpi=300, bbox_inches='tight', facecolor='white')  # PNG at 300 DPI
plt.show()  # Display on screen