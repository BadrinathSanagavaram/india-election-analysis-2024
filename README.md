India 2024 Election Data Cleaning & Transformation Project


📘 Overview
This project focuses on cleaning, transforming, and analyzing the 2024 Indian General Elections dataset to extract actionable insights about constituencies, winning margins, and party performance. The work was conducted in two major phases:

Data Cleaning — Addressing data quality issues such as missing values and inconsistent formats.

Data Transformation and Enrichment — Structuring the dataset to enable visual and statistical analysis by integrating constituency-state mappings and preparing it for dashboarding and further modeling.

This README outlines the entire workflow, tools used, challenges faced, and techniques implemented in detail.

📂 Dataset Overview
Raw File: election_results_2024_raw.csv

Cleaned Output: elections-data-2024-cleaned.csv

Party-wise Output: elections-party_wise_results.csv

Key columns included:

Constituency, Leading Candidate, Trailing Candidate

Leading Party, Trailing Party

Margin, Status

🛠️ Phase 1: Data Cleaning
1.1 Reading the Data
The raw dataset was ingested using pandas. Initial inspections revealed the presence of missing values and data inconsistencies, particularly in the Trailing Candidate, Trailing Party, and Margin columns.

1.2 Handling Missing Values
Constituencies with NaN values in both Trailing Candidate and Trailing Party were examined.

These NaN values were determined to represent uncontested wins and were replaced with:

"No Candidate contested" for Trailing Candidate

"No Party contested" for Trailing Party

1.3 Cleaning Margin Values
A critical issue was observed in the Margin column: some entries used a hyphen (-) instead of a numeric value.

For example, Surat’s margin was '-', which was historically known to be a 543,000 vote margin for BJP. This value was used to replace the missing data.

The Margin column was then cast to int type for numerical operations.

1.4 Data Type Standardization
Ensured correct data types for all columns:

Margin: converted to int

Constituency: standardized to lowercase for downstream consistency

1.5 Uncontested Status Check
Filtered rows where the Status was marked as Uncontested to ensure consistency in downstream calculations and visualizations.

📊 Exploratory Insights & Visualizations
2.1 Margin Distribution
Created a boxplot for the Margin column to understand spread and outliers in winning margins.

High variability was noted, indicating some landslide wins.

2.2 Party-wise Seat Wins
Aggregated the data using groupby('Leading Party') and counted the number of seats won per party.

Generated a horizontal bar chart for the top 10 performing parties.

Added serial numbering (S.No) starting from 1 for tabular presentation.

2.3 Median-Based Margin Analysis
Evaluated how many constituencies had margins greater than the median to identify strong vs. close contests.

This served as a proxy for assessing electoral competitiveness.

🔁 Phase 2: Data Transformation & Structuring
3.1 Constituency Name Normalization
Removed special characters and parenthetical suffixes from Constituency names using regex.

Example: "Nashik (SC)" was transformed to "Nashik"

3.2 Duplication Checks
Checked for duplicated constituencies after normalization. Some cases such as Araku appeared more than once and were verified to avoid skewing results.

3.3 Constituency-State Mapping
A comprehensive Python dictionary was manually curated containing:

28 States + 8 UTs

545 Lok Sabha Constituencies

Each constituency was mapped to its corresponding state to enable geospatial or regional aggregations.

3.4 Merging State Information
Created a DataFrame state_wise_constituencies from the dictionary.

Merged it with the cleaned dataset on the Constituency column using an inner join, ensuring only valid constituency-state combinations were preserved.

Checked for NaN values post-merge to validate completeness.

3.5 Final Export
The cleaned and enriched dataset was exported as:

elections-data-2024-cleaned.csv: contains all key columns + mapped state

elections-party_wise_results.csv: summarized seats won by each party

📈 Candidate-Based Visuals
An example visualization was created:

Compared Rahul Gandhi's margin against other constituencies using a simple matplotlib bar chart.

This concept can be extended to other candidates like Narendra Modi or regional leaders to draw comparative insights.

📦 Tools & Libraries Used
pandas: Data manipulation and aggregation

numpy: Handling missing values and numeric transformations

matplotlib & seaborn: Basic visualizations

plotly: Interactive visuals (used later in Jupyter notebook)

regex: String normalization

Jupyter Notebook: Interactive exploratory analysis
