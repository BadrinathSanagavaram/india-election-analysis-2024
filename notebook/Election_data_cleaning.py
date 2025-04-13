import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# Reading the Data

df = pd.read_csv('/Users/badrinathsanagavaram/Desktop/GitHUB practice folder/Python Pandas Projects/india-election-analysis-2024/data/election_results_2024_raw.csv')
df

#Data Cleaning

df.columns
df.isna().sum()
df.isnull().sum()

# we have one Trailing party , Margin and Trailing Candidate from the same datapoint as NA [Null] this is because the Leading party from that particular constituency has won the election unanimously
df[df['Trailing Candidate'].isna()]

# what we can do is that we can replace the NA value with no party contested
df['Trailing Candidate'].replace(np.nan, 'No Candidate contested', inplace=True)
df['Trailing Party'].replace(np.nan, 'No Party contested', inplace=True)

df[df['Trailing Candidate'].isna()] # the result of this an empty dataframe


# finding the set of unique values
df.nunique()

# while exploring for NaN candidate party and cadidate name we found out that the margin is also '-' let us try to find out if there are any other values like that in the dataset

df[df['Margin'] == '-']
df.dtypes

# we have to convert Margin column into numric column because we have perform certain transformations on that in order to do that we need to replace '-' with a value in the previous elections Surat was won with a margin of 5,43,000 votes by the Same BJP which won this seat too so in order to replace this we can exchange with that value

df['Margin'].replace('5,43,000', 543000, inplace=True)
df[df['Margin'] == '-'] # checking whether the value is still present in the Dataframe or not

df['Margin'] = df['Margin'].astype(int) # converting the margin column to int
df.dtypes # re-checking the datatypes of all other columns
# checking whether the changes have been made in that particular datapoint 493 or not 
df[df['Constituency'] == 'Surat']