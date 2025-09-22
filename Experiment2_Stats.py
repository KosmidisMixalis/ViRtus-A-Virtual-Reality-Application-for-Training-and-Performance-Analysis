import math
import numpy as np
from scipy.stats import kruskal, f_oneway, ttest_ind, shapiro, levene
import scikit_posthocs as sp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.power import FTestAnovaPower,TTestIndPower

########################## Helper Functions ##########################
def standard_deviation(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values))
    return math.sqrt(variance)

def convert_to_seconds(time_str):
    if '.' in time_str:
        minutes, seconds = map(int, time_str.split('.'))
    else:
        minutes, seconds = int(time_str), 0
    return minutes * 60 + seconds

def check_shapiro(data, label, alpha=0.05):
    stat, p = shapiro(data)
    if p > alpha:
        print(f"{label}: Normally distributed (f = {stat:.4f}, p = {p:.4f})")
    else:
        print(f"{label}: NOT normally distributed (f = {stat:.4f}, p = {p:.4f})")
    return p

def check_levene(*groups, label="", alpha=0.05):
    stat, p = levene(*groups)
    if p > alpha:
        print(f"{label}: Variances are homogeneous  (f = {stat:.4f}, p = {p:.4f})")
    else:
        print(f"{label}: Variances are NOT homogeneous (f = {stat:.4f}, p = {p:.4f})")
    return p

def kruskal_epsilon_squared(kw_stat, n_total):
    return kw_stat / (n_total - 1)

def anova_eta_squared(groups, all_data):
    ss_between = sum(len(g) * (np.mean(g) - np.mean(all_data))**2 for g in groups)
    ss_total = sum((x - np.mean(all_data))**2 for x in all_data)
    return ss_between / ss_total

########################## Data before ##########################

# VR Train Time, Errors, Completion Time, Trainer Time
real_world_completion_errors_G1_before = [1,0,3,3,0]
real_world_completion_time_G1_before = ["12.39", "6.20", "14.34", "12.5", "10.20"]

real_world_completion_errors_G2_before = [0,0,0,0,0]
real_world_completion_time_G2_before = ["6.5", "6.558", "6.29", "6.56", "8.08"]

real_world_completion_errors_G3_before = [0,3,0,0,3]
real_world_completion_time_G3_before = ["9.58", "10.05", "12.55", "9.55", "10.54"]

########################## Data after ##########################

# VR Train Time, Errors, Completion Time, Trainer Time
real_world_completion_errors_G1 = [4,3,0,0,0]
real_world_completion_time_G1 = ["6.55", "6.50", "12", "7.53", "10"]

real_world_completion_errors_G2 = [0,0,0,0,0]
real_world_completion_time_G2 = ["4.45", "6.50", "4", "6.30", "6.40"]

real_world_completion_errors_G3 = [0,5,0,0,0]
real_world_completion_time_G3 = ["5.20", "14.16", "8.56", "8.58", "8.10"]

alpha = 0.05


############################################# Std and Medians Before #############################################


print("\n################### Group1 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G1_before)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G1_before)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G1_before]
print(f'Average Real World Completion Time Before: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

print("\n################### Group2 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G2_before)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G2_before)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G2_before]
print(f'Average Real World Completion Time Before: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')


print("\n################### Group3 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G3_before)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G3_before)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G3_before]
print(f'Real World Completion Time Before: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')


############################################# Std and Medians after #############################################


print("\n################### Group1 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G1)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G1)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G1]
print(f'Average Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

print("\n################### Group2 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G2)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G2)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G2]
print(f'Average Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')


print("\n################### Group3 ####################")

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G3)/5}, Std Dev: {standard_deviation(real_world_completion_errors_G3)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G3]
print(f'Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')



####################################################


real_world_completion_time_G1 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G1])
real_world_completion_time_G2 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G2])
real_world_completion_time_G3 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G3])


########################## Assumption Tests ##########################
print("\nTEST 1 : Shapiro-Wilk Normality Tests\n")

check_shapiro(real_world_completion_errors_G1, "Group 1 Errors")
check_shapiro(real_world_completion_errors_G2, "Group 2 Errors")
check_shapiro(real_world_completion_errors_G3, "Group 3 Errors")

check_shapiro(real_world_completion_time_G1, "Group 1 Completion Time")
check_shapiro(real_world_completion_time_G2, "Group 2 Completion Time")
check_shapiro(real_world_completion_time_G3, "Group 3 Completion Time")

