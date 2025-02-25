import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('D:\\learning\\rnsit_python\\practice\\IPLData.csv')

# Understanding the data structure
print(df.info())  # Provides data types and non-null values
print(df.isnull().sum())  # Check for missing values
print(df.describe())  # Summary statistics for numerical data
