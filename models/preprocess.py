import numpy as np
import pandas as pd
import os

def load_data(filename):
    '''
    The following function loads the data set into a numpy array.
    '''
    df=pd.read_csv(filename, sep=',', skiprows=1, header=None)
    return df.values

def preprocess_data(filename):
    '''
    The following function will preprocess the data by limiting our dataset
    to only contain symptoms.
    '''
    assert os.path.isfile(filename), "The file you inputted does not exist."
    data = load_data(filename)
    
    # We removed unwanted columns that are not symptoms of COVID-19
    sanitized_data = np.delete(data, slice(13,20), 1)

    X = convert(sanitized_data[:, :-1])
    y = convert(sanitized_data[:, -1])
    return X, y

def convert(data):
    '''
    The following function converts yes/no's to 1's/0's
    '''
    data = np.where(data == "Yes", 1, data)
    data = np.where(data == "No", 0, data)
    return data.astype(int)

if __name__ == "__main__":
    X, y = preprocess_data("data/covid-dataset.csv")