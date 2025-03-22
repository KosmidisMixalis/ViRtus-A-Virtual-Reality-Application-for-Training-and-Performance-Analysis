import pandas as pd

# Read Excel file
df = pd.read_excel('results.xlsx', header=0)

# Clean column names
df.columns = df.columns.str.replace(r"[\/\n\\]", " ", regex=True)  # Replace /, \n, and \ with space
df.columns = df.columns.str.replace(r"[^\x00-\x7F]+", " ", regex=True)  # Remove non-ASCII characters
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces


def likert_to_percentage(likert_value):
    return ((likert_value - 1) / 4) * 100


# Function to calculate average scores for each category and print the percentage for each question
def calculate_category_scores(df, experience_level):
  

    subset = df[df["Previous Experience with Virtual Reality (VR) Applications"] == experience_level]
   
    questions = [
        'I experienced dizziness, nausea, or discomfort while using the VR application.',
        'I experienced discomfort transitioning from the real world to the virtual environment.',
        'I experienced discomfort transitioning back to the real world after the VR training.'
    ]
    
    # Calculate mean percentage for each question
    question_percentages = {}
    for question in questions:
        mean_score = subset[question].map(likert_to_percentage).mean()
    
        
        question_percentages[question] = mean_score
      
    

    return question_percentages

# Compute scores and print percentages
question_percentages_experiencedVR = calculate_category_scores(df, 'Yes')
question_percentages_inexperiencedVR = calculate_category_scores(df, 'No')


print("Intensity of Motion Sickness in the two groups")

# Print the results for experienced VR users
print("Experienced VR Users - Percentage per Question:")
for question, percentage in question_percentages_experiencedVR.items():
    print(f"{question}: {percentage:.2f}%")

# Print the results for inexperienced VR users
print("Inexperienced VR Users - Percentage per Question:")
for question, percentage in question_percentages_inexperiencedVR.items():
    print(f"{question}: {percentage:.2f}%")
