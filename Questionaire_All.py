import matplotlib.pyplot as plt
import pandas as pd


# Read Excel file
df = pd.read_excel('results.xlsx', header=0)

# Remove unwanted characters like slashes, newlines, backslashes, and any non-printable characters
df.columns = df.columns.str.replace(r"[\/\n\\]", " ", regex=True)  # Replace /, \n, and \ with space
df.columns = df.columns.str.replace(r"[^\x00-\x7F]+", " ", regex=True)  # Remove non-ASCII characters
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces

# Display all rows and columns
pd.set_option("display.max_rows", None)  
pd.set_option("display.max_columns", None)  


reverse_scored_questions = [
    'I was confused or lost during the VR training.',
    'I felt frustrated or anxious during the VR training.'
]
# Function to convert Likert scale (1-5) to 0-100 scale
def likert_to_percentage(likert_value):
    return ((likert_value - 1) / 4) * 100

def likert_to_0_4(likert_value):
    return likert_value - 1  # Convert from (1-5) to (0-4)

# Reverse scores for selected questions
for question in reverse_scored_questions:
    if question in df.columns:
        df[question] = 6 - df[question]  # Reverse score transformation

# Function to calculate average scores for each category (using the whole sample)
def calculate_category_scores(df):
    categories = {
        
        "Usability": df[['The VR training application was easy to use.', 'The controls were intuitive and easy to learn.', 
        'Interactions in the virtual environment felt natural and responsive.']].map(likert_to_0_4).mean().mean(),
        
        "Immersion & Presence": df[['The VR experience felt immersive.', 'I felt present in the virtual environment, as if I were truly there.',
        'The visual and audio elements enhanced my sense of presence and understanding of the training process.']].map(likert_to_0_4).mean().mean(),
        
        "Control & Engagement (Flow & Focus)": df[['I felt in control of my movements and interactions within the VR environment.', 
        'The VR training session was engaging and kept my attention.', 
        'I was able to stay focused without distractions or disruptions.']].map(likert_to_0_4).mean().mean(),
         
        "Learning Effectiveness": df[['The VR training application helped me acquire new skills or knowledge.', 
        'The animations and visualizations (e.g., puzzles, animations) helped me to better understand the process.', 
        'I was confused or lost during the VR training.']].map(likert_to_0_4).mean().mean(),
        
        "Motion Sickness": df[['I experienced dizziness, nausea, or discomfort while using the VR application.',
        'I experienced discomfort transitioning from the real world to the virtual environment.', 
        'I experienced discomfort transitioning back to the real world after the VR training.']].map(likert_to_0_4).mean().mean(),
        
        "Emotional Response & Motivation": df[['I felt frustrated or anxious during the VR training.',
        'The VR training was enjoyable compared to the traditional training method.', 
        'I felt motivated to complete the VR training.']].map(likert_to_0_4).mean().mean(),
        
        "Decision-Making & Critical Thinking": df[['The VR training required me to make meaningful decisions.', 
        'I feel confident in applying what I learned from the VR training.', 'The VR training helped improve my problem-solving skills.']].map(likert_to_0_4).mean().mean(),

        "Realism & Practical Application": df[['The training scenario felt realistic and relevant to real-world application.', 
        'The VR experience effectively simulated the real-world training scenario.']].map(likert_to_0_4).mean().mean(),

        "Overall Satisfaction & Recommendation": df[['I would recommend this VR training method to others.', 
        'The VR training paradigm could be a valuable supplementary tool to training procedures.']].map(likert_to_0_4).mean().mean(),
    }
     
    return categories



# Compute scores for the entire sample (no subgroups)
scores_all_sample = calculate_category_scores(df)
print("Category Scores (in Percentage):\n")
for category, score in scores_all_sample.items():
    print(f"{category}: {score:.2f}%")

# Function to plot bar chart for category scores as percentages
def plot_bar_chart(scores, title):
    categories = list(scores.keys())
    # Convert each score to percentage
    scores_values = [score for score in scores.values()]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, scores_values, color='blue', alpha=0.7)
    plt.xlabel('Categories')
    plt.ylabel('Average Score (%)')
    plt.title(title)
    
    # Rotate category labels to avoid overlap
    plt.xticks(rotation=45, ha='right')
    
    # Use tight_layout to adjust layout and avoid clipping of labels
    plt.tight_layout()
    
    # Save the chart as a PNG file
    plt.savefig(f'{title}.png')
    
    # Show the chart
    plt.show()
    plt.close()

# Plot results for the entire sample
plot_bar_chart(scores_all_sample, "Overall Sample - Quality Breakdown")
