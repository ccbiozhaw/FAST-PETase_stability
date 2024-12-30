import pandas as pd
from scipy import stats
import numpy as np

def perform_column_ttests(file_path, sheet1_name, sheet2_name):
    """
    Performs statistical tests between corresponding columns in two Excel worksheets.
    First checks for variance homogeneity using Levene's test, then performs
    either standard t-test (homogeneous variances) or Welch's t-test (heterogeneous variances).
    
    Parameters:
    file_path (str): Path to Excel file
    sheet1_name (str): Name of first worksheet
    sheet2_name (str): Name of second worksheet
    
    Returns:
    DataFrame with statistical test results
    """
    # Read both worksheets
    df1 = pd.read_excel(file_path, sheet_name=sheet1_name)
    df2 = pd.read_excel(file_path, sheet_name=sheet2_name)
    
    # Skip the first column (indices)
    columns = df1.columns[1:]
    
    # Store results
    results = []
    
    # Perform tests for each pair of columns
    for col in columns:
        # Get the data, excluding any NaN values
        data1 = df1[col].dropna()
        data2 = df2[col].dropna()
        
        # Perform Levene's test for homogeneity of variances
        levene_stat, levene_p = stats.levene(data1, data2)
        
        # Choose appropriate t-test based on Levene's test result
        # If levene_p < 0.05, variances are significantly different
        if levene_p < 0.05:
            # Use Welch's t-test for unequal variances
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)
            test_type = "Welch's t-test"
        else:
            # Use standard t-test for equal variances
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=True)
            test_type = "Student's t-test"
        
        # Calculate additional statistics
        mean1 = np.mean(data1)
        mean2 = np.mean(data2)
        std1 = np.std(data1)
        std2 = np.std(data2)
        
        results.append({
            'Column': col,
            'Test_type': test_type,
            'Levene_statistic': levene_stat,
            'Levene_p_value': levene_p,
            't_statistic': t_stat,
            'p_value': p_value,
            f'{sheet1_name}_mean': mean1,
            f'{sheet2_name}_mean': mean2,
            f'{sheet1_name}_std': std1,
            f'{sheet2_name}_std': std2,
            'Significant_0.05': p_value < 0.05,
            'Equal_variances': levene_p >= 0.05
        })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    # Format p-values and statistics for readability
    for col in ['Levene_p_value', 'p_value']:
        results_df[col] = results_df[col].apply(lambda x: f'{x:.4f}')
    
    return results_df

file_path = 'DSSP_WT_FAST_50.xlsx'
sheet1_name = '310_helix_WT_50'
sheet2_name = '310_helix_FAST_50'

results = perform_column_ttests(file_path, sheet1_name, sheet2_name)
print(results)

results.to_excel('ttest_results_310_helix.xlsx', index=False)

file_path = 'DSSP_WT_FAST_50.xlsx'
sheet1_name = 'alpha_helix_WT_50'
sheet2_name = 'alpha_helix_FAST_50'

results = perform_column_ttests(file_path, sheet1_name, sheet2_name)
print(results)

results.to_excel('ttest_results_alpha_helix.xlsx', index=False)