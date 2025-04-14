import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

df['Status'].unique()
df[df['Status'] == 'Uncontested']
plt.figure(figsize=(10, 10))
plt.boxplot(df['Margin'],labels=['Margin'])
plt.title("Box Plot for Margin")
plt.show()

pd.set_option('Display.max_columns', 5)
pd.set_option('Display.max_rows', 500)
df.sort_values(by = 'Margin' ,ascending=False, inplace=True)

# Creating a new dataframe for Leading party and number of seats won along with useful data vizualizations
df_leading_party=df.groupby("Leading Party")
df_number_seats_won_by_each_party = df_leading_party['Status'].count().sort_values(ascending=False)
df_number_seats_won_by_each_party = pd.DataFrame(df_number_seats_won_by_each_party)
df_number_seats_won_by_each_party.rename(columns={'Status': 'Seats Won'}, inplace=True) # renaming status column to seats won column
df_number_seats_won_by_each_party.columns
df_number_seats_won_by_each_party

# Calculating the length of dataset of df_number_seats_won_by_each_party
len(df_number_seats_won_by_each_party)

# I want to number of the serial column to start from 1 instead of 0 if we reset the Dataframe we will get numbering from 0 so creating a list and then adding the list in the dataframe
# creating a list of the length of df_number_seats_won_by_each_party
column_index = []
for i in range(1,43):
    column_index.append(i)
column_index
df_number_seats_won_by_each_party["S.No"] = column_index # adding the index values starting from 1 to the dataframe
df_number_seats_won_by_each_party.reset_index(inplace=True) # resetting the index and then setting it to S.No
df_number_seats_won_by_each_party.set_index('S.No', inplace=True) # setting up the index to S.NO
df_number_seats_won_by_each_party.head(10).plot(kind="barh", x='Leading Party' ,y = 'Seats Won') # creating a basic horizontal box plots for visualization
plt.show()

#Checking the number of constituencies which have margin's greater than the median margin in the election of 2024 
len(df[df['Margin'] >= df['Margin'].median()])

#Grouping it by statewise and displyaing the count
df['Constituency'] = df['Constituency'].str.lower()
df['Constituency']

df.to_csv("/Users/badrinathsanagavaram/Desktop/GitHUB practice folder/Python Pandas Projects/india-election-analysis-2024/data/elections-data-2024-cleaned.csv", index=False)

