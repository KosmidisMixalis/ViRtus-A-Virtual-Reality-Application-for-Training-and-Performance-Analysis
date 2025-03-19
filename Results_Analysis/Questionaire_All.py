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

# Reverse scores for selected questions
for question in reverse_scored_questions:
    if question in df.columns:
        df[question] = 6 - df[question]  # Reverse score transformation

# Print cleaned column names to verify
#print(df.columns.tolist())

# Function to calculate average scores for each category
def calculate_category_scores(df, experience_level):
    subset = df[df["Previous Experience with Virtual Reality (VR) Applications"] == experience_level]

    categories = {
         
        "Motion Sickness": subset[['I experienced dizziness, nausea, or discomfort while using the VR application.',
        'I experienced discomfort transitioning from the real world to the virtual environment.', 
        'I experienced discomfort transitioning back to the real world after the VR training.']].mean().mean(),
        
        "Learning Effectiveness": subset[['The VR training application helped me acquire new skills or knowledge.', 
        'The animations and visualizations (e.g., puzzles, animations) helped me to better understand the process.', 
        'I was confused or lost during the VR training.']].mean().mean(),
                
        "Emotional Response & Motivation": subset[['I felt frustrated or anxious during the VR training.',
         'The VR training was enjoyable compared to the traditional training method.', 
         'I felt motivated to complete the VR training.']].mean().mean(),
        
        "Decision-Making & Critical Thinking": subset[['The VR training required me to make meaningful decisions.', 
         'I feel confident in applying what I learned from the VR training.', 'The VR training helped improve my problem-solving skills.']].mean().mean(),

        "Realism & Practical Application": subset[['The training scenario felt realistic and relevant to real-world application.', 
        'The VR experience effectively simulated the real-world training scenario.']].mean().mean(),

        "Immersion & Presence": subset[['The VR experience felt immersive.', 'I felt present in the virtual environment, as if I were truly there.',
        'The visual and audio elements enhanced my sense of presence and understanding of the training process.']].mean().mean(),
        
        "Usability": subset[['The VR training application was easy to use.', 'The controls were intuitive and easy to learn.', 
        'Interactions in the virtual environment felt natural and responsive.']].mean().mean(),
        
        "Control & Engagement (Flow & Focus)": subset[['I felt in control of my movements and interactions within the VR environment.', 
        'The VR training session was engaging and kept my attention.', 
        'I was able to stay focused without distractions or disruptions.']].mean().mean(),
        
        "Overall Satisfaction & Recommendation": subset[['I would recommend this VR training method to others.', 
        'The VR training paradigm could be a valuable supplementary tool to training procedures.']].mean().mean(),
        }
     
    return categories
    

def calculate_category_scores2(df, experience_level):
    subset = df[df["Experience in the field of Electronics"] == experience_level]

    categories = {
        "Motion Sickness": subset[['I experienced dizziness, nausea, or discomfort while using the VR application.',
        'I experienced discomfort transitioning from the real world to the virtual environment.', 
        'I experienced discomfort transitioning back to the real world after the VR training.']].mean().mean(),
        
        "Learning Effectiveness": subset[['The VR training application helped me acquire new skills or knowledge.', 
        'The animations and visualizations (e.g., puzzles, animations) helped me to better understand the process.', 
        'I was confused or lost during the VR training.']].mean().mean(),
                
        "Emotional Response & Motivation": subset[['I felt frustrated or anxious during the VR training.',
         'The VR training was enjoyable compared to the traditional training method.', 
         'I felt motivated to complete the VR training.']].mean().mean(),
        
        "Decision-Making & Critical Thinking": subset[['The VR training required me to make meaningful decisions.', 
         'I feel confident in applying what I learned from the VR training.', 'The VR training helped improve my problem-solving skills.']].mean().mean(),

        "Realism & Practical Application": subset[['The training scenario felt realistic and relevant to real-world application.', 
        'The VR experience effectively simulated the real-world training scenario.']].mean().mean(),

        "Immersion & Presence": subset[['The VR experience felt immersive.', 'I felt present in the virtual environment, as if I were truly there.',
        'The visual and audio elements enhanced my sense of presence and understanding of the training process.']].mean().mean(),
        
        "Usability": subset[['The VR training application was easy to use.', 'The controls were intuitive and easy to learn.', 
        'Interactions in the virtual environment felt natural and responsive.']].mean().mean(),
        
        "Control & Engagement (Flow & Focus)": subset[['I felt in control of my movements and interactions within the VR environment.', 
        'The VR training session was engaging and kept my attention.', 
        'I was able to stay focused without distractions or disruptions.']].mean().mean(),
        
        "Overall Satisfaction & Recommendation": subset[['I would recommend this VR training method to others.', 
        'The VR training paradigm could be a valuable supplementary tool to training procedures.']].mean().mean(),
    }
    
    return categories

# Compute scores
scores_experiencedVR = calculate_category_scores(df, 'Yes')
scores_inexperiencedVR = calculate_category_scores(df, 'No')

scores_experiencedElectronics = calculate_category_scores2(df, 'Yes')
scores_inexperiencedElectronics = calculate_category_scores2(df, 'No')


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

plot_bar_chart(scores_experiencedVR, "VR Experienced Users - Quality Breakdown")
plot_bar_chart(scores_inexperiencedVR, "VR Inexperienced Users - Quality Breakdown")
plot_bar_chart(scores_experiencedElectronics, "Electronics Experienced Users - Quality Breakdown")
plot_bar_chart(scores_inexperiencedElectronics, "Electronics Inexperienced Users - Quality Breakdown")

