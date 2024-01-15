import pandas as pd

df_iris = pd.read_csv('iris_data/iris.data', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

print(df_iris)