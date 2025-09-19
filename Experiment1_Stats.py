import math
import numpy as np
from scipy.stats import kruskal, f_oneway, ttest_ind, shapiro, levene
import scikit_posthocs as sp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.power import FTestAnovaPower,TTestIndPower

########################## Helper Functions ##########################
def standard_deviation(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
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

########################## Data ##########################

# VR Train Time, Errors, Completion Time, Trainer Time
VR_train_times_lst_G1 = ["8.41", "12.26", "11.24", "10.55", "17.19", "9.19", "12.15", "9.30", "11.31", "18.54", "12.50", "7", "10.07", "6.14", "6.50", "10.43", "6.10", "8.32", "8.16", "6.20"]
real_world_completion_errors_G1 = [1,0,3,0,3,1,1,2,3,0,0,0,0,1,0,0,3,5,1,5]
real_world_completion_time_G1 = ["12.39","6.20","14.34","10.20","12.5","7.25","7.59","14.19","12.34","8.14","10.45","10.20","10.19","9.38","7.15","9.56","7.34","9","7","7.25"]

VR_train_times_lst_G2 = ["8.47","5.32","4.17","7.04","7.21","7.18","10.56","7.23","8.32","8.02","14.5","7.34","6.32","10.17","9.38","9.13","7.57","11.26","8.02","7.15"]
real_world_completion_errors_G2 = [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]
real_world_completion_time_G2 = ["6.58","8.08","6.50","6.29","6.56","12","14.2","8.36","7.10","7.22","9.40","5.15","10.52","9.08","8.10","8.51","8.04","8.20","10.17","9.05"]
trainer_spent_time_G2 = ["6.14","4","5.30","5","8.18","9.49","7.5","9.30","6.5","8.51","8.5","9.42","9.25","9.25","10.24","10.50","6.48","6.20","7.20","7.30"]

trainer_demo_time_G3 = ["7","7.11","8","5.21","6.47","6.47","6.50","8.42","8.04","10.50","8.05","9.05","9.05","6.57","10.24","8.45","7.48","10.1","6.48","6.58"]
real_world_completion_errors_G3 = [2,3,0,0,1,2,0,2,0,1,3,3,0,1,0,0,0,3,0,0]
real_world_completion_time_G3 = ["10.2","10.54","13","12.55","7.05","8.05","6","7.42","8.16","9.55","11.12","8.25","5.55","12.05","9.09","8.12","9.58","10.05","6.34","9.55"]
trainer_spent_time_G3 = ["17.2","18.05","21","18.16","13.52","14.52","12.50","16.24","16.20","20.45","19.17","17.30","15","19.02","19.33","16.57","17.46","20.06","13.22","16.53"]

alpha = 0.05


############################################# Std and Avgs #############################################


print("\n################### Group1 ####################")

# VR Train Time
time_seconds = [convert_to_seconds(time) for time in VR_train_times_lst_G1]
print(f'Average VR Train Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G1)/20}, Std Dev: {standard_deviation(real_world_completion_errors_G1)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G1]
print(f'Average Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

print("\n################### Group2 ####################")

# VR Train Time
time_seconds = [convert_to_seconds(time) for time in VR_train_times_lst_G2]
print(f'Average VR Train Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G2)/20}, Std Dev: {standard_deviation(real_world_completion_errors_G2)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G2]
print(f'Average Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

# Trainer spent Time At the beginning plus Time spent when guided trainee in the VR
time_seconds = [convert_to_seconds(time) for time in trainer_spent_time_G2]
print(f'Average Time At the beginning plus guided trainee in VR: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')


print("\n################### Group3 ####################")

# Train Time From Trainer {Demo time at the beginning + If asked for help}
time_seconds = [convert_to_seconds(time) for time in trainer_demo_time_G3]
print(f'Average VR Train Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

# Errors
print(f'Avg. Real World Errors: {sum(real_world_completion_errors_G3)/20}, Std Dev: {standard_deviation(real_world_completion_errors_G3)}')

# Real World Completion Time
time_seconds = [convert_to_seconds(time) for time in real_world_completion_time_G3]
print(f'Real World Completion Time: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

# Trainer spent Time with supervision
time_seconds = [convert_to_seconds(time) for time in trainer_spent_time_G3]
print(f'Average Time Demonstration plus Supervision: {(sum(time_seconds)//len(time_seconds))}, Std Dev: {(int(standard_deviation(time_seconds)))}')

####################################################

# Convert times to seconds
VR_train_times_lst_G1 = np.array([convert_to_seconds(x) for x in VR_train_times_lst_G1])
VR_train_times_lst_G2 = np.array([convert_to_seconds(x) for x in VR_train_times_lst_G2])
trainer_demo_time_G3 = np.array([convert_to_seconds(x) for x in trainer_demo_time_G3])
real_world_completion_time_G1 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G1])
real_world_completion_time_G2 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G2])
real_world_completion_time_G3 = np.array([convert_to_seconds(x) for x in real_world_completion_time_G3])
trainer_spent_time_G2 = np.array([convert_to_seconds(x) for x in trainer_spent_time_G2])
trainer_spent_time_G3 = np.array([convert_to_seconds(x) for x in trainer_spent_time_G3])

########################## Assumption Tests ##########################
print("\nTEST 1 : Shapiro-Wilk Normality Tests\n")
check_shapiro(VR_train_times_lst_G1, "Group 1 Train Time")
check_shapiro(VR_train_times_lst_G2, "Group 2 Train Time")
check_shapiro(trainer_demo_time_G3, "Group 3 Train Time")

check_shapiro(real_world_completion_errors_G1, "Group 1 Errors")
check_shapiro(real_world_completion_errors_G2, "Group 2 Errors")
check_shapiro(real_world_completion_errors_G3, "Group 3 Errors")

check_shapiro(real_world_completion_time_G1, "Group 1 Completion Time")
check_shapiro(real_world_completion_time_G2, "Group 2 Completion Time")
check_shapiro(real_world_completion_time_G3, "Group 3 Completion Time")

check_shapiro(trainer_spent_time_G2, "Group 2 Trainer Time")
check_shapiro(trainer_spent_time_G3, "Group 3 Trainer Time")

print("\nTEST 2 : Levene’s Test for Homogeneity of Variances\n")
check_levene(VR_train_times_lst_G1, VR_train_times_lst_G2, trainer_demo_time_G3, label="Train Time Across Groups")
check_levene(real_world_completion_errors_G1, real_world_completion_errors_G2, real_world_completion_errors_G3, label="Errors Across Groups")
check_levene(real_world_completion_time_G1, real_world_completion_time_G2, real_world_completion_time_G3, label="Completion Time Across Groups")
check_levene(trainer_spent_time_G2, trainer_spent_time_G3, label="Trainer Time Across Groups")

########################## Kruskal-Wallis + ε² ##########################
print("\n[Train Time: Kruskal-Wallis + Dunn Post-hoc]")
kw_train = kruskal(VR_train_times_lst_G1, VR_train_times_lst_G2, trainer_demo_time_G3)
print("Kruskal-Wallis H-test:", kw_train)
dunn_train = sp.posthoc_dunn([VR_train_times_lst_G1, VR_train_times_lst_G2, trainer_demo_time_G3], p_adjust='holm')
print("Dunn’s Post-hoc p-values:\n", dunn_train)
n_total_train = len(VR_train_times_lst_G1) + len(VR_train_times_lst_G2) + len(trainer_demo_time_G3)
epsilon_sq_train = kruskal_epsilon_squared(kw_train.statistic, n_total_train)
print(f"Train Time effect size (ε²) = {epsilon_sq_train:.3f}")

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

########################## Independent t-test ##########################
print("\n[Trainer Time: Independent t-test (G2 vs G3)]")
tstat, pval = ttest_ind(trainer_spent_time_G2, trainer_spent_time_G3, equal_var=True)
print(f"t-test: t={tstat:.4f}, p={pval:.4f}")

mean_diff = np.mean(trainer_spent_time_G2) - np.mean(trainer_spent_time_G3)
pooled_std = np.sqrt(((len(trainer_spent_time_G2)-1)*np.var(trainer_spent_time_G2, ddof=1) +
                      (len(trainer_spent_time_G3)-1)*np.var(trainer_spent_time_G3, ddof=1)) /
                     (len(trainer_spent_time_G2)+len(trainer_spent_time_G3)-2))
cohen_d = mean_diff / pooled_std
print(f"Cohen’s d: {cohen_d:.3f}")


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

#    Calculate power for independent t-test using Cohen's d
def ttest_power(cohens_d, n_per_group, alpha=0.05):

    power_analysis = TTestIndPower()
    return power_analysis.solve_power(effect_size=cohens_d, nobs1=n_per_group,
                                     alpha=alpha, ratio=1.0, alternative='two-sided')


n_groups = 3
n_per_group = 20

# Kruskal-Wallis results
epsilon_train_time = 0.10  # Train Time ε²
epsilon_errors = 0.21      # Real-World Errors ε²

# ANOVA results
eta_completion_time = 0.047  # Completion Time η²

# t-test results
cohens_d_trainer_time = 4.361  # Trainer Time (G2 vs G3)
n_per_group_ttest = 20

# ---- Calculate power ----
power_train_time = kruskal_power(epsilon_train_time, n_groups, n_per_group)
power_errors = kruskal_power(epsilon_errors, n_groups, n_per_group)
power_completion_time = anova_power(eta_completion_time, n_groups, n_per_group)
power_trainer_time = ttest_power(cohens_d_trainer_time, n_per_group_ttest)

# Print results with interpretations
print(f"Power (Train Time, Kruskal-Wallis): {power_train_time:.3f} - Moderate power, risk of Type II error.")
print(f"Power (Errors, Kruskal-Wallis): {power_errors:.3f} - High power, very low risk of Type II error.")
print(f"Power (Completion Time, ANOVA): {power_completion_time:.3f} - Low power, may fail to detect true effect.")

print(f"Power (Trainer Time, t-test): {power_trainer_time:.3f} - Extremely high, effect is robust.")
