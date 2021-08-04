import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# path of the file read
flight_filepath = "flight_delays.csv"

# read the file
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# print the data
# print(flight_data)

# bar charts
# set the width and height fo the figure
# plt.figure(figsize=(10, 6))
#
# # add title
# plt.title("Average Arrival Delay for spirit Airlines Flights, by Month")
#
# # bar chart
# sns.barplot(x=flight_data.index, y=flight_data["NK"])
#
# # add label for vertical axis
# plt.ylabel("Arrival delay (in minutes)")

# heatmaps
# set the width and height of the figure
plt.figure(figsize=(14, 7))

# add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# heatmap showing
sns.heatmap(data=flight_data, annot=True)

# add label for horizontal axis
plt.xlabel("Airline")

# show figure
plt.show()
