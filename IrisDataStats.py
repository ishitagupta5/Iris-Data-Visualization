'''
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
Loads a dataset with assosciated attribute names, then reports on details
of the dataset including statistics and graphs
'''

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# specifying column names
file = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

#loads the data from a csv file into a dataframe
dataset = pandas.read_csv(file, names=names)

#dataset dimensions (number of rows and columns)
print("Dataset Shape:", dataset.shape)

# first 20 rows to get a glimpse of the data
print("Dataset Head (First 20 Rows):\n", dataset.head(20))

# descriptive statistics for numerical features
print("Summary Statistics:\n", dataset.describe())

# class distribution to grasp sample proportions
print("Class Distribution:\n", dataset.groupby('class').size())

# Create box plots for each feature to visualize spread and potential outliers
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# Save the plot for reference
plt.savefig('box.png')

# histograms for each feature to visualize their distributions
dataset.hist()
plt.savefig('hist.png')

# scatter plot matrix to visualize pairwise relationships between features
scatter_matrix(dataset)
plt.savefig('matrix.png')
