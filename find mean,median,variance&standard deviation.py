#WAP to find mean,median,variance and standard deviation of the list using numpy

import numpy as np

def mean_median_variance_std_dev(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    variance = np.var(numbers)
    std_dev = np.std(numbers)
    return mean, median, variance, std_dev

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
mean, median, variance, std_dev = mean_median_variance_std_dev(numbers)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
