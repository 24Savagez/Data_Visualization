import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# path of the file to read
insurance_filepath = "insurance.csv"

# read the file
insurance_data = pd.read_csv(insurance_filepath)

# show 5 first row
print(insurance_data.head())

# scatter plots
# sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# regression line in scatter plots
# sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# take color in scatter plots
# sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# add line regression
# sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)

# categorical scatter plot
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])

# show figure
plt.show()
