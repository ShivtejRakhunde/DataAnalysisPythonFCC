import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    #conversion into 3*3 numpy array
    m = np.array(list).reshape((3,3))
    #mean
    mean_rows = np.mean(m, axis=0)
    mean_cols = np.mean(m, axis=1)
    mean_all = np.mean(m)

    #varience
    var_rows = np.var(m, axis=0)
    var_cols = np.var(m, axis=1)
    var_all = np.var(m)

    #SD
    std_rows = np.std(m, axis=0)
    std_cols = np.std(m, axis=1)
    std_all = np.std(m)

    # Max
    max_rows = np.max(m, axis=0)
    max_cols = np.max(m, axis=1)
    max_all = np.max(m)
    
    # Min
    min_rows = np.min(m, axis=0)
    min_cols = np.min(m, axis=1)
    min_all = np.min(m)
    
    # Sum
    sum_rows = np.sum(m, axis=0)
    sum_cols = np.sum(m, axis=1)
    sum_all = np.sum(m)

    #store results in dictionary
    calculations = {
    'mean': [mean_rows.tolist(), mean_cols.tolist(), mean_all],
    'variance': [var_rows.tolist(), var_cols.tolist(), var_all],
    'standard deviation': [std_rows.tolist(), std_cols.tolist(), std_all],
    'max': [max_rows.tolist(), max_cols.tolist(), max_all],
    'min': [min_rows.tolist(), min_cols.tolist(), min_all],
    'sum': [sum_rows.tolist(), sum_cols.tolist(), sum_all]
    }

    return calculations