import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# path of the file to read
iris_filepath = "iris.csv"

# read the file
iris_data = pd.read_csv(iris_filepath, index_col='Id')

# print the first 5 row of the data
print(iris_data.columns)

# histogram
# sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)

# kernel density estimate (KDE) plot
# sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# two-dimensional (2D) KDE plot
# sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data["Sepal Width (cm)"], kind='kde')

# path of the files to read
iris_set_filepath = 'iris_setosa.csv'
iris_ver_filepath = 'iris_versicolor.csv'
iris_vir_filepath = 'iris_virginica.csv'

# read the files
iris_set_data = pd.read_csv(iris_set_filepath, index_col="Id")
iris_ver_data = pd.read_csv(iris_ver_filepath, index_col="Id")
iris_vir_data = pd.read_csv(iris_vir_filepath, index_col="Id")

# histograms for each species
# sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
# sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
# sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)
#
# # add title
# plt.title("Histogram of Petal Lengths, by Species")
#
# # force legend to appear
# plt.legend()

# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

# add title
plt.title("Distribution of Petal Lengths, by Species")

# show figure
plt.show()