print("\nTEST 2 : Levene’s Test for Homogeneity of Variances\n")
check_levene(real_world_completion_errors_G1, real_world_completion_errors_G2, real_world_completion_errors_G3, label="Errors Across Groups")
check_levene(real_world_completion_time_G1, real_world_completion_time_G2, real_world_completion_time_G3, label="Completion Time Across Groups")

########################## Kruskal-Wallis + ε² ##########################

print("\n[Errors: Kruskal-Wallis + Dunn Post-hoc]")
kw_errors = kruskal(real_world_completion_errors_G1, real_world_completion_errors_G2, real_world_completion_errors_G3)
print("Kruskal-Wallis H-test:", kw_errors)
dunn_errors = sp.posthoc_dunn([real_world_completion_errors_G1, real_world_completion_errors_G2, real_world_completion_errors_G3], p_adjust='holm')
print("Dunn’s Post-hoc p-values:\n", dunn_errors)
n_total_errors = len(real_world_completion_errors_G1) + len(real_world_completion_errors_G2) + len(real_world_completion_errors_G3)
epsilon_sq_errors = kruskal_epsilon_squared(kw_errors.statistic, n_total_errors)
print(f"Errors effect size (ε²) = {epsilon_sq_errors:.3f}")

########################## ANOVA + η² + Power ##########################
print("\n[Completion Time: One-way ANOVA + Tukey Post-hoc]")
anova_completion = f_oneway(real_world_completion_time_G1, real_world_completion_time_G2, real_world_completion_time_G3)
print("One-way ANOVA:", anova_completion)

all_data = np.concatenate([real_world_completion_time_G1, real_world_completion_time_G2, real_world_completion_time_G3])
labels = (["G1"]*len(real_world_completion_time_G1) + ["G2"]*len(real_world_completion_time_G2) + ["G3"]*len(real_world_completion_time_G3))
tukey_completion = pairwise_tukeyhsd(endog=all_data, groups=labels, alpha=0.05)
print(tukey_completion)

eta_sq_completion = anova_eta_squared([real_world_completion_time_G1, real_world_completion_time_G2, real_world_completion_time_G3], all_data)
print(f"Completion Time effect size (η²) = {eta_sq_completion:.3f}")

# Power analysis
anova_power = FTestAnovaPower()
effect_size_f = np.sqrt(eta_sq_completion / (1 - eta_sq_completion))
n_total = len(all_data)
k_groups = 3
power = anova_power.solve_power(effect_size=effect_size_f, nobs=n_total, alpha=alpha, k_groups=k_groups)
print(f"Power of the ANOVA test: {power:.3f}")



print("\n POWER ANALYSIS \n")


# Approximate power for Kruskal-Wallis using effect size epsilon-squared.    
#  Converts epsilon-squared to Cohen's f for use with ANOVA power calculation.

def kruskal_power(epsilon_squared, n_groups, n_per_group, alpha=0.05):
    # Cohen's f approximation: f = sqrt(eta^2 / (1 - eta^2))
    f = np.sqrt(epsilon_squared / (1 - epsilon_squared))
    power_analysis = FTestAnovaPower()
    return power_analysis.solve_power(effect_size=f, nobs=n_per_group * n_groups,
                                     alpha=alpha, k_groups=n_groups)

# Calculate power for one-way ANOVA using eta-squared effect size.
def anova_power(eta_squared, n_groups, n_per_group, alpha=0.05):

    f = np.sqrt(eta_squared / (1 - eta_squared))
    power_analysis = FTestAnovaPower()
    return power_analysis.solve_power(effect_size=f, nobs=n_per_group * n_groups,
                                     alpha=alpha, k_groups=n_groups)

n_groups = 3
n_per_group = 5

# Kruskal-Wallis results
epsilon_errors = 0.145      # Real-World Errors ε²

# ANOVA results
eta_completion_time = 0.333  # Completion Time η²



# ---- Calculate power ----
power_errors = kruskal_power(epsilon_errors, n_groups, n_per_group)
power_completion_time = anova_power(eta_completion_time, n_groups, n_per_group)

# Print results with interpretations
print(f"Power (Errors, Kruskal-Wallis): {power_errors:.3f}")
print(f"Power (Completion Time, ANOVA): {power_completion_time:.3f}")
