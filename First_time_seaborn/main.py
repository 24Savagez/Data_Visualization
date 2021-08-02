import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# path of the file to read
fifa_filepath = "fifa.csv"

# read the file into a variable
fifa_data = pd.read_csv(fifa_filepath, index_col='Date', parse_dates=True)

# print the first 5 rows-of the data
# print(fifa_data.head())

# set the width and height of the figure
plt.figure(figsize=(16, 6))

# line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)

# show figure
plt.show()
