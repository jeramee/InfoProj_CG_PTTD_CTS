# ctss_simulation.py

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from multiprocessing import Pool

def simulate_trial(sample_size, effect_size, dropout_rate):
    """
    Simulate a clinical trial with a given sample size, effect size, and dropout rate.
    This function generates treatment and control groups, performs a t-test, and calculates
    survival curves using the Kaplan-Meier estimator.
    
    Args:
        sample_size (int): Number of participants in the trial.
        effect_size (float): Expected effect size in the treatment group.
        dropout_rate (float): Fraction of participants dropping out.
    
    Returns:
        Dict: A dictionary containing p-values, sample sizes, and survival curves.
    """
    treatment = np.random.normal(loc=effect_size, scale=1, size=sample_size)
    control = np.random.normal(loc=0, scale=1, size=sample_size)
    treatment = treatment[np.random.rand(sample_size) > dropout_rate]
    control = control[np.random.rand(sample_size) > dropout_rate]
    t_stat, p_value = stats.ttest_ind(treatment, control)
    kmf = KaplanMeierFitter()
    kmf.fit(treatment, event_observed=np.random.binomial(1, 0.9, size=len(treatment)))
    return {"p_value": p_value, "sample_size": len(treatment), "survival_curve": kmf.survival_function_}

def run_simulations(num_trials, sample_size, effect_size, dropout_rate):
    """
    Run multiple clinical trial simulations in parallel using multiprocessing.
    
    Args:
        num_trials (int): Number of trials to simulate.
        sample_size (int): Number of participants per trial.
        effect_size (float): Expected effect size.
        dropout_rate (float): Fraction of participants dropping out.
    
    Returns:
        DataFrame: Results of the simulation.
    """
    with Pool() as pool:
        results = pool.starmap(simulate_trial, [(sample_size, effect_size, dropout_rate) for _ in range(num_trials)])
    return pd.DataFrame(results)
