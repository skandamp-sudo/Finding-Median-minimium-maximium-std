import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)

sum_a = np.sum(a)
print("Sum:", sum_a)

product = np.prod(a)
print("Product:", product)

mean = np.mean(a)
print("Mean:", mean)

standard_deviation = np.std(a)
print("Standard deviation:", standard_deviation)

variance = np.var(a)
print("Variance:", variance)

minimum = np.min(a)
print("Minimum value:", minimum)

maximum = np.max(a)
print("Maximum value:", maximum)

minimum_index = np.argmin(a)
print("Minimum index:", minimum_index)

maximum_index = np.argmax(a)
print("Maximum index:", maximum_index)

median = np.median(a)
print("Median:", median)
