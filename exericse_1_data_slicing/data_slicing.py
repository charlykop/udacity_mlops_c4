import pandas as pd

################## Meine Loesung
def load_data(data_path, column_names):
    df_iris = pd.read_csv(data_path, names = column_names)
    return df_iris

def analyse_slice_data(df, label):
    df_slice = df.loc[df['label']==label].drop('label', axis=1)
    return df_slice.describe()

################# Musterloesung
def slice_iris(df, feature):
    """ Function for calculating descriptive stats on slices of the Iris dataset."""
    for cls in df["label"].unique():
        df_temp = df[df["label"] == cls]
        mean = df_temp[feature].mean()
        stddev = df_temp[feature].std()
        print(f"Class: {cls}")
        print(f"{feature} mean: {mean:.4f}")
        print(f"{feature} stddev: {stddev:.4f}")
    print()

if __name__ == "__main__": 
    df_iris = load_data('iris_data/iris.data', ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label'])
    
    ################## Meine Loesung
    print(analyse_slice_data(df_iris, 'Iris-setosa'))
    print(analyse_slice_data(df_iris, 'Iris-versicolor'))
    print(analyse_slice_data(df_iris, 'Iris-virginica'))

    ################# Musterloesung
    slice_iris(df_iris, "sepal_length")
    slice_iris(df_iris, "sepal_width")
    slice_iris(df_iris, "petal_length")
    slice_iris(df_iris, "petal_width")


