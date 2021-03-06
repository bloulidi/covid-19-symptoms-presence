import numpy as np
import pandas as pd
import os
import imblearn
from collections import Counter

def oversample(filename, sampling = 0.5):
    '''
    The following function will oversample the data (duplicate the minority) to tackle our imbalance problem.
    '''
    X, y = preprocess_data(filename)
    oversample = imblearn.over_sampling.RandomOverSampler(sampling_strategy = sampling)
    X_over, y_over = oversample.fit_resample(X, y)
    print(f'Oversampled dataset shape {Counter(y_over)}')
    return X_over, y_over

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
    print('Original dataset shape %s' % Counter(y))
    return X, y

def preprocess_experiment(filename):
    '''
    The following function will preprocess the experimental dataset
    '''
    assert os.path.isfile(filename), "The file you inputted does not exist."
    data = convert(load_data(filename))
    data = np.where(data > 1, 1, data)

    dry_cough = data[:, 0]
    fever = data[:, 1]
    sore_throat = data[:, 2]
    breathing_problems = data[:, 3]
    output = data[:, -1]
    
    data = np.stack((breathing_problems, fever, dry_cough, sore_throat, output), axis=1)
    X = data[:, :-1]
    y = data[:, -1]
    
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
