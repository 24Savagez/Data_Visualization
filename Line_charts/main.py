import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# path of the file to read
spotify_filepath = "spotify.csv"

# read the file
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# print the last 5 row of the data
# print(spotify_data.tail())

print(list(spotify_data.columns))

# set the width and height of the figure
plt.figure(figsize=(14, 6))

# add title
plt.title("Daily Global Streams of Popular Song in 2017-2018")

# line chart showing daily global streams of each song
# sns.lineplot(data=spotify_data)

# line chart showing daily global streams of "shape of you"
sns.lineplot(data=spotify_data["Shape of You"], label="Shape of You")

# line chart showing daily global streams of "Despacito"
sns.lineplot(data=spotify_data["Despacito"], label="Despacito")

# add label for horizontal axis
plt.xlabel("Date")

# show figure
plt.show()
