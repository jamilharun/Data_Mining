# Import necessary libraries
import pandas as pd

# Read in the data
data = pd.read_csv("data.csv")

# Select only the relevant columns
data = data[["column1", "column2", "column3"]]

# Remove any rows with missing values
data = data.dropna()

# Summarize the data
mean = data.mean()
median = data.median()
mode = data.mode()

# Output the results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
