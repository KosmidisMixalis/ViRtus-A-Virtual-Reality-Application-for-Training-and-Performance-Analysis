import math

def standard_deviation(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

############### Avg. Age ####################
var_g1_list = [24,28,26,23,28,21,21,19,19,58,24,23,25,23,20,21,21,21,21,22]
var_g2_list = [28,31,25,29,29,21,28,20,25,20,28,23,25,25,47,19,29,42,23,19]
var_g3_list = [19,61,19,23,20,20,45,26,24,56,25,22,24,25,40,25,25,25,23,24]

print(f'Avg. Age Group1: {sum(var_g1_list)/20}, Std Dev: {standard_deviation(var_g1_list)}')
print(f'Avg. Age Group2: {sum(var_g2_list)/20}, Std Dev: {standard_deviation(var_g2_list)}')
print(f'Avg. Age Group3: {sum(var_g3_list)/20}, Std Dev: {standard_deviation(var_g3_list)}')

############### Stats Experiment 1 #############
################# Groups Stats #################

def convert_to_seconds(time_str):
    if '.' in time_str:
        minutes, seconds = map(int, time_str.split('.'))
    else:
        minutes, seconds = int(time_str), 0
    return minutes * 60 + seconds

def convert_to_minutes_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"

#############################################
print("################### Group1 ####################")

# VR Train Time
time_list = ["8.41", "12.26", "11.24", "10.55", "17.19", "9.19", "12.15", "9.30", "11.31", "18.54", "12.50", "7", "10.07", "6.14", "6.50", "10.43", "6.10", "8.32", "8.16", "6.20"]
time_seconds = [convert_to_seconds(time) for time in time_list]
print(f'Average VR Train Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

# Errors
errors = [1,0,3,0,3,1,1,2,3,0,0,0,0,1,0,0,3,5,1,5]
print(f'Avg. Real World Errors: {sum(errors)/20}, Std Dev: {standard_deviation(errors)}')

# Real World Completion Time
time_lst = ["12.39", "6.20", "14.34", "10.20", "12.5", "7.25", "7.59", "14.19", "12.34", "8.14", "10.45", "10.20", "10.19", "9.38", "7.15", "9.56", "7.34", "9", "7", "7.25"]
time_seconds = [convert_to_seconds(time) for time in time_lst]
print(f'Average Real World Completion Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

#############################################
print("################### Group2 ####################")

# VR Train Time
time_list = ["8.47", "5.32", "4.17", "7.04", "7.21", "7.18", "10.56", "7.23", "8.32", "8.02", "14.5", "7.34", "6.32", "10.17", "9.38", "9.13", "7.57", "11.26", "8.02", "7.15"]
time_seconds = [convert_to_seconds(time) for time in time_list]
print(f'Average VR Train Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

# Errors
errors = [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]
print(f'Avg. Real World Errors: {sum(errors)/20}, Std Dev: {standard_deviation(errors)}')

# Real World Completion Time
time_lst = ["6.58", "8.08", "6.50", "6.29", "6.56", "12", "14.2", "8.36", "7.10", "7.22", "9.40", "5.15", "10.52", "9.08", "8.10", "8.51", "8.04", "8.20", "10.17", "9.05"]
time_seconds = [convert_to_seconds(time) for time in time_lst]
print(f'Average Real World Completion Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

# Trainer spent Time At the beginning plus Time spent when guided trainee in the VR
time_lst = ["6.14", "4", "5.30", "5", "8.18", "9.49", "7.5", "9.30", "6.5", "8.51", "8.5", "9.42", "9.25", "9.25", "10.24", "10.50", "6.48", "6.20", "7.20", "7.30"]
time_seconds = [convert_to_seconds(time) for time in time_lst]
print(f'Average Time At the beginning plus guided trainee in VR: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

#############################################
print("################### Group3 ####################")

# Train Time From Trainer {Demo time at the beginning + If asked for help}
time_list = ["7", "7.11", "8", "5.21", "6.47", "6.47", "6.50", "8.42", "8.04", "10.50", "8.05", "9.05", "9.05", "6.57", "10.24", "8.45", "7.48", "10.1", "6.48", "6.58"]
time_seconds = [convert_to_seconds(time) for time in time_list]
print(f'Average VR Train Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

# Errors
errors = [2,3,0,0,1,2,0,2,0,1,3,3,0,1,0,0,0,3,0,0]
print(f'Avg. Real World Errors: {sum(errors)/20}, Std Dev: {standard_deviation(errors)}')

# Real World Completion Time
time_lst = ["10.2", "10.54", "13", "12.55", "7.05", "8.05", "6", "7.42", "8.16", "9.55", "11.12", "8.25", "5.55", "12.05", "9.09", "8.12", "9.58", "10.05", "6.34", "9.55"]
time_seconds = [convert_to_seconds(time) for time in time_lst]
print(f'Real World Completion Time: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')

# Trainer spent Time with supervision
time_lst = ["17.2", "18.05", "21", "18.16", "13.52", "14.52", "12.50", "16.24", "16.20", "20.45", "19.17", "17.30", "15", "19.02", "19.33", "16.57", "17.46", "20.06", "13.22", "16.53"]
time_seconds = [convert_to_seconds(time) for time in time_lst]
print(f'Average Time Demonstration plus Supervision: {convert_to_minutes_seconds(sum(time_seconds)//len(time_seconds))}, Std Dev: {convert_to_minutes_seconds(int(standard_deviation(time_seconds)))}')
