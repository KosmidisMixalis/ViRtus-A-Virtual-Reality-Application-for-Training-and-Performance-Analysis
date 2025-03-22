import matplotlib.pyplot as plt

# Define the groups
g1_elec = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g1_vr = [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
g2_elec = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g2_vr = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
g3 = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]

# Function to plot pie charts for each group and save the figure
def plot_group_pie(data, group_name, subgroups, save_path):
    # Create subplots
    fig, axes = plt.subplots(1, len(subgroups), figsize=(12, 6))

    # If there's only one subplot, `axes` will be an Axes object, not an array.
    if len(subgroups) == 1:
        axes = [axes]  # Convert to a list so we can iterate over it
    
    # Loop through each subgroup
    for i, (subgroup, ax) in enumerate(zip(subgroups, axes)):
        # Count Yes (1's) and No (0's)
        yes_count = sum(subgroup)
        no_count = len(subgroup) - yes_count
        
        # Data for the pie chart
        labels = ['Yes', 'No']
        sizes = [yes_count, no_count]
        colors = ['#FF4500', '#0D98BA']  # Orange-Red and Blue-Green
        # Create a pie chart for the subgroup
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, 
                                          startangle=90, wedgeprops={'edgecolor': 'Black', 'linewidth': 1.5})
        
        # Style the text in the pie chart for clarity
        for autotext in autotexts:
            autotext.set_fontsize(20)
            autotext.set_color('black')  # White color for better visibility

         # Increase the font size of the 'Yes' and 'No' labels
        for text in texts:
            text.set_fontsize(20)  # Set font size for Yes/No labels
            
        
    
    # Adjust layout to avoid overlap with the main title and ensure clean presentation
    # plt.tight_layout(rect=[0, 0.03, 1, 0.95])  
    
    # Save the figure
    plt.savefig(save_path, format='png', bbox_inches='tight')  # Save as PNG (you can change the format if desired)
    print(f"Figure saved as {save_path}")
    
    plt.show()

# Plot each group with subgroups as subfigures and save the figure
plot_group_pie(None, "G1 - Exp in Electronics", [g1_elec], "group_1_El_pie_chart.png")
plot_group_pie(None, "G1 - Exp in VR", [g1_vr], "group_1_VR_pie_chart.png")
plot_group_pie(None, "G2 - Exp in Electronics", [g2_elec], "group_2_El_pie_chart.png")
plot_group_pie(None, "G2 - Exp in VR", [g2_vr], "group_2_VR_pie_chart.png")
plot_group_pie(None, "G3 - Exp in Electronics", [g3], "group_3_pie_chart.png")  # g3 is already a single list, but we pass it as a list
